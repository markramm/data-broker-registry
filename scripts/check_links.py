#!/usr/bin/env python3
"""
Verify the liveness of every broker opt-out URL authored in data/brokers/*.md, and write
data/link-status.json. Re-run periodically — broker opt-out pages churn constantly.

Reads the AUTHORED markdown roster directly (not the compiled data/brokers.json), so this can
run before a first build exists — build_brokers.py then reads this file back in to set each
entry's link_status. Run via scripts/build.sh, which does both in the right order.

Status meanings:
  live        — 2xx, the page loads
  bot-blocked — 403, the SITE IS UP but blocks automated requests. Usable by a real human in a
                browser. (Most major people-search sites do this; do NOT treat as broken.)
  redirect    — 3xx, follow it (curl -L already does; recorded for awareness)
  broken      — 404 / connection-failed / 400. Do NOT present as a working one-click link.

MIT, (C) 2026 Transparency Cascade Press.
"""
import json, os, subprocess, sys, concurrent.futures as cf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import broker_lib as bl

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "data", "link-status.json")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Safari/537.36"

def collect_urls():
    urls = set()
    for path in bl.iter_broker_files():
        text = open(path, encoding="utf-8").read()
        try:
            entry, _ = bl.parse_frontmatter(text, path)
        except bl.BrokerFileError:
            continue  # a malformed file is validate_broker.py's job to catch, not ours
        u = (entry.get("opt_out_url") or "").strip()
        if u.startswith("http"):
            urls.add(u)
    return sorted(urls)

def check(url):
    try:
        out = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L", "--max-time", "15", "-A", UA, url],
            capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception:
        out = "000"
    if out.startswith("2"): s = "live"
    elif out == "403": s = "bot-blocked"
    elif out.startswith("3"): s = "redirect"
    else: s = "broken"
    return url, s

def main():
    urls = collect_urls()
    status = {}
    with cf.ThreadPoolExecutor(max_workers=10) as ex:
        for url, s in ex.map(check, urls):
            status[url] = s
    json.dump(status, open(OUT, "w"), indent=0)
    from collections import Counter
    print(f"checked {len(urls)} urls → {OUT}: {dict(Counter(status.values()))}")

if __name__ == "__main__":
    main()
