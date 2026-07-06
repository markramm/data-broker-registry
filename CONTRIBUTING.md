# Contributing

There are two very different kinds of contribution here: **adding/correcting broker data**
(no code required) and **working on the app or build pipeline** (Python/JS). Most
contributions are the first kind.

## Adding or correcting a broker entry

Each broker is one markdown file under `data/brokers/`, named after its domain with dots
replaced by hyphens (`spokeo.com` -> `data/brokers/spokeo-com.md`). The file has YAML-ish
frontmatter matching `broker.schema.json`, followed by numbered step-by-step instructions.

Read `broker.schema.json` for the authoritative field list. A real example, trimmed:

```markdown
---
id: spokeo-com
name: Spokeo
domain: spokeo.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.spokeo.com/optout"
captcha: true
required_fields: [listing_url, email]
legal_basis: [ccpa]
last_verified: null
source: "data-brokers-watch + tcp-verified"
notes: "Explain how you determined this -- what you fetched, what you couldn't, and why."
---

1. Search your name on spokeo.com and copy your profile's URL.
2. Go to https://www.spokeo.com/optout and paste the URL and your email.
3. Solve the CAPTCHA and submit.
4. Confirm via the email Spokeo sends you.
```

### The two fields that matter most

- **`tier`** (`auto` | `assisted` | `guided`) is about how much a tool *could* automate --
  not how the broker is categorized. `auto` = the opt-out is a plain email (no login, no
  form). `assisted` = a straightforward web form with no CAPTCHA/ID requirement. `guided` =
  CAPTCHA-gated, ID-upload-required, phone-only, or otherwise needs a human doing manual
  steps. When in doubt between `assisted` and `guided`, pick `guided` -- overstating
  friction wastes a user's time; understating it breaks their trust in the badge.
- **`priority`** (`crucial` | `high` | `standard`) is about impact, independent of tier.
  `crucial` is reserved for people-search / home-address-reseller sites -- the ones with
  real personal-safety stakes (stalking, doxxing). `high` is everything else with a real,
  working opt-out. `standard` covers lower-impact or B2B-only brokers.

### The rule that matters most: never put PII in a URL

`opt_out_url` must be exactly the broker's own opt-out page -- never append a query string
built from anyone's name, email, address, or anything else. History, referrer headers, and
server logs all leak query-string PII. `scripts/broker_lib.py`'s build-time lint will reject
an `opt_out_url` containing `email=`, `ssn=`, `name=`, `dob=`, or `address=` in the query
string, but don't rely on the lint catching everything -- treat this as a hard rule, not a
suggestion.

### If you can't confirm the process yourself

- Set `last_verified: null` rather than guessing a date. `null` means "not confirmed by a
  human against the broker's own page" and the app badges these visibly -- that's the
  point, not a failure state.
- If you don't have a confirmed URL/email yet, use the placeholder pattern
  `<verify: what needs to be checked>` instead of leaving the field blank or guessing.
  `last_verified` must stay `null` whenever a field is a placeholder.
- Write down in `notes` what you actually did (fetched the page and it matched; fetched it
  and it was blocked; corroborated from third-party removal guides; etc.) so the next
  person doesn't have to redo your research from scratch.

### Validating before you open a PR

```sh
python3 scripts/validate_broker.py data/brokers/your-new-file.md
```

This checks your file against the schema and the cross-field rules (placeholder-implies-null,
`tier: auto` requires a real `opt_out_email`, no PII in URLs) without needing to touch
anything else. CI runs the same check across every file in the repo, plus a full rebuild, on
every PR that touches `data/` or `scripts/`.

### If a broker has moved, died, or should be excluded

- **Dead/no real opt-out exists**: add the domain to `data/brokers-drop.json` instead of
  deleting or leaving a broken entry.
- **Not yet researched**: it's probably already in `data/backlog.json` -- see
  `_meta.backlog_count` in the compiled dataset. Promoting a backlog domain to a real entry
  is one of the most useful contributions there is; there's no need to ask permission first.

## Working on the build pipeline or app code

```sh
scripts/build.sh              # full pipeline: refresh link liveness, then compile
python3 scripts/build_brokers.py --check   # verify data/brokers.json wasn't hand-edited
python3 scripts/check_semver_bump.py HEAD  # confirm dataset_version was bumped if content changed
```

`scripts/build_brokers.py` is the compiler (glob `data/brokers/*.md` -> validate -> merge in
link liveness -> hash -> write `data/brokers.json` + `data/manifest.json`).
`scripts/broker_lib.py` holds the shared frontmatter-parsing/validation logic both the
compiler and `validate_broker.py` use -- if you're fixing a validation bug, it almost
certainly belongs there, not duplicated in both call sites.

If your change alters `data/brokers.json`'s content, always run `scripts/build.sh` and
commit the regenerated `data/brokers.json` + `data/manifest.json` together with your source
change -- CI rejects a PR where the compiled artifact doesn't match a fresh rebuild.

## Licensing your contribution

Broker research and instructions you write are contributed under this dataset's license,
CC BY-NC-SA 4.0 (see `LICENSE-DATA`). App/build code is MIT (see `LICENSE`). You don't need
to do anything special to comply with this -- just don't paste in content you don't have
the right to relicense (e.g. someone else's removal-guide prose verbatim; write your own
summary of what you found instead).
