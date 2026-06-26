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
    if not u.startswith("http"):
        u = "https://" + u
    return u

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
                "has_link": bool(opt_url),                     # one-click opt-out URL
                "has_method": bool(opt_url or method or r.get("Phone Number","").strip()),  # any actionable path
                "source": "data-brokers-watch",
            })

    # merge hand-curated enrichment (verified opt-out links from our research)
    enriched = 0
    if os.path.exists(ENRICH):
        overlay = {e["domain"].lower(): e for e in json.load(open(ENRICH)) if e.get("domain")}
        by_domain = {r["domain"].lower(): r for r in rows if r["domain"]}
        for dom, e in overlay.items():
            if dom in by_domain:
                by_domain[dom].update({k: v for k, v in e.items() if v})
                by_domain[dom]["source"] = "data-brokers-watch + tcp-verified"
                by_domain[dom]["has_link"] = bool(by_domain[dom].get("opt_out_url"))
                by_domain[dom]["has_method"] = bool(by_domain[dom].get("opt_out_url") or by_domain[dom].get("opt_out_method") or by_domain[dom].get("phone"))
                enriched += 1
            else:  # net-new broker we curated
                e["source"] = "tcp-verified"
                e["has_link"] = bool(e.get("opt_out_url"))
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
