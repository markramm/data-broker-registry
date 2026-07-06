---
id: peoplefinderonline-net
name: "People Finder: Instant Online Records Retrieval"
domain: peoplefinderonline.net
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://infotracer.com/optout/"
opt_out_email: null
phone: 617-262-9317
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, address, email]
readd_days: null
legal_basis: []
last_verified: null
source: data-brokers-watch
notes: "Direct fetch of infotracer.com/optout/ hit a rate-limit error page; confirmed via WebSearch instead. peoplefinderonline.net's opt-out routes through InfoTracer's own portal: search by name/state to find your record (CAPTCHA on search), select and remove it, then a second form step asks for email + CAPTCHA again before a confirmation-email verification link. CAPTCHA gating at multiple steps -> guided tier. last_verified left null (not freshly fetched)."
---

1. Go to infotracer.com/optout/ and search for your record by first name, last name, and state.
2. Complete the CAPTCHA to view search results.
3. Find your matching record, check the "select record" box, and click "Remove Data."
4. On the removal form, enter an email address you can access and complete the CAPTCHA again, then submit.
5. Check your inbox for a confirmation email from InfoTracer and click the verification link to finalize the request.
6. Allow up to 72 hours for the listing to be removed; repeat if the record reappears after a data refresh.
