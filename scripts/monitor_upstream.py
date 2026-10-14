#!/usr/bin/env python3
"""
Snapshot the upstream broker lists this dataset draws on, so their changes show up as git diffs
under monitor/upstream/ instead of having to be re-scraped and re-read by hand.

  ca-registry.tsv  California's official data broker registry (CPPA), one row per registrant,
                   with an `ours` column: authored / backlog / dropped / new. `new` rows are
                   registered brokers this dataset doesn't cover yet.
  badbool.md       Yael Grauer's Big Ass Data Broker Opt-Out List README (CC BY-NC-SA 4.0,
                   the same license as this dataset; see LICENSE-DATA), verbatim.

A source that fails to fetch keeps its previous snapshot. Run by .github/workflows/page-monitor.yml.

MIT, (C) 2026 Transparency Cascade Press.
"""
import csv, io, json, os, re, sys, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import broker_lib as bl

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(HERE, "monitor", "upstream")
CA_URL = "https://cppa.ca.gov/data_broker_registry/registry.csv"
BADBOOL_URL = "https://raw.githubusercontent.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List/master/README.md"
UA = "Mozilla/5.0 (compatible; data-broker-registry upstream monitor; +https://github.com/markramm/data-broker-registry)"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8-sig", "replace")


def domain_of(url):
    d = re.split(r"[;,\s]+", (url or "").strip().lower())[0]  # some rows list several sites
    d = re.sub(r"^[a-z]+://", "", d).split("/")[0].split("?")[0].split(":")[0]
    return d[4:] if d.startswith("www.") else d


def our_roster():
    status = {}
    for d in json.load(open(os.path.join(HERE, "data", "backlog.json"))):
        status[d.lower()] = "backlog"
    for d in bl.load_drop_list():
        status[d] = "dropped"
    for path in bl.iter_broker_files():
        try:
            entry, _ = bl.parse_frontmatter(open(path, encoding="utf-8").read(), path)
        except bl.BrokerFileError:
            continue
        if entry.get("domain"):
            status[domain_of(entry["domain"])] = "authored"
    return status


def ca_registry(roster):
    rows = list(csv.reader(io.StringIO(fetch(CA_URL))))
    header, body = rows[0], rows[1:]
    col = lambda prefix: next(i for i, h in enumerate(header) if h.lower().startswith(prefix))
    i_name, i_dba, i_site = col("data broker name"), col("doing business as"), col("data broker primary website")
    i_email = col("data broker primary contact email")
    i_rights = next(i for i, h in enumerate(header) if "exercise" in h.lower())
    out = []
    for r in body:
        if len(r) <= i_rights or not r[i_name].strip():
            continue
        dom = domain_of(r[i_site])
        clean = lambda s: re.sub(r"\s+", " ", s).strip()
        out.append([dom, roster.get(dom, "new"), clean(r[i_name]), clean(r[i_dba]),
                    clean(r[i_email]), clean(r[i_rights])])
    out.sort(key=lambda x: (x[0], x[2]))
    buf = io.StringIO()
    w = csv.writer(buf, delimiter="\t", lineterminator="\n")
    w.writerow(["domain", "ours", "name", "dba", "email", "rights_url"])
    w.writerows(out)
    return buf.getvalue(), sum(1 for x in out if x[1] == "new"), len(out)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    roster = our_roster()
    try:
        text, new, total = ca_registry(roster)
        open(os.path.join(OUT_DIR, "ca-registry.tsv"), "w", encoding="utf-8").write(text)
        print(f"ca-registry: {total} registrants, {new} not in this dataset")
    except Exception as e:
        print(f"::warning::ca-registry fetch failed, keeping previous snapshot: {e}")
    try:
        open(os.path.join(OUT_DIR, "badbool.md"), "w", encoding="utf-8").write(fetch(BADBOOL_URL))
        print("badbool: ok")
    except Exception as e:
        print(f"::warning::badbool fetch failed, keeping previous snapshot: {e}")


if __name__ == "__main__":
    main()
