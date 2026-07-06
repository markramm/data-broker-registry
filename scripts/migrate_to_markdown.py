#!/usr/bin/env python3
"""
One-time bridge: converts the legacy CSV-derived data/brokers.json (722 entries, tier
crucial/high/tail purely derived from has_link+people_search) into the new authored
markdown-with-frontmatter format under data/brokers/.

Per the rewrite plan, this does NOT attempt to mechanically re-tier all 722 brokers --
most have no opt-out URL, method, or phone at all, and fabricating auto/assisted/guided
judgment calls for them would be false editorial confidence. Instead:

  Tier A (full authoring, TODO placeholders for a human editorial pass):
    every legacy "crucial" or "high" broker (has a working link today) -- these get a
    real .md file with tier/priority/required_fields left as explicit TODO markers for
    a human to fill in, since that's a genuine judgment call this script can't make.

  Tier B (mechanical stub, safe defaults, no human pass needed to be honest):
    legacy "tail" brokers with a phone number and nothing else -- auto-stubbed as
    tier:guided, method:phone, last_verified:null, generic call-first instructions.
    This is mechanical but SAFE because "phone-only, guided, unverified" cannot
    overstate confidence in either direction.

  Tier C (excluded from v1, tracked not discarded):
    everything else (no link, no method, no phone) -- written to data/backlog.json as
    a flat domain list, the post-v1 authoring queue. NOT converted to .md files.

Usage: scripts/migrate_to_markdown.py [--legacy-path PATH] [--enrichment-path PATH]

MIT, (C) 2026 Transparency Cascade Press.
"""
import argparse, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import broker_lib as bl

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_LEGACY_PATH = os.path.join(HERE, "data", "brokers.json")
DEFAULT_ENRICHMENT_PATH = os.path.join(HERE, "data", "brokers-enrichment.json")
OUT_DIR = bl.BROKERS_DIR
BACKLOG_PATH = os.path.join(HERE, "data", "backlog.json")

TODO_TIER = "TODO-tier"
TODO_PRIORITY = "TODO-priority"

CATEGORY_MAP_HINTS = {
    "people": "people_search",
}


PHONE_SHAPE_RE = re.compile(r"^[0-9+()\-. extEXT]+$")


def looks_like_phone(raw):
    raw = (raw or "").strip()
    if not raw:
        return False
    # upstream CSV has scraping artifacts like "Download Search Results" in the phone
    # column for a couple of domains -- require at least a few digits and reject anything
    # that doesn't match the schema's own phone-field shape, so junk doesn't get authored
    # as if it were a real phone number.
    digit_count = sum(1 for c in raw if c.isdigit())
    return digit_count >= 7 and bool(PHONE_SHAPE_RE.match(raw))


def domain_to_id(domain):
    slug = domain.lower().replace(".", "-")
    slug = re.sub(r"[^a-z0-9-]", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def normalize_category(raw_category, people_search):
    if people_search:
        return "people_search"
    return (raw_category or "other").strip().lower().replace(" ", "_") or "other"


def infer_method(legacy):
    if legacy.get("opt_out_url"):
        return "form"
    if legacy.get("opt_out_method", "").strip():
        m = legacy["opt_out_method"].lower()
        if "email" in m:
            return "email"
        if "mail" in m and "email" not in m:
            return "mail"
        return "form"
    if legacy.get("phone", "").strip():
        return "phone"
    return "unsupported"


def build_tier_a_entry(legacy, enrichment_by_domain):
    domain = legacy["domain"]
    enrich = enrichment_by_domain.get(domain, {})
    research_note = enrich.get("research_note", "")
    entry = {
        "id": domain_to_id(domain),
        "name": legacy.get("name") or domain,
        "domain": domain,
        "category": normalize_category(legacy.get("category"), legacy.get("people_search")),
        "people_search": bool(legacy.get("people_search")),
        "tier": TODO_TIER,
        "priority": TODO_PRIORITY,
        "method": infer_method(legacy),
        "opt_out_url": legacy.get("opt_out_url") or None,
        "opt_out_email": None,
        "phone": legacy.get("phone") if looks_like_phone(legacy.get("phone")) else None,
        "captcha": bool(legacy.get("has_captcha")),
        "id_required": False,
        "phone_required": False,
        "charges_fee": False,
        "required_fields": [],
        "readd_days": None,
        "legal_basis": [],
        "last_verified": None,
        "source": legacy.get("source", "data-brokers-watch"),
    }
    if research_note:
        entry["notes"] = f"MIGRATED research_note: {research_note}"
    return entry


def build_tier_b_entry(legacy):
    domain = legacy["domain"]
    phone = legacy.get("phone", "").strip()
    return {
        "id": domain_to_id(domain),
        "name": legacy.get("name") or domain,
        "domain": domain,
        "category": normalize_category(legacy.get("category"), legacy.get("people_search")),
        "people_search": bool(legacy.get("people_search")),
        "tier": "guided",
        "priority": "standard",
        "method": "phone",
        "opt_out_url": None,
        "opt_out_email": None,
        "phone": phone,
        "captcha": False,
        "id_required": False,
        "phone_required": True,
        "charges_fee": False,
        "required_fields": [],
        "readd_days": None,
        "legal_basis": [],
        "last_verified": None,
        "source": legacy.get("source", "data-brokers-watch"),
    }, phone


def body_for_tier_a(entry):
    return (
        f"<!-- TODO: write real step-by-step instructions for {entry['name']}. -->\n"
        f"1. TODO: describe how to opt out of {entry['name']}."
    )


def body_for_tier_b(phone):
    return (
        f"1. Call {phone} and request removal of your information.\n"
        "2. No verified step-by-step procedure exists yet for this broker -- "
        "if you learn one, please contribute it."
    )


def write_broker_file(entry, body):
    path = os.path.join(OUT_DIR, f"{entry['id']}.md")
    frontmatter = bl.render_frontmatter(entry)
    with open(path, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write("\n")
        f.write(body)
        f.write("\n")
    return path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--legacy-path", default=DEFAULT_LEGACY_PATH)
    parser.add_argument("--enrichment-path", default=DEFAULT_ENRICHMENT_PATH)
    args = parser.parse_args()

    legacy = json.load(open(args.legacy_path))
    brokers = legacy["brokers"]

    enrichment_by_domain = {}
    if os.path.exists(args.enrichment_path):
        for e in json.load(open(args.enrichment_path)):
            if e.get("domain"):
                enrichment_by_domain[e["domain"].lower()] = e

    os.makedirs(OUT_DIR, exist_ok=True)

    tier_a_count = 0
    tier_b_count = 0
    backlog = []

    for legacy_broker in brokers:
        legacy_tier = legacy_broker.get("tier")
        if legacy_tier in ("crucial", "high"):
            entry = build_tier_a_entry(legacy_broker, enrichment_by_domain)
            write_broker_file(entry, body_for_tier_a(entry))
            tier_a_count += 1
        elif looks_like_phone(legacy_broker.get("phone")):
            entry, phone = build_tier_b_entry(legacy_broker)
            write_broker_file(entry, body_for_tier_b(phone))
            tier_b_count += 1
        else:
            backlog.append(legacy_broker["domain"])

    json.dump(sorted(backlog), open(BACKLOG_PATH, "w"), indent=1)

    print(f"Tier A (full authoring, TODO placeholders): {tier_a_count} files")
    print(f"Tier B (mechanical phone-only stubs): {tier_b_count} files")
    print(f"Tier C (backlog, not converted): {len(backlog)} domains -> {BACKLOG_PATH}")
    print(f"\nNext: run scripts/validate_broker.py against data/brokers/*.md to see what's")
    print(f"still marked {TODO_TIER}/{TODO_PRIORITY} and needs a real editorial pass.")


if __name__ == "__main__":
    main()
