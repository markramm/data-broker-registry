---
id: wyty-com
name: Wyty
domain: wyty.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.wyty.com/remove/"
opt_out_email: null
phone: "888-211-2291"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [full_name, address, email, phone]
readd_days: 365
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on wyty.com and wyty.com/remove/ succeeded and rendered live content. Wyty (operated by Wyty LLC) is a people-search/reverse-lookup site offering name, reverse-phone, and reverse-address searches returning 'phone numbers, addresses, relatives, age, and more' from public records. The site's own /remove/ page describes a CAPTCHA-gated opt-out form requesting first/middle/last name, address, city, state, phone, and email (email used for confirmation only), plus phone and email alternatives to the web form. The privacy policy states a roughly 12-month (365-day) wait before re-authorizing a Personal Information sale, which we use as readd_days. CAPTCHA present -> guided tier despite an otherwise-normal form. Not independently re-rendered after this pass -- last_verified left null."
---

1. Go to https://www.wyty.com/remove/ (Wyty's "Do Not Sell My Personal Information" removal page, linked from the site footer).
2. Enter your first, middle, and last name, your address, city, and state, and a phone number if you have one on file with Wyty.
3. Enter a valid email address -- Wyty uses this only to send a confirmation receipt, not as part of the stored opt-out record.
4. Solve the CAPTCHA and submit the form.
5. Alternatively, you can request removal by phone at 888-211-2291 or by emailing privacy@wyty.com instead of using the web form.
6. Wyty states removal typically takes 7-14 days from receipt of the request, and that it will wait at least 12 months before asking you to reauthorize a sale of your personal information -- plan to re-check or resubmit roughly once a year.
