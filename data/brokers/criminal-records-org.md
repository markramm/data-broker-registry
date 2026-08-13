---
id: criminal-records-org
name: Criminal-Records.org (InfoTracer)
domain: criminal-records.org
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "<verify: locate InfoTracer's consumer opt-out/removal page -- criminal-records.org appears to be an InfoTracer-operated criminal-records lookup property and likely shares InfoTracer's central opt-out system, but the exact removal URL was not confirmed by direct fetch (site returned an expired-certificate error)>"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch to criminal-records.org failed with a TLS certificate-expired error, so the live page could not be rendered directly. WebSearch confirms the domain is operated by InfoTracer and indexes county/state criminal and arrest records (felonies and misdemeanors) nationwide, updated daily -- a genuine people-search/background-check data broker with real personal-safety stakes (arrest and conviction data tied to named individuals). InfoTracer-family sites typically require locating your specific record/profile URL and submitting it through a removal form with CAPTCHA. Because the specific opt-out URL for this property could not be confirmed live, opt_out_url is left as a <verify:> placeholder and last_verified is null. Process below is reconstructed from InfoTracer's known standard removal flow (consistent with other InfoTracer-operated lookup sites) but has not been freshly confirmed against a rendered page."
---

1. Search your name on criminal-records.org (or the broader InfoTracer network) and locate the specific record or profile page that matches you.
2. Copy the full URL of that record.
3. Find InfoTracer's opt-out/removal page (commonly linked from the site footer as "Do Not Sell My Info," "Privacy," or "Opt Out") and paste the record URL into the removal form along with a valid email address.
4. Solve the CAPTCHA if presented.
5. Submit the request and check your email for a confirmation link; click it to finalize the removal.
6. Repeat for each distinct matching record, since arrest/court data is often duplicated across multiple listings pulled from different source counties.
7. Because criminal and public-court records are re-ingested periodically from county sources, periodically re-search your name and repeat this process if a record reappears.
