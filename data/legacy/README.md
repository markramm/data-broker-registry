# Legacy source data

`data-brokers-watch-source.csv` is the original CSV from [Data Brokers Watch](https://github.com/V4NT-ORG/Data-Broker-Watch)
(GPL-3.0), kept here as a historical/provenance reference only. It is **not** part of the
compiled dataset (`data/brokers.json`) and is not covered by `LICENSE-DATA` — it remains
under DBW's own GPL-3.0 terms.

It was used as one input to `scripts/migrate_to_markdown.py`, the one-time bridge that
generated the initial `data/brokers/*.md` roster. That roster (and everything built from it)
re-derives facts into a new schema and is licensed separately — see `/LICENSE-DATA`.
