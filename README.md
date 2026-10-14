# data-broker-registry

An open, versioned, schema-validated registry of data brokers and how to opt out of each
one — the facts, the editorial judgment (how automatable is this opt-out? how urgent?), and
the build pipeline that compiles them into a single artifact. This is a **dataset repo**, not
an app: it has no UI of its own on purpose, so it can be consumed by more than one frontend,
run locally, or forked independently.

The reference frontend that consumes this dataset is
[Make Yourself Expensive](https://github.com/markramm/make-yourself-expensive), built by
[Transparency Cascade Press](https://transparencycascade.org) — a free, no-account,
no-server tool that walks a reader through opting out of every broker in here by hand, the
way the [Consumer Reports study found beats every paid service](https://transparencycascade.org/resources/data-footprint/).
Nothing about this dataset depends on that frontend, though; anyone is welcome to build a
different one against the same `data/brokers.json` artifact.

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

A daily GitHub Action (`.github/workflows/page-monitor.yml`) runs `scripts/monitor_pages.py`,
which fetches every opt-out page, keeps a text snapshot of each under `monitor/snapshots/`, and
files one `page-monitor` issue per broker whose page changed (text, form fields, CAPTCHA,
redirects) or disagrees with its entry. Those issues are the re-verification queue: a changed page
means "look again", never "the entry is wrong". It never edits `data/`.

To validate a single file while authoring (e.g. as a pre-commit check):

```
python3 scripts/validate_broker.py data/brokers/some-broker.md
```

## Frontends

This repo has no UI of its own. [Make Yourself Expensive](https://github.com/markramm/make-yourself-expensive)
is the reference frontend (on-device profile, tiered opt-out actions, dataset-integrity
checking against the `content_hash` this repo's build emits) — but any tool can consume the
compiled `data/brokers.json` artifact the same way it does. A second or third frontend is
exactly as welcome as the first.

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
