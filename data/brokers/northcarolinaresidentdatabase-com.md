---
id: northcarolinaresidentdatabase-com
name: North Carolina Resident Database
domain: northcarolinaresidentdatabase.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "<verify: site is fully Cloudflare bot-blocked (403/challenge page on / and /opt-out) in every fetch attempted this session; exact opt-out URL and form fields not directly confirmed, only inferred from search-result summaries>"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, full_name]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "northcarolinaresidentdatabase.com is a people-search site covering North Carolina residents: names, addresses, phone numbers, emails, birth dates/ages, household/neighbor information, reverse phone lookup, and voter-registration-derived details, browsable by city/county/street. Direct fetches of both '/' and '/opt-out' returned Cloudflare 403/JS-challenge pages in this session (could not render actual content). Search-result summaries (not independently verified) describe an opt-out page at /opt-out where you paste the URL of the record you want removed and answer a CAPTCHA-style security prompt, with removal taking 1-2 days; this could not be confirmed by directly loading the page, so opt_out_url is left as a placeholder and last_verified is null. people_search:true and priority:crucial given real personal-safety stakes (addresses, phone numbers, voter data). captcha:true reflects the (unverified) search-summary description of a security prompt on the opt-out form."
---

1. Search your name and city on northcarolinaresidentdatabase.com and locate the profile that matches you; copy that profile's URL. (Verify the exact opt-out page yourself -- the site blocked automated fetches during this research, so the details below could not be independently confirmed.)
2. Go to the site's opt-out page (reported at northcarolinaresidentdatabase.com/opt-out, but confirm this is current since it was not independently verified) and paste in the URL of the record you want removed.
3. Answer any CAPTCHA or security-style prompt the form presents, and submit the request.
4. Removal is reported to take roughly one to two days to process; check back on your profile after that window to confirm it's gone, and re-check periodically since these sites commonly re-ingest public records.
