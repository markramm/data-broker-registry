#!/usr/bin/env bash
# Single entrypoint for the dataset pipeline: refresh link liveness, then compile.
# Order matters -- check_links.py reads data/brokers/*.md directly (no build dependency),
# and build_brokers.py reads the freshly-written data/link-status.json back in.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

python3 scripts/check_links.py
python3 scripts/build_brokers.py
