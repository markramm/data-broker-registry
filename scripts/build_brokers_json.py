#!/usr/bin/env python3
"""
Convert the Data Brokers Watch CSV (GPL-3.0, github.com/V4NT-ORG/Data-Broker-Watch)
into brokers.json for the Make Yourself Expensive tool.

We embed all ~770 as the ROSTER, flag which have a usable opt-out link/method,
and tag categories. High-impact people-search brokers can be hand-enriched in
brokers-enrichment.json (verified opt-out links from our own research) — that
overlay is merged on top so the working-link coverage isn't limited to the CSV's.

License: this tool is GPL-3.0; the DBW data is GPL-3.0; combining them is GPL's intent.
"""
import csv, json, os, re, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(HERE, "data", "data-brokers-watch-source.csv")
ENRICH = os.path.join(HERE, "data", "brokers-enrichment.json")
DROP = os.path.join(HERE, "data", "brokers-drop.json")
OUT = os.path.join(HERE, "data", "brokers.json")

# People-search / address-resellers are the highest-impact for personal safety
# (the Hortman-notebook category). Tag them so the tool can surface them first.
PEOPLE_SEARCH_HINTS = ("people", "search", "directory", "background", "lookup",
                       "phone", "address", "public record", "reverse")

def clean_name(s):
    s = (s or "").strip().strip('"').strip()
    # title-case all-lower or fix stray spacing; leave proper names alone
    return re.sub(r"\s+", " ", s)

def norm_url(u):
    u = (u or "").strip().strip('"').strip()
    if not u:
        return ""
    if u.lower() in ("n/a", "none", "unclear", "-", "see comments"):
        return ""
    # DBW packs multiple URLs in one field as "url1 , url2" or "url1 ; ccpa: url2" — take the first.
    u = re.split(r"\s*[;,]\s*|\s+ccpa:\s*|\s{2,}", u)[0].strip()
    if not u.startswith("http"):
        u = "https://" + u
    return u

# liveness map from scripts/check_links.py (verified 2026-06-26). live/bot-blocked = usable by a
# human; broken (404/dead) = do NOT present as a working one-click link.
import json as _json
_LS_PATH = os.path.join(HERE, "data", "link-status.json")
LINK_STATUS = _json.load(open(_LS_PATH)) if os.path.exists(_LS_PATH) else {}
DROP_DOMS = set(_json.load(open(DROP))) if os.path.exists(DROP) else set()
def url_ok(u):
    """Is this URL usable by a real human? (live or bot-blocked, NOT broken)"""
    if not u:
        return False
    return LINK_STATUS.get(u, "unknown") in ("live", "bot-blocked", "redirect", "unknown")

def has_optout(row):
    """Does this broker have an actionable opt-out path?"""
    return bool(norm_url(row.get("Opt Out URL")) or
                (row.get("Opt-Out Method", "").strip() and
                 row.get("Opt-Out Method", "").strip().lower() not in ("unclear", "n/a", "")))

def is_people_search(cats):
    c = (cats or "").lower()
    return any(h in c for h in PEOPLE_SEARCH_HINTS)

def main():
    rows = []
    with open(SRC, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            name = clean_name(r.get("Name") or r.get("Domain") or "")
            domain = clean_name(r.get("Domain") or "").lower()
            if not name and not domain:
                continue
            # skip dead brokers
            if (r.get("Health") or "").strip().lower() == "dead":
                continue
            if domain in DROP_DOMS:  # researched dead / no-opt-out — remove from actionable register
                continue
            cats = (r.get("Categories") or "").strip()
            opt_url = norm_url(r.get("Opt Out URL"))
            method = (r.get("Opt-Out Method") or "").strip()
            method = "" if method.lower() in ("unclear", "n/a") else method
            rows.append({
                "name": name or domain,
                "domain": domain,
                "category": cats,
                "people_search": is_people_search(cats),
                "opt_out_url": opt_url,
                "opt_out_method": method,
                "phone": (r.get("Phone Number") or "").strip(),
                "needs_form": (r.get("Form") or "").strip().lower() in ("yes", "true", "1"),
                "has_captcha": (r.get("Capcha") or "").strip().lower() in ("yes", "true", "1"),
                "link_status": LINK_STATUS.get(opt_url, "unknown") if opt_url else "none",
                # has_link = a usable one-click URL (live/bot-blocked, NOT a verified-broken one)
                "has_link": bool(opt_url) and url_ok(opt_url),
                "has_method": bool((opt_url and url_ok(opt_url)) or method or r.get("Phone Number","").strip()),
                "source": "data-brokers-watch",
            })

    # merge hand-curated enrichment (verified opt-out links from our research)
    enriched = 0
    if os.path.exists(ENRICH):
        overlay = {e["domain"].lower(): e for e in json.load(open(ENRICH)) if e.get("domain")}
        by_domain = {r["domain"].lower(): r for r in rows if r["domain"]}
        for dom, e in overlay.items():
            # honest status: trust the URL as one-click only if the researcher VERIFIED it
            # (fetched the page) OR curl confirms it live/bot-blocked. A "likely" URL that also
            # fails a curl check is shown as a manual/unconfirmed link, not a silent one-click.
            def enriched_status(e):
                u = e.get("opt_out_url", "")
                if not u:
                    return "none", False
                live = LINK_STATUS.get(u) in ("live", "bot-blocked", "redirect")
                conf = e.get("research_confidence", "verified")
                if conf == "verified" or live:
                    return "tcp-verified", True          # safe to present as one-click
                return "tcp-unconfirmed", False          # likely but unverified — manual, with caveat
            if dom in by_domain:
                by_domain[dom].update({k: v for k, v in e.items() if v})
                st, ok = enriched_status(e)
                by_domain[dom]["source"] = "data-brokers-watch + tcp-verified"
                by_domain[dom]["link_status"] = st
                by_domain[dom]["has_link"] = ok
                by_domain[dom]["has_method"] = bool(by_domain[dom].get("opt_out_url") or by_domain[dom].get("opt_out_method") or by_domain[dom].get("phone"))
                enriched += 1
            else:  # net-new broker we curated
                st, ok = enriched_status(e)
                e["source"] = "tcp-verified"
                e["link_status"] = st
                e["has_link"] = ok
                e["has_method"] = bool(e.get("opt_out_url") or e.get("opt_out_method") or e.get("phone"))
                rows.append(e)
                enriched += 1

    # sort: people-search-with-working-link first (highest impact, actionable), then the rest
    rows.sort(key=lambda r: (not (r["people_search"] and r["has_link"]),
                             not r["has_link"], not r["has_method"], r["name"].lower()))

    meta = {
        "_meta": {
            "source": "Data Brokers Watch (github.com/V4NT-ORG/Data-Broker-Watch), GPL-3.0",
            "tool_license": "GPL-3.0",
            "attribution": "Broker roster from Data Brokers Watch / YourDigitalRights.org (GPL-3.0). "
                           "Opt-out links for high-impact brokers verified by Transparency Cascade Press.",
            "total_brokers": len(rows),
            "with_optout_link": sum(1 for r in rows if r["has_link"]),
            "with_any_method": sum(1 for r in rows if r["has_method"]),
            "people_search_actionable": sum(1 for r in rows if r["people_search"] and r["has_link"]),
            "enriched_by_tcp": enriched,
        },
        "brokers": rows,
    }
    json.dump(meta, open(OUT, "w"), indent=1)
    print(f"wrote {OUT}: {len(rows)} brokers, {meta['_meta']['with_optout_link']} with opt-out links, "
          f"{enriched} TCP-enriched")

if __name__ == "__main__":
    main()
