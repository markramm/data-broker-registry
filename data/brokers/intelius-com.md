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
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, dob, email]
readd_days: 3
legal_basis: [ccpa]
last_verified: null
source: "data-brokers-watch + tcp-verified"
notes: "Intelius is a hub in the PeopleConnect/CID network: this same opt-out portal (or its suppression-center sibling) is the actual removal mechanism for other files in this batch, including instantpeoplefinder-com and intelregistry-com, both of which point their opt_out_url at Intelius. WebFetch was blocked on both www.intelius.com and intelius.com (host unreachable from this environment) and could not be freshly confirmed. Assessed consistently across multiple third-party guides (cybernews, Optery, GhostMyData, Incogni, security.org): from the homepage, click 'Do Not Sell or Share My Personal Info' -> 'view public data tools' -> 'manage my suppression rules' to reach the opt-out form; then email + CAPTCHA, email verification link (~15 min expiry), legal name + DOB + CAPTCHA, select your matching record, and a final email confirmation link. No ID upload, no fee, no phone-only requirement, but a genuinely multi-step CAPTCHA-gated identity flow -> tier guided. Deletion reported to take ~72 hours once submitted."
---

1. Go to Intelius's opt-out page (linked above), or from Intelius.com click "Do Not Sell or Share My Personal Info" in the footer, then "view public data tools" and "manage my suppression rules" to reach the same form.
2. Enter your email address and complete the CAPTCHA, then submit to receive a verification email.
3. Open the email and click the verification link promptly -- it typically expires after about 15 minutes.
4. Provide your legal name and date of birth, completing another CAPTCHA if prompted, and submit.
5. From the list of matching records, locate your listing (cross-check address or other details) and click "Remove This Record."
6. Open the confirmation email that follows and click its link -- the removal doesn't finalize until you do. If you'd rather not use the web form, you can call Intelius directly at (206) 301-5800. Full removal typically takes about 72 hours.
