---
id: hireright-com
name: General Information Solutions LLC
domain: hireright.com
category: background_check
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "<verify: exact contact method/fields on https://www.hireright.com/legal/do-not-sell-my-personal-information>"
opt_out_email: null
phone: null
captcha: false
id_required: true
phone_required: false
charges_fee: false
verification: id_upload
required_fields: [full_name, address, email, gov_id]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "HireRight (operating as General Information Solutions LLC per the legacy CSV) is a major employment background-check/screening company -- same pattern as backgroundchecks.com and cbcinnovis.com from prior rounds: a genuine broker of identity/employment-history records on named individuals, people_search:true, crucial priority. Raw curl of hireright.com/legal/privacy-policy confirmed the policy explicitly states: 'HireRight abides by the opt-out provisions of the CCPA, but the CCPA does not apply to background screening' (mirroring backgroundchecks.com's disclaimer), and links out to a dedicated sub-page at /legal/do-not-sell-my-personal-information. That sub-page and hireright.com/legal (the parent legal-policies index) are a JavaScript-rendered single-page app -- WebFetch repeatedly returned only the page title/shell and raw curl did not render app content, so the exact form fields, CAPTCHA presence, or submission mechanism on that page could not be confirmed. Because FCRA-governed background-check opt-outs (per the backgroundchecks.com precedent) typically require a government-ID upload, and given the confirmed existence but unconfirmed mechanics of a dedicated do-not-sell page, this is marked guided/crucial with id_required:true as a conservative default matching the established pattern for this broker category, but opt_out_url is a <verify:> placeholder and opt_out_email is left null since neither could be independently confirmed. last_verified is null per placeholder rule."
---

1. Go to https://www.hireright.com/legal/do-not-sell-my-personal-information -- HireRight's dedicated California "Do Not Sell or Share My Personal Information" page, linked from their main privacy policy.
2. Note that HireRight's privacy policy states the CCPA "does not apply to background screening" -- if your concern is about the accuracy of a background-check report (rather than a data-sale opt-out), use HireRight's separate FCRA dispute process instead of the CCPA page.
3. Follow the instructions on the do-not-sell page to submit your opt-out request. (The exact form fields and whether a government-ID upload is required could not be independently confirmed for this entry -- treat as likely, based on comparable FCRA-governed background-check brokers, but verify on the live page.)
4. If the dedicated page is unavailable, HireRight's main Legal Policies index at https://www.hireright.com/legal lists related notices, including "United States Opt-Out Rights (Outside of California)" for non-California state privacy laws.
5. Keep a copy of your submission and any confirmation you receive.
