# Make Yourself Expensive

A free, no-account, no-tracking, **open-source** tool that walks you through getting your
data out of the data-broker economy — by hand, the way the [Consumer Reports study found beats every
paid service](https://transparencycascade.org/resources/data-footprint/).

Built by [Transparency Cascade Press](https://transparencycascade.org). Nothing you do here leaves
your browser. There is no server, no account, and no analytics on your actions. We make no money from
it and there's nothing to sell — which is the point. A reader-protection tool is only trustworthy if
it can't be bought out from under you. (The free app we used to recommend, Permission Slip, was handed
to a paid service in May 2026. This one is open source; it stays free and forkable forever.)

## Data

Each broker is authored as a markdown file with YAML frontmatter under `data/brokers/`, validated
against `broker.schema.json`, and compiled into `data/brokers.json` by `scripts/build_brokers.py`.
Every entry carries an authored `tier` (`auto`/`assisted`/`guided` — how much the tool can automate)
and `priority` (`crucial`/`high`/`standard` — impact), plus a `last_verified` date: `null` means a
human hasn't yet confirmed the routing against the broker's own page, and the app badges those
entries as unverified.

Sources this dataset draws on and credits:
- [Data Brokers Watch](https://github.com/V4NT-ORG/Data-Broker-Watch) — initial roster baseline.
- [Privacy Rights Clearinghouse](https://privacyrights.org) — data broker registry.
- [Yael Grauer's Big Ass Data Broker Opt-Out List (BADBOOL)](https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List).
- Transparency Cascade Press's own verification research, tiering, and instructions.
- California's free state [DROP tool](https://privacy.ca.gov/) (linked, not bundled).

Brokers not yet given a full editorial pass are tracked in `data/backlog.json` rather than silently
dropped or guessed at — `_meta.authored_count` / `backlog_count` / `total_known` in the compiled
dataset show real coverage.

## Build

```
scripts/build.sh
```

runs the full pipeline in order: `scripts/check_links.py` (refreshes `data/link-status.json`
liveness cache by reading URLs straight from `data/brokers/*.md`) then `scripts/build_brokers.py`
(validates every broker file against `broker.schema.json`, merges in liveness, computes a content
hash, and writes `data/brokers.json` + `data/manifest.json`).

To validate a single file while authoring (e.g. as a pre-commit check):

```
python3 scripts/validate_broker.py data/brokers/some-broker.md
```

## Frontends

This repo is the dataset — the facts, the schema, and the build pipeline that compiles them.
The static site in `index.html`/`app.js` is one thin frontend for it. A second, more complete
frontend ("Protect": on-device profile, tiered opt-out actions, dataset-integrity checking)
lives in a separate repo and consumes the same compiled `data/brokers.json` artifact. Nothing
about the dataset depends on either frontend; a third frontend is exactly as welcome as the
first two.

## Contributing

See `CONTRIBUTING.md` — most contributions are adding or correcting a broker entry, which
doesn't require touching any code.

## License

This repository uses two licenses, on purpose — a dataset and the software that reads it are
different things:

- **App code** (scripts, build tooling): MIT. See `LICENSE`.
- **Broker dataset** (`data/brokers/`, compiled `data/brokers.json`, `broker.schema.json`):
  CC BY-NC-SA 4.0, crediting Privacy Rights Clearinghouse, Yael Grauer/BADBOOL, and Data Brokers
  Watch. See `LICENSE-DATA` for the full attribution and scope notes.
