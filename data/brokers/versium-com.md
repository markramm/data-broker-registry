---
id: versium-com
name: "Versium"
domain: versium.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://versium.com/ccpa-opt-out/"
opt_out_email: "optout@versium.com"
phone: "1-800-395-0164"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: ["full_name", "email", "address", "dob", "phone"]
readd_days: null
legal_basis: ["ccpa", "cpra"]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on versium.com's privacy policy surfaced an opt-out page at /ccpa-opt-out/ (confirmed reachable, HTTP 200 on redirect check), plus an alternate email channel (optout@versium.com) and postal/phone options. Versium is an identity-resolution / marketing-data and analytics vendor (B2B data append and audience-targeting services), not a people-search site, so people_search is false and priority is high rather than crucial. No CAPTCHA or ID upload found in the fetched policy text, so assisted tier. Page content was summarized by WebFetch, not rendered directly by this agent -- last_verified left null."
---

1. Go to the [Versium CCPA opt-out page](https://versium.com/ccpa-opt-out/) and follow the form instructions, or
2. Email optout@versium.com with your full name, email address, street address, date of birth, and phone number, and request that Versium opt you out of data sale/sharing and delete your record.
3. Alternatively, call 1-800-395-0164 (or write to Versium, 7530 164th Avenue NE, Suite A204, Redmond, WA 98052, Attn: Privacy) with the same information.
4. Keep a copy of your request; Versium's policy does not specify a standard confirmation timeline, so follow up if you don't hear back within a few weeks.
