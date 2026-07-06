---
id: reverserecords-org
name: Reverserecords.Org
domain: reverserecords.org
category: people_search
people_search: true
tier: guided
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
legal_basis: []
last_verified: null
source: "data-brokers-watch + tcp-verified"
notes: "Confirmed live 2026-07-03 that reverserecords.org itself is unreachable -- WebFetch failed with 'certificate has expired', consistent with the prior MIGRATED research_note. Removal must go through the shared InfoTracer opt-out portal instead (same network as Records Authority / Reverse Genie): name+state search with CAPTCHA, select record, second CAPTCHA + email, confirm via emailed link. last_verified left null because although the broken cert was confirmed, the InfoTracer opt-out steps themselves were not freshly fetched (rate-limited on attempt) -- only corroborated via third-party guides."
---

1. Do not visit reverserecords.org directly -- its own domain's SSL certificate has expired, so your browser will show a security warning and no functional opt-out page loads there.
2. Instead, go to `https://infotracer.com/optout/` -- Reverse Records is part of the InfoTracer network and removal is handled centrally from there.
3. Enter your first and last name, select your state, enter your city, and submit.
4. Check the "I'm not a robot" verification box to see search results.
5. Find your record, check the box to select it, then click the "Remove Data" button that appears.
6. Enter your email address, complete the CAPTCHA, submit, then check your email and click "Confirm Email" to finalize the removal.
