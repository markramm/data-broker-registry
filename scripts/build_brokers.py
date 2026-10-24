#!/usr/bin/env python3
"""
Compile data/brokers/*.md (authored, schema-validated broker entries) into data/brokers.json,
plus data/manifest.json (content hash + version, for the frontend's integrity check).

Replaces build_brokers_json.py's CSV-row pipeline: this reads the authored markdown roster
instead of the Data Brokers Watch CSV. See broker.schema.json for the field contract and
scripts/broker_lib.py for the shared parse/validate logic.

Run via scripts/build.sh, which refreshes data/link-status.json first (scripts/check_links.py)
so link_status reflects current liveness before this compiles it in.

MIT, (C) 2026 Transparency Cascade Press.
"""
import hashlib, json, os, sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import broker_lib as bl

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK_STATUS_PATH = os.path.join(HERE, "data", "link-status.json")
BACKLOG_PATH = os.path.join(HERE, "data", "backlog.json")
OUT_PATH = os.path.join(HERE, "data", "brokers.json")
MANIFEST_PATH = os.path.join(HERE, "data", "manifest.json")

SCHEMA_VERSION = "1.0"
HASH_ALGORITHM = "sha256-canonical-v1"

# Fields excluded from the content hash: they change on routine re-verification/rebuild
# passes and should NOT make a rebuild look like tampering. Everything safety-relevant
# (opt_out_url/opt_out_email above all) stays in the hash.
HASH_EXCLUDED_FIELDS = {"last_verified"}
TIER_ORDER = {"crucial": 0, "high": 1, "standard": 2}


def load_link_status():
    if not os.path.exists(LINK_STATUS_PATH):
        return {}
    return json.load(open(LINK_STATUS_PATH))


def load_backlog():
    if not os.path.exists(BACKLOG_PATH):
        return []
    return json.load(open(BACKLOG_PATH))


def merge_link_status(entry, link_status):
    url = entry.get("opt_out_url")
    if isinstance(url, str) and url.startswith("http"):
        entry["link_status"] = link_status.get(url, "unknown")
    else:
        entry["link_status"] = "unknown" if entry.get("opt_out_email") else "unknown"
    return entry


def canonical_for_hash(entries):
    """Deterministic serialization for hashing: sorted keys, volatile fields stripped."""
    cleaned = []
    for e in entries:
        stripped = {k: v for k, v in e.items() if k not in HASH_EXCLUDED_FIELDS}
        cleaned.append(stripped)
    cleaned.sort(key=lambda e: e.get("id", ""))
    # ensure_ascii=False: JS's JSON.stringify emits UTF-8 literally rather than \uXXXX-escaping
    # non-ASCII text (em-dashes, curly quotes, accented names are common in authored prose).
    # The frontend's canonical-hash implementation must byte-for-byte agree with this one, so
    # this must NOT ensure-ascii-escape -- otherwise every entry with non-ASCII text would
    # permanently fail the integrity check.
    return json.dumps(cleaned, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def bump_patch_version(prev_version):
    if not prev_version:
        return "0.1.0"
    parts = prev_version.split(".")
    if len(parts) != 3:
        return "0.1.0"
    major, minor, patch = parts
    return f"{major}.{minor}.{int(patch) + 1}"


def main(check_only=False):
    entries, errors_by_path = bl.load_and_validate_all()

    if errors_by_path:
        print(f"FAILED: {len(errors_by_path)} broker file(s) have errors:", file=sys.stderr)
        for path, errs in errors_by_path.items():
            print(f"\n{path}", file=sys.stderr)
            for err in errs:
                print(f"  - {err}", file=sys.stderr)
        return 1

    link_status = load_link_status()
    for entry in entries:
        merge_link_status(entry, link_status)

    entries.sort(key=lambda e: (TIER_ORDER.get(e.get("priority"), 9), e["name"].lower()))

    backlog = load_backlog()
    authored_count = len(entries)
    backlog_count = len(backlog)

    content_hash = "sha256:" + hashlib.sha256(canonical_for_hash(entries).encode("utf-8")).hexdigest()

    # Only bump when the content changed, so rebuilding an already-built tree is a no-op.
    prev_version, prev_hash = None, None
    if os.path.exists(MANIFEST_PATH):
        prev = json.load(open(MANIFEST_PATH))
        prev_version, prev_hash = prev.get("dataset_version"), prev.get("content_hash")
    if prev_version and prev_hash == content_hash:
        dataset_version = prev_version
    else:
        dataset_version = bump_patch_version(prev_version)

    tier_counts = dict(Counter(e.get("tier") for e in entries))
    priority_counts = dict(Counter(e.get("priority") for e in entries))
    unverified_count = sum(1 for e in entries if e.get("last_verified") is None)

    meta = {
        "schema_version": SCHEMA_VERSION,
        "dataset_version": dataset_version,
        "content_hash": content_hash,
        "attribution": (
            "Broker facts drawn from Data Brokers Watch, Privacy Rights Clearinghouse, and "
            "Yael Grauer's Big Ass Data Broker Opt-Out List (BADBOOL). Verification research, "
            "tiering, and instructions are original work by Transparency Cascade Press. "
            "See LICENSE-DATA for the full attribution and licensing notes."
        ),
        "authored_count": authored_count,
        "backlog_count": backlog_count,
        "total_known": authored_count + backlog_count,
        "unverified_count": unverified_count,
        "tiers": tier_counts,
        "priorities": priority_counts,
    }

    if check_only:
        # Two independent checks: (1) does the COMMITTED data/brokers.json's own _meta.content_hash
        # match what its own "brokers" array actually hashes to right now -- catches direct edits
        # to the compiled artifact that bypassed the build entirely; (2) does a fresh rebuild from
        # data/brokers/*.md agree with what's committed -- catches authored files that changed
        # without anyone rerunning the build.
        if not os.path.exists(OUT_PATH):
            print("no existing data/brokers.json to check against", file=sys.stderr)
            return 1
        committed = json.load(open(OUT_PATH))
        committed_meta = committed.get("_meta", {})
        committed_entries = committed.get("brokers", [])
        committed_self_hash = (
            "sha256:" + hashlib.sha256(canonical_for_hash(committed_entries).encode("utf-8")).hexdigest()
        )
        if committed_meta.get("content_hash") != committed_self_hash:
            print(
                f"FAILED: data/brokers.json was hand-edited without rerunning the build -- its own "
                f"_meta.content_hash ({committed_meta.get('content_hash')}) does not match what its "
                f"'brokers' array actually hashes to ({committed_self_hash}).",
                file=sys.stderr,
            )
            return 1

        if committed_self_hash != content_hash:
            print(
                f"FAILED: a fresh rebuild from data/brokers/*.md ({content_hash}) does not match the "
                f"committed data/brokers.json ({committed_self_hash}) -- authored files changed but "
                f"the build was not rerun, or dataset_version was not bumped.",
                file=sys.stderr,
            )
            return 1

        print("ok: data/brokers.json is internally consistent and matches a fresh rebuild")
        return 0

    for entry in entries:
        entry.pop("instructions_md_rendered", None)

    json.dump({"_meta": meta, "brokers": entries}, open(OUT_PATH, "w"), indent=1)
    json.dump(meta, open(MANIFEST_PATH, "w"), indent=1)

    print(
        f"wrote {OUT_PATH}: {authored_count} authored brokers "
        f"({backlog_count} in backlog, {unverified_count} unverified), "
        f"dataset_version={dataset_version}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(check_only="--check" in sys.argv))
