---
id: truepeoplesearch-com
name: TruePeopleSearch
domain: truepeoplesearch.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.truepeoplesearch.com/removal"
opt_out_email: "support@truepeoplesearch.com"
phone: "415-869-6899"
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, full_name, address, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "data-brokers-watch + tcp-verified"
notes: "WebFetch on truepeoplesearch.com/removal failed outright (tool could not fetch host). Process reconstructed from multiple independent 2026 opt-out-guide writeups (Security.org, Incogni, Atlas Privacy, idstrong) which consistently describe: search name/city/state to find the listing, open it, click 'Remove This Record,' then enter email, solve a CAPTCHA, agree to terms, and confirm via an emailed link within 72 hours. CAPTCHA-gated multi-step flow -> guided tier despite no ID/phone requirement. Support email and two phone numbers (415-869-6899 primary, 888-838-4803 fallback if the form fails) noted as alternates. Not freshly confirmed against a rendered page -- last_verified left null."
---

<!-- Real instructions based on TruePeopleSearch's documented removal flow. -->
1. Go to https://www.truepeoplesearch.com/removal and enter your full name, city, and state to find your listing.
2. Open the record that matches you and click "View Details," then find and click "Remove This Record" at the bottom of the page.
3. Enter your email address, solve the CAPTCHA, and agree to the removal terms.
4. Submit the request, then check your email for a confirmation message from TruePeopleSearch and click the link inside to finalize it.
5. Repeat for each separate matching listing (up to five requests per email address); removal should complete within about 72 hours.
6. If the online form doesn't work, email support@truepeoplesearch.com or call 415-869-6899 (or 888-838-4803) for help.
