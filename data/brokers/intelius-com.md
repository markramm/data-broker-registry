---
id: intelius-com
name: Intelius
domain: intelius.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: portal
opt_out_url: "https://www.intelius.com/opt-out"
opt_out_email: null
phone: "(206) 301-5800"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, dob, email]
readd_days: 3
legal_basis: [ccpa]
last_verified: "2026-08-13"
source: "data-brokers-watch + tcp-verified + chrome-verified"
notes: "Chrome-driven verification (2026-08-13) confirmed https://www.intelius.com/opt-out redirects directly to https://suppression.peopleconnect.us/login -- the SAME shared PeopleConnect suppression portal used by peopleconnect-us and instantcheckmate-com, not a separate Intelius-specific flow. The reachable step is 'Step 1: Enter your email address' with no CAPTCHA visible; full_name/dob are requested at a later step in the flow per the PeopleConnect suppression entries, not confirmed independently here. Set captcha:false and tier should be treated as equivalent to peopleconnect-us going forward -- the earlier guided/CAPTCHA assessment appears to describe an older or alternate entry point that no longer matches what the documented opt_out_url actually loads. Deletion timing (~72 hours) not re-confirmed live."
---

1. Go to Intelius's opt-out page (linked above), or from Intelius.com click "Do Not Sell or Share My Personal Info" in the footer, then "view public data tools" and "manage my suppression rules" to reach the same form.
2. Enter your email address and complete the CAPTCHA, then submit to receive a verification email.
3. Open the email and click the verification link promptly -- it typically expires after about 15 minutes.
4. Provide your legal name and date of birth, completing another CAPTCHA if prompted, and submit.
5. From the list of matching records, locate your listing (cross-check address or other details) and click "Remove This Record."
6. Open the confirmation email that follows and click its link -- the removal doesn't finalize until you do. If you'd rather not use the web form, you can call Intelius directly at (206) 301-5800. Full removal typically takes about 72 hours.
