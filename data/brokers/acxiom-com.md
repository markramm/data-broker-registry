---
id: acxiom-com
name: "Acxiom Llc"
domain: acxiom.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://isapps.acxiom.com/optout/optout.aspx"
opt_out_email: null
phone: "1-877-774-2094"
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: ["full_name", "email", "address", "phone"]
readd_days: null
legal_basis: ["ccpa"]
last_verified: "2026-07-03"
source: data-brokers-watch
notes: "Fetched isapps.acxiom.com/optout/optout.aspx directly: self-serve form collecting name (incl. variants/nicknames/former names), phone numbers, email addresses, and mailing addresses, with per-category opt-out checkboxes. Third-party guides (Optery, Clearnym) additionally describe an email + CAPTCHA + confirmation-link verification step not fully visible in the raw fetch, so captcha is marked true. No ID upload or mandatory phone call -- a careful human can deep-link and paste fields, so assisted rather than guided. Acxiom is a marketing data aggregator (not people-search), so priority is high rather than crucial."
---

1. Go to the [Acxiom opt-out form](https://isapps.acxiom.com/optout/optout.aspx).
2. Choose which categories to opt out of (mailing addresses, phone numbers, email addresses) -- select all that apply.
3. Enter your full name, including any nicknames, former/married names, or common misspellings, using the "+" buttons to add each variant.
4. Enter every phone number, email address, and mailing address associated with you, then submit.
5. Enter your email address and complete the CAPTCHA to receive a confirmation link.
6. Open the confirmation email and click the verification link to finalize the opt-out request.
