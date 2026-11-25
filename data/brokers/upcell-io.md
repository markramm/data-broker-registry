---
id: upcell-io
name: "upcell"
domain: upcell.io
category: b2b_contact_data
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://www.upcell.io/data-claim"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Listed in the California data broker registry (upcell, LLC), whose rights URL is upcell.io/data-claim. On 2026-11-24 I fetched that page with curl and rendered it in a headless browser without typing anything or submitting. The page, 'Data Rights & Removal Request', says that after you submit the form 'your record will be permanently suppressed and will no longer be available through our platform', that opt-out and deletion requests are handled the same way, and that upcell responds within 30 days. The form has required First Name, Last Name and Business Email fields, an optional Phone Number field, and a required 'Request Type' select with 'Opt-Out / Delete My Information', 'Data Access' and 'Other Privacy Request'. No CAPTCHA widget or captcha script loaded, so tier assisted. The page says nothing about a confirmation email, so verification is left null rather than guessed. upcell is a B2B sales-prospecting and contact-enrichment platform (its site compares itself with ZoomInfo, Apollo, Lusha and RocketReach), so priority standard. Not walked through by a human: last_verified null."
---

1. Open upcell's removal form at https://www.upcell.io/data-claim.
2. Enter your first name, last name and the business email address upcell might hold for you. Phone number is optional.
3. Under "Request Type", choose "Opt-Out / Delete My Information".
4. Click "Submit". upcell says your record will be permanently suppressed and that it responds within 30 days.
5. Repeat for each work email address you have used.
