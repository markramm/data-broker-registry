# Design: opt-out processes and automation hints

Status: **proposal** (2026-10-14). Nothing here is implemented yet.

## Why

Today an entry says *where* to opt out (`method`, `opt_out_url`, `opt_out_email`) and tells a
person *how* in prose steps. A desktop tool that sends email, waits for confirmations, and
re-checks listings weeks later needs more: what happens in what order, who acts at each point,
what ends each stage, and how long to wait before following up or escalating.

The data splits into three layers, each with a different audience and a different rate of change:

| Layer | Where | Who edits it | Changes when | Versioned by |
|---|---|---|---|---|
| **Facts** (exists) | `data/brokers/<id>.md` frontmatter | anyone | the broker moves its opt-out | `dataset_version` |
| **Process** (new) | same file, new flat fields | anyone | the broker changes its procedure (rare) | `dataset_version` |
| **Automation** (new) | `automation/<id>.json` | people who write browser automation | a form's markup changes (often) | `automation_version` |

Facts and process stay in one file, editable by hand, and every opt-out tool can use them.
Automation is optional, more technical, and breaks more often, so it has its own directory,
version, and staleness tracking. A tool that only guides people by hand can ignore it entirely.

**Non-goals:** the user's state, meaning which requests they've sent, when, and what came back.
That lives in each tool. The dataset describes the process, and the tool tracks one person's
progress through it. Nothing in this repo ever holds personal data.

## Layer 2: process

### New frontmatter fields (all flat, so the existing parser handles them)

```yaml
process: [find_listing, submit_form, confirm_email, recheck_listing]
per_listing: true            # repeat everything after find_listing once per profile found
processing_days: 3           # broker's stated time to act after a complete request; null = unknown
confirm_window_hours: 72     # how long a confirmation link stays valid; null = unknown
email_template: null         # override the default template (see Templates); usually null
```

`process` is an **ordered list of stage names** from a fixed vocabulary. The numbered prose
steps stay as they are: they're what a person reads. `process` is what a tool's state machine
runs. The validator checks that the two agree in substance (see Validation).

### Stage vocabulary

Defined once in `data/stages.json` (shipped with the dataset), so tools read the meaning of each
stage instead of hard-coding it:

| Stage | Who acts | Inputs | Done when | Default timeout |
|---|---|---|---|---|
| `find_listing` | user (tool may assist) | name, location | user confirms 0..n listings are theirs; yields `listing_url`s | — |
| `submit_form` | user / tool | `required_fields` | broker's form accepts the submission | — |
| `send_email` | user / tool | template + `required_fields` | message sent to `opt_out_email` | — |
| `call_phone` | user | `phone` | user records the call happened | — |
| `mail_letter` | user | template, postal address | user records mailing | — |
| `create_account` | user | email (+ password the *user* keeps) | account exists | — |
| `confirm_email` | user / tool | — | user clicks the broker's emailed link | `confirm_window_hours` or 72h |
| `confirm_sms` | user | phone | user enters the code | 1h |
| `verify_identity` | user | ID / questions | broker accepts identity | legal deadline |
| `await_response` | broker | — | broker replies (accepted / denied / needs more) | legal deadline |
| `recheck_listing` | user / tool | `listing_url`s | listing no longer resolves | `processing_days` or 7 |

The vocabulary is closed. A new stage takes a PR to `stages.json` plus a schema change, so
tools can rely on knowing every stage they'll meet. Anything truly unusual goes in the prose
steps, with the nearest stage in `process`.

Stages that collect sensitive inputs (`verify_identity`, and any stage whose broker requires
`dob`, `ssn` or `gov_id`) are marked `sensitive: true` in `stages.json`. Tools must ask
explicitly before sending that data. The dataset already flags these with `id_required`; the
flag just becomes enforceable.

### Legal deadlines and escalation (`data/legal.json`)

Follow-up and escalation are mostly the same for every broker under a given law, so they're
per law, not per broker:

```json
{
  "ccpa": {
    "acknowledge_days": 10,
    "delete_days": 45, "delete_extension_days": 45,
    "opt_out_business_days": 15,
    "regulator": {"name": "California Privacy Protection Agency",
                  "complaint_url": "https://cppa.ca.gov/webapplications/complaint"},
    "templates": {"request": "ccpa-request", "followup": "ccpa-followup", "complaint": "ccpa-complaint"}
  }
}
```

A tool computes `await_response`'s deadline from the entry's `legal_basis`. When the deadline
passes it offers the follow-up template, and after that the regulator complaint. The numbers
come from the statutes and regulations, need a citation in the file, and are checked by a human
like everything else. The figures above are placeholders until someone verifies them.

### Templates (`data/templates/<key>.md`)

These are the request letters a tool sends on the user's behalf. The frontmatter holds `key`,
`legal_basis`, `kind` (request / followup / complaint) and `subject`. The body has `{{placeholders}}`.

```markdown
---
key: ccpa-request
legal_basis: ccpa
kind: request
subject: "CCPA request to delete and to opt out of sale/sharing"
---
To {{broker_name}}:

Under the California Consumer Privacy Act I request that you (1) delete the personal
information you hold about me and (2) stop selling or sharing it...

{{identifying_fields}}
```

`{{identifying_fields}}` expands to **only** the broker's `required_fields`, so data
minimization is enforced by the data itself, not by each tool remembering to do it. An entry's
`email_template` overrides the default only when a broker needs specific wording.

### Profile-field vocabulary (`data/profile-fields.json`)

`required_fields` stays coarse for people (`full_name`, `address`). Placeholders and automation
need finer fields, so this file maps each coarse field to fine ones:
`full_name → first_name, middle_name, last_name`;
`address → street, city, state, zip, prior_addresses`.
It also covers `email`, `phone`, `dob`, `listing_url` and `aliases`. Templates and automation may
only use placeholders that come from the broker's `required_fields`.

### Validation (added to `broker_lib._cross_field_checks`)

- Every `process` value is in `stages.json`.
- `method` agrees with the stages: `form → submit_form`, `email → send_email`,
  `phone → call_phone`, `mail → mail_letter`, `portal → create_account or submit_form`.
- `listing_url` in `required_fields` ⇔ `find_listing` in `process`. `per_listing: true`
  requires `find_listing`.
- `phone_required` ⇔ `call_phone`. `id_required` ⇔ `verify_identity`.
- `verification` (today a free-text field with nine spellings for four ideas) is
  **deprecated**. Its meaning moves into stages (`email_confirm → confirm_email`,
  `sms_confirm → confirm_sms`, `id_upload / identity_* / id_verify → verify_identity`).
  The build keeps emitting it, derived from the process, for one minor version.

### Brand families (issue #4)

This fits the open broker-family proposal without new stages. An entry whose opt-out is handled
by another entry gets `covered_by: intelius-com` and **no** `process`. A tool marks it done
when the covering entry's process completes, and never sends a second request that would be
rejected as a duplicate. The field name is #4's to decide; this design only needs it to exist.

### Examples

Spokeo: a form per profile, a confirmation link, then a re-check.
```yaml
method: form
required_fields: [listing_url, email]
process: [find_listing, submit_form, confirm_email, recheck_listing]
per_listing: true
processing_days: 3
```

180byTwo: an email request under CCPA, then wait for a reply.
```yaml
method: email
legal_basis: [ccpa]
process: [send_email, await_response]
```

A broker that demands a phone call and an ID:
```yaml
method: phone
phone_required: true
id_required: true
process: [call_phone, verify_identity, await_response]
```

### Migration

`scripts/derive_process.py` writes a first `process` into every entry from what's already there:
- `method` gives the action stage.
- `listing_url` in `required_fields` adds `find_listing` and `recheck_listing`.
- `verification` gives the confirm or verify stage.
- `phone_required` and `id_required` add their stages.
- Anything with a `legal_basis` and no confirmation stage gets `await_response`.

The derived processes land in one PR (about 490 files, mechanical, easy to review by
spot-check). Until a human confirms an entry's process, the compiled output carries
`process_source: "derived"` for it, the same way `last_verified: null` works today. A
confirmation is recorded the same way a verification is.

This is an additive schema change, so `schema_version` goes 1.0 → 1.1 and
`check_semver_bump.py` should require a minor version bump.

## Layer 3: automation

### Layout and versioning

```
automation/
  automation.schema.json
  <broker-id>.json          one per broker that has any automation
  manifest.json             automation_version, content_hash, requires_schema: "1.1"
```

`scripts/build_automation.py` validates and compiles these into `automation/automation.json`.
It runs as a separate build with a separate version and hash. A broker can be in the dataset
with no automation file; most will be for a long time.

### Shape

Automation is keyed by **stage**, so it attaches to the process instead of replacing it:

```json
{
  "broker": "spokeo-com",
  "hosts": ["www.spokeo.com"],
  "authored_against": {
    "opt_out_url": "https://www.spokeo.com/optout",
    "fields": ["*:email", "*:text"],
    "date": "2026-10-20"
  },
  "last_tested": null,
  "stages": {
    "find_listing": {
      "search_url": "https://www.spokeo.com/{{first_name}}-{{last_name}}/{{state}}",
      "result": {"item": {"css": ".result-card"}, "link": {"css": "a.profile-link"},
                 "show": ["name", "age", "locations"]}
    },
    "submit_form": {
      "url": "https://www.spokeo.com/optout",
      "actions": [
        {"fill": {"label": "Listing URL"}, "value": "{{listing_url}}"},
        {"fill": {"label": "Email Address"}, "value": "{{email}}"},
        {"human": "captcha"},
        {"click": {"role": "button", "name": "Opt Out"}}
      ],
      "success": {"text": "check your email"}
    },
    "confirm_email": {
      "from": "@spokeo.com",
      "subject": "(?i)opt.?out",
      "link": "^https://www\\.spokeo\\.com/optout/confirm\\?"
    }
  }
}
```

The selectors above are **illustrative**. Spokeo blocks automated fetches, so a real file needs
someone who has loaded the form in a browser.

### Rules the schema and build enforce

These files run on users' machines and come from the community, so they are **declarative
data, never code**:
- **A closed action vocabulary:** `goto`, `fill`, `select`, `check`, `click`, `wait_for`,
  `assert`, `human`. There is no `eval`, no script, and no arbitrary headers or cookies.
- **Locators** prefer `label` and `role`+`name` (accessibility semantics survive redesigns).
  `css` is allowed only as a fallback.
- **Hosts:** every URL must be on `hosts`, and `hosts` must sit under the entry's `domain` or a
  domain declared in the facts layer. An automation file can't send a user's data anywhere the
  dataset doesn't already name.
- **Placeholders** must map to the broker's `required_fields`, using the same rule as templates.
- **`human` steps are mandatory** for `captcha`, `login` and `id_upload`, and for anything the
  facts layer marks sensitive. Automation fills in what it can; the person solves challenges
  and approves sensitive data. The dataset never describes how to defeat a CAPTCHA or a bot
  wall. Whatever a tool does on the user's own machine is that tool's business.
- **`confirm_email`** patterns let a tool with mail permission find the confirmation message
  and *offer* to open the link. Whether it acts without asking is the tool's choice and the
  user's consent, not the dataset's.

### Staleness: reuses the page monitor

`authored_against.fields` uses the same format as `monitor/fingerprints.json`. When the monitor
sees a form's fields drift away from what the automation was written against, the compiled
`automation.json` marks that broker `stale: true`. The monitor issue also gets an
"automation stale" line, and the daily routine treats it as work. Tools should fall back to
guided mode for stale entries instead of filling a form that has moved.

## Compiled artifacts tools consume

| Artifact | Contents | Version |
|---|---|---|
| `data/brokers.json` | facts + `process` + timing fields | `dataset_version` |
| `data/stages.json`, `data/legal.json`, `data/profile-fields.json`, `data/templates/` | shared vocabularies | `dataset_version` |
| `automation/automation.json` | per-broker, per-stage automation + `stale` flags | `automation_version` |

## Open questions

1. **Automation license.** The dataset is CC BY-NC-SA. Should `automation/` be more permissive
   (MIT or CC0) so commercial and nonprofit tool builders alike can ship it? Selectors are
   closer to code than to editorial research.
2. **Legal deadlines beyond CCPA.** Which other state laws (VCDPA, CDPA, Oregon, Texas) get
   entries in `legal.json` in the first pass, and who verifies the numbers?
3. **Does `process` become required** once migration is done? The proposal is yes, at the next
   schema minor version after the derived PR merges.
4. **Who records a process confirmation?** It could be a new `verifications:` record (from the
   verify-flow design) with `scope: process`, or `last_verified` could imply it. The proposal is
   the former, once verification history exists.
