---
id: spokeo-com
name: Spokeo
domain: spokeo.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.spokeo.com/optout"
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
source: "data-brokers-watch + tcp-verified"
notes: "WebFetch on spokeo.com/optout returned HTTP 403 (bot-blocked). Process reconstructed from multiple independent 2026 opt-out-guide writeups (Incogni, DeleteMe, Security.org, OneRep) which consistently describe: find your profile, copy its URL, paste into the opt-out form with an email, solve a CAPTCHA, then click an emailed confirmation link. CAPTCHA-gated -> guided tier despite being only a 2-field form. Not freshly confirmed against a rendered page -- last_verified left null."
---

<!-- Real instructions based on Spokeo's documented opt-out form flow. -->
1. Search your name on spokeo.com and open the profile that matches you; copy that profile's URL.
2. Go to https://www.spokeo.com/optout (or follow "Do Not Sell My Info" in the site footer).
3. Paste the profile URL into the opt-out form, enter a valid email address, and solve the CAPTCHA.
4. Click "Opt out" to submit the request.
5. Check your email for a confirmation message from Spokeo and click the confirmation link -- the opt-out isn't final until you confirm.
6. Repeat separately for each distinct matching profile; expect the request to process within 24-48 hours, and re-check periodically since Spokeo re-ingests public records.
