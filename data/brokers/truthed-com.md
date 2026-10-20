---
id: truthed-com
name: "Truthed"
domain: truthed.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.truthed.com/optout"
opt_out_email: null
phone: "1-888-387-5010"
captcha: false
id_required: true
phone_required: false
charges_fee: false
verification: id_verify
required_fields: [full_name, email, gov_id]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-10-20 by the daily maintainer from California's data broker registry (Truthed, Inc; rights_url https://www.truthed.com/optout). The registry contact is a named individual's address, so it is not used as opt_out_email. Truthed describes itself as 'a modern people search and background check platform', so people_search is true and priority is crucial. Pages were rendered in a headless browser. /optout (HTTP 200) asks 'Do you want to remove your personal information from our search results?' and its 'Yes, remove my information' button leads to /optout/search, a record search with first, middle and last name, city, state and age fields. The record-selection and confirmation steps after the search were not reached, because that would mean searching a real person. The site's guide, /resources/want-to-opt-out-from-our-people-search, says: 'IMPORTANT: ID required. You'll need to provide proof of your identity before we can complete your request.' It also says you select your record, confirm, and receive an email confirmation; removal is free, needs no membership, and takes up to 5 business days. Because ID is required, the tier is guided and id_required is true. The exact ID step (upload or other) was not seen. No CAPTCHA was on the search form. However, a second load of /optout/search and a load of /privacy-center returned HTTP 403 with a Cloudflare 'Performing security verification' (Turnstile) interstitial, so a human visitor may also get a bot check. Nothing was submitted; last_verified is null."
---

1. Go to https://www.truthed.com/optout. The site footer also links to it as "Remove My Information". Click "Yes, remove my information".
2. On the search page, enter your first and last name. City, state and age help narrow the results. Then click "Search Records".
3. Find your record in the results and confirm that you want it removed.
4. Truthed says it needs proof of identity before it completes a removal. Follow the prompts to provide it, and share only what is required.
5. Watch for the confirmation email, which says the opt-out is under way.
6. Truthed says removal can take up to 5 business days. After that, clear your browser cache and search your name again. If a record is still showing, or a new one appears later, contact Truthed again.
7. For problems, call 1 (888) 387-5010 (Monday-Friday, 7am-5pm PT).
