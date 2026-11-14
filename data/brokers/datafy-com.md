---
id: datafy-com
name: "Datafy, LLC"
domain: datafy.com
category: location_ad_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.datafy.com/opt-out"
opt_out_email: "opt-out@datafy.com"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [full_name, email, other]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Added 2026-11-14 by the daily maintainer from the California data broker registry (Datafy, LLC; registry email opt-out@datafy.com, rights URL datafy.com/opt-out). Datafy's homepage describes analytics and ad tech built on 'visitation, spending, and behavioral signals'. Its opt-out page ('Datafy - Personal Data Rights Request') says the Mobile Advertising ID (MAID / IDFA / AAID) is 'one of the identifiers that we use most often' and that 'we require this ID in your request, otherwise we will not be able to match your personal data' -- though the form field itself is marked optional. Rendered the form headless (nothing submitted): required first name, last name, primary email, myself/another individual, country, state, a request type (opt out of sale/use, know, limit, delete, correct) and a typed signature; optional MAID, secondary email and notes. A visible Cloudflare Turnstile widget (data-size normal) is on the page, so captcha true and tier guided. The page also mentions a request-status page keyed by request ID. Visitation/device-ID data -> high priority, not people-search. The registry email was not confirmed on Datafy's own page. last_verified left null."
---

1. Find your phone's advertising ID first -- Datafy says it matches records by this ID. On Android: Settings > Privacy > Ads (or Settings > Google > Ads). On iPhone, Apple doesn't show the IDFA directly; Datafy's page says you need a third-party app to view it. If you can't get it, you can still submit, but Datafy may not find your data.
2. Go to https://www.datafy.com/opt-out.
3. Enter your first and last name, email, country and state, and choose "Myself".
4. Paste your Mobile Device Advertising ID.
5. Under the requested action, choose "Opt-out of the sale and use of my personal data" (submit a second request choosing the delete option if you also want deletion).
6. Type your name as the signature, complete the CAPTCHA, and submit. Keep the request ID if one is shown so you can check its status later.
7. If the form doesn't work, email opt-out@datafy.com (the address in Datafy's California registry filing) with the same details, including your advertising ID.
