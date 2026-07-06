#!/usr/bin/env python3
"""
CI check: if data/brokers.json's content changed vs. the base ref, _meta.dataset_version must
have incremented (per semver, any component going up is fine -- this just rejects "changed
content, same version string").

Usage: scripts/check_semver_bump.py [base-ref]  (default base-ref: origin/main)

MIT, (C) 2026 Transparency Cascade Press.
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BROKERS_PATH = os.path.join(HERE, "data", "brokers.json")


def parse_version(v):
    parts = v.split(".")
    if len(parts) != 3:
        return None
    try:
        return tuple(int(p) for p in parts)
    except ValueError:
        return None


def git_show(ref, path):
    try:
        out = subprocess.run(
            ["git", "show", f"{ref}:{path}"], capture_output=True, text=True, cwd=HERE, check=True
        )
        return json.loads(out.stdout)
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        return None


def main():
    base_ref = sys.argv[1] if len(sys.argv) > 1 else "origin/main"

    current = json.load(open(BROKERS_PATH))
    base = git_show(base_ref, "data/brokers.json")

    if base is None:
        print(f"no data/brokers.json found at {base_ref} -- nothing to compare, treating as new file, ok")
        return 0

    base_hash = base.get("_meta", {}).get("content_hash")
    current_hash = current.get("_meta", {}).get("content_hash")

    if base_hash == current_hash:
        print("content_hash unchanged -- no version bump required")
        return 0

    base_version = parse_version(base.get("_meta", {}).get("dataset_version", ""))
    current_version = parse_version(current.get("_meta", {}).get("dataset_version", ""))

    if current_version is None:
        print(f"FAILED: current dataset_version is not valid semver: {current.get('_meta', {}).get('dataset_version')!r}", file=sys.stderr)
        return 1

    if base_version is not None and current_version <= base_version:
        print(
            f"FAILED: data/brokers.json content changed (hash {base_hash} -> {current_hash}) but "
            f"dataset_version did not increase ({base.get('_meta', {}).get('dataset_version')} -> "
            f"{current.get('_meta', {}).get('dataset_version')}). Re-run scripts/build.sh.",
            file=sys.stderr,
        )
        return 1

    print(f"ok: dataset_version bumped ({base.get('_meta', {}).get('dataset_version')} -> {current.get('_meta', {}).get('dataset_version')})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
