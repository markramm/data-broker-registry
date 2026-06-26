# Make Yourself Expensive

A free, no-account, no-tracking, **open-source (GPL-3.0)** tool that walks you through getting your
data out of the data-broker economy — by hand, the way the [Consumer Reports study found beats every
paid service](https://transparencycascade.org/resources/data-footprint/).

Built by [Transparency Cascade Press](https://transparencycascade.org). Nothing you do here leaves
your browser. There is no server, no account, and no analytics on your actions. We make no money from
it and there's nothing to sell — which is the point. A reader-protection tool is only trustworthy if
it can't be bought out from under you. (The free app we used to recommend, Permission Slip, was handed
to a paid service in May 2026. This one is GPL-3.0; it stays free and forkable forever.)

## Data
- **Bundled:** broker roster from [Data Brokers Watch](https://github.com/V4NT-ORG/Data-Broker-Watch)
  (GPL-3.0), plus opt-out links for high-impact brokers verified by us (`data/brokers-enrichment.json`).
- **Optional (link-out, not bundled):** [Yael Grauer's Big Ass Data Broker Opt-Out List](https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List)
  (CC BY-NC-SA — link-only unless separately permitted), and California's free state [DROP tool](https://privacy.ca.gov/).

## Build
`python3 scripts/build_brokers_json.py` regenerates `data/brokers.json` from the CSV + enrichment overlay.

## License
GPL-3.0. See `LICENSE`.
