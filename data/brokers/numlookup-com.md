---
id: numlookup-com
name: "NumLookup"
domain: numlookup.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.numlookup.com/opt_out"
opt_out_email: "hello@numlookup.com"
phone: "1-844-405-2145"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [phone, full_name]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-10-17 by the daily maintainer from California's data broker registry (NumLookup LLC, listing hello@numlookup.com and https://www.numlookup.com/privacy-policy). The privacy policy (fetched, HTTP 200) section 2 'Information Opt-Out' links to an opt-out tool at https://www.numlookup.com/opt_out and says all 31,826 (2023) and 94,071 (2024) opt-out requests were approved, completing in under 30 / 20 days on average. Fetched the tool directly (HTTP 200): it has two tabs, PHONE (country + phone number) and NAME (full name + US state), one listing per submission, and a visible reCAPTCHA v2 box (div#captcha, 304x78, rendered via recaptcha/api.js; the script blocks submit with 'Please verify captcha'). No email field is on the first screen; what happens after 'Remove My Info' (record selection, confirmation) was not observed because nothing was submitted. Reverse-phone and people-search product -> people_search true, priority crucial; CAPTCHA -> guided. required_fields lists both phone and full_name because the two tabs remove different listings and most people will want both. hello@numlookup.com is the policy's contact for know/correct requests. last_verified null."
---

1. Go to https://www.numlookup.com/opt_out.
2. To remove a phone listing: stay on the PHONE tab, pick the country, and enter the phone number.
3. Complete the reCAPTCHA and click "Remove My Info", then follow any on-screen steps to confirm the listing.
4. To remove a name listing: return to the page, choose the NAME tab, enter your full name and select your state, complete the reCAPTCHA again and click "Remove My Info".
5. Repeat for each phone number and each name/state combination you want removed.
6. NumLookup says removals usually complete within 20-30 days. Search the site again after that to check, and if a listing is still there, email hello@numlookup.com or call 1-844-405-2145.
