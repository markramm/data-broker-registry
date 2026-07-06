---
id: infotracer-com
name: Infotracer
domain: infotracer.com
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://infotracer.com/optout/"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, address, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: data-brokers-watch
notes: "Hub/parent people-search site for a broader network. Direct WebFetch hit a 'requested too many times' rate-limit page rather than the real form, so not freshly confirmed -- assessed from consistent third-party opt-out guides (Incogni, Optery, IDStrong, OneRep) describing the current flow: name/city/state search, select record, email + CAPTCHA, email verification link, ~72hr processing. last_verified left null pending a successful direct fetch."
---

1. Go to Infotracer's opt-out page (linked above).
2. Enter your first name, last name, state, and city, then submit the search.
3. Find the record matching you in the results and check the box in the "select record" column, then click the red "remove data" button.
4. Enter your email address and complete the CAPTCHA challenge, then submit.
5. Check your inbox for a verification email from Infotracer and click the "Click Here" link to confirm.
6. Removal typically completes within about 72 hours.
