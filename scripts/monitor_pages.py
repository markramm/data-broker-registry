#!/usr/bin/env python3
"""
Detect changes to every broker's opt-out page, so a human re-verifies the entries whose page
actually moved instead of re-checking all of them on a calendar.

For each authored broker with an http(s) opt_out_url, fetch the page and record:
  - a normalized text snapshot   -> monitor/snapshots/<id>.txt  (git diff of this IS the change)
  - a fingerprint                -> monitor/fingerprints.json
      status, final_url, text_hash, form fields, captcha/vendor signals, last_changed

and report what changed since the previous run: a markdown summary (--report) and one event per
broker needing attention (--events), which .github/workflows/page-monitor.yml files as issues.

Nothing here touches data/: a changed page is a reason to re-verify an entry, never evidence
that the entry is wrong. Fetch failures and bot blocks keep the previous snapshot, so a flaky
week doesn't erase the baseline or show up as a "change".

Limits: plain HTTP fetch, no JavaScript. Pages that render their form client-side fingerprint
their static shell only; those that block bots (403/429/challenge) can't be fingerprinted.

MIT, (C) 2026 Transparency Cascade Press.
"""
import argparse, concurrent.futures as cf, datetime, hashlib, html.parser, json, os, re, sys
import urllib.error, urllib.parse, urllib.request
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import broker_lib as bl

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MONITOR_DIR = os.path.join(HERE, "monitor")
SNAP_DIR = os.path.join(MONITOR_DIR, "snapshots")
FP_PATH = os.path.join(MONITOR_DIR, "fingerprints.json")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
MAX_BYTES = 3_000_000
REPO_URL = (f"{os.environ['GITHUB_SERVER_URL']}/{os.environ['GITHUB_REPOSITORY']}"
            if os.environ.get("GITHUB_REPOSITORY") else "https://github.com/markramm/data-broker-registry")
PRIORITY_ORDER = {"crucial": 0, "high": 1, "standard": 2}

# Elements whose text is chrome or code, not the opt-out process.
SKIP_TAGS = {"script", "style", "noscript", "svg", "template", "nav", "footer", "header", "iframe"}
BLOCK_TAGS = {"p", "div", "li", "tr", "br", "h1", "h2", "h3", "h4", "h5", "h6", "section",
              "article", "main", "form", "label", "option", "td", "th", "dt", "dd", "blockquote"}
FIELD_SKIP_TYPES = {"hidden", "submit", "button", "reset", "image"}
# Field names that are framework plumbing, not something the user is asked for.
FIELD_NOISE = re.compile(r"csrf|token|nonce|captcha|recaptcha|honeypot|^_|viewstate|eventvalidation", re.I)
# A visible challenge widget, not just a library: invisible reCAPTCHA v3 (api.js?render=<key>)
# and the bare word "captcha" in a site-wide bundle are on pages with no user-facing challenge.
CAPTCHA_RE = re.compile(r"""class=["'][^"']*\b(g-recaptcha|h-captcha|cf-turnstile|frc-captcha)\b|data-sitekey=""", re.I)
# Hosted privacy-request portals: when one appears or disappears, the process itself moved.
VENDORS = {
    "onetrust": r"onetrust\.com|privacyportal",
    "trustarc": r"trustarc\.com|truste\.com",
    "transcend": r"transcend\.io",
    "ketch": r"ketch\.com|ketchcdn",
    "osano": r"osano\.com",
    "datagrail": r"datagrail\.io",
    "securiti": r"securiti\.ai",
    "mineos": r"mineos\.ai|saymine",
    "didomi": r"didomi\.io",
    "google_forms": r"docs\.google\.com/forms|forms\.gle",
    "jotform": r"jotform\.com",
    "typeform": r"typeform\.com",
}
GENERATED_NAME = re.compile(r"\d{4,}|^(?=.*\d)[\w-]{25,}$")
CHALLENGE_RE = re.compile(r"just a moment|attention required|cf-browser-verification|cf_chl_|"
                          r"access denied|pardon our interruption|px-captcha|are you a robot|are you human|"
                          r"requested too many times|human verification|verify you are (a )?human|"
                          r"unusual traffic|request unsuccessful|incapsula incident", re.I)


class PageParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.chunks = []
        self.fields = []
        self.title = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag in SKIP_TAGS:
            self.skip += 1
        if tag in BLOCK_TAGS:
            self.chunks.append("\n")
        if tag in ("input", "select", "textarea"):
            ftype = (a.get("type") or tag).lower()
            name = a.get("name") or a.get("id") or ""
            if ftype not in FIELD_SKIP_TYPES and name and not FIELD_NOISE.search(name):
                if GENERATED_NAME.search(name):
                    name = "*"  # form builders mint a new name per render; keep only the type
                self.fields.append(f"{name}:{ftype}")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag in SKIP_TAGS:
            self.skip -= 1

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag in SKIP_TAGS and self.skip:
            self.skip -= 1
        if tag in BLOCK_TAGS:
            self.chunks.append("\n")

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        if not self.skip:
            self.chunks.append(data)


def normalize_text(chunks):
    lines = []
    for line in "".join(chunks).splitlines():
        line = re.sub(r"\s+", " ", line).strip()
        if len(line) < 2 or re.match(r"^(©|copyright\b)", line, re.I):
            continue
        lines.append(line)
    return "\n".join(lines) + "\n" if lines else ""


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read(MAX_BYTES)
            charset = r.headers.get_content_charset() or "utf-8"
            return r.status, r.geturl(), r.headers.get_content_type(), raw.decode(charset, "replace")
    except urllib.error.HTTPError as e:
        try:
            body = e.read(200_000).decode("utf-8", "replace")
        except Exception:
            body = ""
        return e.code, url, "", body
    except Exception as e:
        return 0, url, "", f"{type(e).__name__}: {e}"


def host(url):
    h = (urllib.parse.urlsplit(url).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def is_home_redirect(url, final_url):
    a, b = urllib.parse.urlsplit(url), urllib.parse.urlsplit(final_url)
    return (host(url) == host(final_url) and a.path.strip("/") != ""
            and b.path.strip("/") == "" and not b.query)


def text_hash(text):
    # Order-insensitive: many pages shuffle testimonial/FAQ blocks on every load, and the
    # opt-out process doesn't change when its paragraphs swap places.
    return "sha256:" + hashlib.sha256("\n".join(sorted(set(text.splitlines()))).encode()).hexdigest()


def observe(broker):
    """Fetch one broker's page and return (observation dict, normalized text or None)."""
    url = broker["opt_out_url"]
    code, final_url, ctype, body = fetch(url)
    if code == 0 or code >= 500:
        code, final_url, ctype, body = fetch(url)  # one retry: CI networks drop connections
    obs = {"url": url, "status": code}
    if code == 0:
        obs["state"] = "unreachable"
        obs["error"] = body[:200]
        return obs, None
    if code in (403, 429, 503) or (code < 400 and CHALLENGE_RE.search(body[:20000]) and len(body) < 30000):
        obs["state"] = "bot-blocked"
        return obs, None
    if code >= 500:
        obs["state"] = "unreachable"
        return obs, None
    if code >= 400:
        obs["state"] = "broken"
        return obs, None
    if ctype and "html" not in ctype:
        # PDF or similar: hash the bytes we got rather than parse them.
        obs.update(state="live", final_url=final_url, content_type=ctype,
                   text_hash="sha256:" + hashlib.sha256(body.encode()).hexdigest())
        return obs, None
    p = PageParser()
    try:
        p.feed(body)
    except Exception:
        pass
    text = normalize_text(p.chunks)
    obs.update(
        state="live",
        final_url=final_url,
        home_redirect=is_home_redirect(url, final_url),
        offsite=host(final_url) != host(url),
        title=re.sub(r"\s+", " ", "".join(p.title)).strip()[:200],
        text_hash=text_hash(text),
        text_lines=text.count("\n"),
        fields=sorted(p.fields),
        captcha=bool(CAPTCHA_RE.search(body)),
        vendors=sorted(v for v, rx in VENDORS.items() if re.search(rx, body, re.I)),
    )
    return obs, text


def load_brokers(only=None):
    brokers = []
    for path in bl.iter_broker_files():
        try:
            entry, _ = bl.parse_frontmatter(open(path, encoding="utf-8").read(), path)
        except bl.BrokerFileError:
            continue
        url = (entry.get("opt_out_url") or "").strip()
        if not url.startswith("http") or (only and entry.get("id") not in only):
            continue
        brokers.append(entry)
    return brokers


CONTENT_KEYS = ("final_url", "home_redirect", "offsite", "title", "text_hash", "text_lines",
                "fields", "captcha", "vendors", "content_type")


def significant_lines(old_text, new_text):
    """Lines added or removed, ignoring short label-like lines (<= 3 words): some pages
    rotate placeholder labels ("Phone", "Email") on each load, and real process changes
    come with sentences."""
    # Digits are masked first: build ids, server names and timestamps ("GREEN6WEST2.
    # Version: 10/13/2026") differ per request without the page changing.
    mask = lambda t: {re.sub(r"\d+", "#", l) for l in t.splitlines()}
    return [l for l in mask(old_text) ^ mask(new_text) if len(l.split()) > 3]


def field_diff(old, new):
    old, new = list(old or []), list(new or [])
    if any(f.startswith("*:") for f in old + new):
        # Generated names on either side: only the kinds of fields asked for are comparable.
        old, new = [f.split(":")[-1] for f in old], [f.split(":")[-1] for f in new]
    old, new = Counter(old), Counter(new)
    if old == new:
        return None
    parts = []
    if new - old:
        parts.append("+" + ", +".join(sorted((new - old).elements())))
    if old - new:
        parts.append("-" + ", -".join(sorted((old - new).elements())))
    return "form fields " + " ".join(parts)


def content_diff(prev, obs, text_changed):
    """Reasons a live page differs from its last live observation."""
    reasons = []
    if obs.get("final_url") != prev.get("final_url"):
        reasons.append(f"now lands on {obs.get('final_url')}")
    if text_changed:
        reasons.append(f"page text changed ({text_changed} lines)")
    f = field_diff(prev.get("fields"), obs.get("fields"))
    if f:
        reasons.append(f)
    if obs.get("captcha") != prev.get("captcha"):
        reasons.append("CAPTCHA " + ("appeared" if obs.get("captcha") else "disappeared"))
    if obs.get("vendors") != prev.get("vendors"):
        reasons.append(f"request-portal vendor {prev.get('vendors') or '[]'} → {obs.get('vendors') or '[]'}")
    return reasons


def mismatches(obs, broker):
    """Things the page shows that disagree with the authored entry (worth a look, not proof)."""
    out = []
    if obs.get("state") != "live":
        return out
    if obs.get("captcha") and broker.get("captcha") is False:
        out.append("page loads a CAPTCHA but entry says captcha: false")
    if obs.get("home_redirect"):
        out.append("opt-out URL redirects to the homepage")
    elif obs.get("offsite"):
        out.append(f"opt-out URL now lands on another site: {host(obs['final_url'])}")
    return out


def main():
    ap = argparse.ArgumentParser(description="Detect changes to broker opt-out pages.")
    ap.add_argument("--only", nargs="*", help="broker ids to check (default: all)")
    ap.add_argument("--report", help="write a markdown change report here")
    ap.add_argument("--events", help="write one JSON event per broker needing attention (for issue filing)")
    ap.add_argument("--workers", type=int, default=12)
    args = ap.parse_args()

    brokers = load_brokers(set(args.only) if args.only else None)
    prev_all = json.load(open(FP_PATH)) if os.path.exists(FP_PATH) else {"brokers": {}}
    prev_fps = prev_all.get("brokers", {})
    today = datetime.date.today().isoformat()
    os.makedirs(SNAP_DIR, exist_ok=True)

    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        results = list(ex.map(observe, brokers))

    fps = dict(prev_fps)
    changed, flagged, failing = [], [], []
    for broker, (obs, text) in zip(brokers, results):
        bid = broker["id"]
        prev = prev_fps.get(bid)
        snap = os.path.join(SNAP_DIR, f"{bid}.txt")
        if prev is None or prev.get("url") != obs["url"]:
            # New broker, or its opt_out_url was edited: start a fresh baseline silently.
            obs.pop("error", None)
            obs["last_changed"] = today
            fps[bid] = obs
            if text is not None:
                with open(snap, "w", encoding="utf-8") as f:
                    f.write(text)
        elif obs["state"] != "live":
            rec = {k: v for k, v in prev.items() if k not in ("misses", "pending")}
            if obs["state"] == prev.get("state"):
                pass  # still blocked/broken as before
            elif obs["state"] == "unreachable":
                # Network errors never change state on their own; a streak is reported once.
                rec["misses"] = prev.get("misses", 0) + 1
                if rec["misses"] == 3:
                    failing.append((broker, "unreachable for 3 runs in a row"))
            elif prev.get("pending") == obs["state"]:
                # Seen twice in a row: accept. Only "the page is gone" is news; a bot wall
                # appearing just means we can't see the page.
                rec.update(state=obs["state"], status=obs["status"])
                if obs["state"] == "broken":
                    rec["last_changed"] = today
                    changed.append((broker, [f"page now returns HTTP {obs['status']}"]))
            else:
                rec["pending"] = obs["state"]  # bot walls flap between 403 and 404; wait a run
            fps[bid] = rec
            continue
        else:
            # Live: compare against the last live observation, wherever the page went since.
            n_changed = 0
            if text is not None and prev.get("text_hash") and obs["text_hash"] != prev["text_hash"]:
                old_text = open(snap, encoding="utf-8").read() if os.path.exists(snap) else ""
                n_changed = len(significant_lines(old_text, text))
                if not n_changed:
                    obs["text_hash"], obs["text_lines"] = prev["text_hash"], prev.get("text_lines")
            reasons = content_diff(prev, obs, n_changed) if prev.get("text_hash") else []
            if prev.get("state") == "broken":
                reasons.insert(0, "page is back (was broken)")
            obs["last_changed"] = today if reasons else prev.get("last_changed", today)
            fps[bid] = obs
            if text is not None and (n_changed or not os.path.exists(snap) or not prev.get("text_hash")):
                with open(snap, "w", encoding="utf-8") as f:
                    f.write(text)
            if reasons:
                changed.append((broker, reasons))
        obs = fps[bid]
        m = mismatches(obs, broker)
        if m:
            obs["flags"] = m
            # Report a disagreement once, when it first appears, not every week it persists.
            new = [x for x in m if x not in (prev or {}).get("flags", [])]
            if new:
                flagged.append((broker, new))

    # Drop fingerprints for brokers no longer authored (only on a full run).
    if not args.only:
        live_ids = {b["id"] for b in brokers}
        for bid in list(fps):
            if bid not in live_ids:
                del fps[bid]
                snap = os.path.join(SNAP_DIR, f"{bid}.txt")
                if os.path.exists(snap):
                    os.remove(snap)

    os.makedirs(MONITOR_DIR, exist_ok=True)
    with open(FP_PATH, "w", encoding="utf-8") as f:
        json.dump({"brokers": dict(sorted(fps.items()))}, f, indent=1, sort_keys=True, ensure_ascii=False)
        f.write("\n")

    states = Counter(o["state"] for o, _ in results)
    baseline = not prev_fps
    print(f"checked {len(brokers)} pages: {dict(states)}; "
          f"{len(changed)} changed, {len(flagged)} flagged, {len(failing)} failing")
    if args.report:
        write_report(args.report, today, states, changed, flagged, failing, baseline)
    if args.events:
        write_events(args.events, changed, flagged, failing)


EVENT_KINDS = (("changed", "Its opt-out page changed since the last check."),
               ("mismatch", "Its opt-out page disagrees with the entry."),
               ("unreachable", "Its opt-out page has stopped responding."))


def write_events(path, changed, flagged, failing):
    """One event per broker, merging every reason, so the workflow files at most one issue each."""
    by_id = {}
    for (kind, lead), items in zip(EVENT_KINDS, (changed, flagged, failing)):
        for b, reasons in items:
            e = by_id.setdefault(b["id"], {"id": b["id"], "priority": b.get("priority"),
                                            "kinds": [], "lines": []})
            e["kinds"].append(kind)
            e["lines"].append(f"**{lead}**")
            e["lines"] += [f"- {r}" for r in (reasons if isinstance(reasons, list) else [reasons])]
    events = []
    for e in sorted(by_id.values(), key=lambda e: (PRIORITY_ORDER.get(e["priority"], 9), e["id"])):
        b = e["id"]
        body = "\n".join([
            f"The page monitor flagged [`{b}`]({REPO_URL}/blob/main/data/brokers/{b}.md) "
            f"({e['priority']} priority).", "", *e["lines"], "",
            f"Snapshot of the page text: [`monitor/snapshots/{b}.txt`]({REPO_URL}/blob/main/monitor/snapshots/{b}.txt) "
            f"— its history shows exactly what moved.", "",
            "This means **re-verify the entry**, not that it is wrong. If the opt-out still works "
            "as written, close this issue with a note; otherwise open a PR against the entry "
            "and reference this issue."])
        labels = ["page-monitor", "broker-data"]
        if e["priority"] == "crucial":
            labels.append("priority: high")
        if e["kinds"] == ["mismatch"]:
            # "Open the page, is there a CAPTCHA / where does it land?" needs no prior context.
            labels.append("good first issue")
        events.append({"id": b, "title": f"Page monitor: {b}", "body": body, "labels": labels})
    with open(path, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=1, ensure_ascii=False)


def write_report(path, today, states, changed, flagged, failing, baseline):
    def key(item):
        b = item[0]
        return (PRIORITY_ORDER.get(b.get("priority"), 9), b["id"])

    def link(b):
        return f"[`{b['id']}`]({REPO_URL}/blob/main/data/brokers/{b['id']}.md) ({b.get('priority')}, {b.get('tier')})"

    lines = [f"## Broker page monitor — {today}", ""]
    lines.append("Checked: " + ", ".join(f"{n} {s}" for s, n in sorted(states.items())))
    lines.append("")
    if baseline:
        lines += ["First run: this PR records the baseline snapshot for every page. "
                  "Nothing to verify yet — later runs report changes against it.", ""]
    lines += ["A changed page means **re-verify the entry**, not that the entry is wrong. "
              "The diff of `monitor/snapshots/` in this PR shows exactly what moved on each page. "
              "Merging this PR accepts the new snapshots as the baseline.", ""]
    for title, items in (("Changed since last run", changed),
                         ("Page newly disagrees with the entry", flagged),
                         ("Repeatedly unreachable or blocked", failing)):
        if not items:
            continue
        lines += [f"### {title} ({len(items)})", ""]
        for b, reasons in sorted(items, key=key):
            r = reasons if isinstance(reasons, list) else [reasons]
            lines.append(f"- {link(b)} — " + "; ".join(r))
        lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
