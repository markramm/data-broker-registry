---
id: spydialer-com
name: "Spy Dialer, Inc."
domain: spydialer.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.spydialer.com/optout.aspx"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, phone]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: data-brokers-watch
notes: "WebFetch on /Consumers/ returned only marketing copy (JS-rendered wizard). Real removal form lives at spydialer.com/optout.aspx per multiple 2026 opt-out-guide writeups (Security.org, Incogni, mePrism); flow is: pick state, solve CAPTCHA, continue past a privacy-law notice, then add the phone number/name to opt out. CAPTCHA-gated multi-step wizard -> guided tier. Updated opt_out_url from the bare /Consumers/ landing page to the actual optout.aspx tool. Not freshly confirmed against a rendered page -- last_verified left null."
---

<!-- Real instructions based on Spy Dialer's documented opt-out wizard. -->
1. Go to https://www.spydialer.com/optout.aspx (or click "Do Not Sell Or Share My Personal Information" in the site footer).
2. Select your state from the dropdown and solve the CAPTCHA, then click "Continue."
3. Click through the privacy-law notice ("Got it, continue").
4. Enter the name and phone number you want removed from Spy Dialer's reverse-lookup index.
5. Click "Opt-out my info" to submit the request.
6. Wait 24-72 hours, then search your own number on Spy Dialer to confirm it no longer returns a listing; repeat if it reappears.
