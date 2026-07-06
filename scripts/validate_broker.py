#!/usr/bin/env python3
"""
Validate one or more data/brokers/*.md files against broker.schema.json. Fast, single-file
checks -- wired as a pre-commit hook on changed files. For full-repo cross-file checks
(duplicate id/domain across the whole roster), build_brokers.py's --check mode runs this
same logic over every file.

Usage: scripts/validate_broker.py data/brokers/spokeo-com.md [more files...]

MIT, (C) 2026 Transparency Cascade Press.
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import broker_lib as bl


def main():
    paths = sys.argv[1:]
    if not paths:
        print("usage: validate_broker.py <file.md> [file.md ...]", file=sys.stderr)
        return 2

    schema = bl.load_schema()
    failed = False

    for path in paths:
        if not path.endswith(".md"):
            continue
        try:
            text = open(path, encoding="utf-8").read()
            entry, _ = bl.parse_frontmatter(text, path)
        except bl.BrokerFileError as e:
            print(f"FAIL {path}")
            for err in e.errors:
                print(f"  - {err}")
            failed = True
            continue

        fname_id = os.path.splitext(os.path.basename(path))[0]
        errs = bl.validate_entry(entry, schema)
        if entry.get("id") and entry["id"] != fname_id:
            errs.append(f"frontmatter id {entry['id']!r} does not match filename-derived id {fname_id!r}")

        if errs:
            print(f"FAIL {path}")
            for err in errs:
                print(f"  - {err}")
            failed = True
        else:
            print(f"ok   {path}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
