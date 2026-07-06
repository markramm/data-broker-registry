---
id: snoopstation-com
name: Snoopstation.Com
domain: snoopstation.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.intelius.com/opt-out/"
opt_out_email: "privacy@peopleconnect.us"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, dob, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "data-brokers-watch + tcp-verified"
notes: "MIGRATED research_note: Intelius-network; opt out at intelius.com/opt-out (bot-block 403, live). WebFetch on intelius.com/opt-out returned HTTP 403 (bot-blocked), confirming the prior note. Snoopstation is one of several PeopleConnect-owned people-search brands (with Intelius, Instant Checkmate, TruthFinder); opting out via Intelius's shared PeopleConnect Suppression Center covers Snoopstation too. Multi-step verified-email + DOB flow, so classified guided rather than assisted. Not freshly confirmed against a rendered page -- last_verified left null."
---

<!-- Real instructions based on PeopleConnect's shared Intelius/Snoopstation suppression flow. -->
1. Go to https://www.intelius.com/opt-out/ (Snoopstation is owned by the same parent, PeopleConnect, and shares this suppression system).
2. Click through to "Do Not Sell or Share My Personal Information" -> "View Public Data Tools" -> "Manage My Suppression Rules" to reach the PeopleConnect Suppression Center.
3. Enter a valid email address, agree to the terms, and submit -- then check your inbox and click the verification link quickly, as it can expire.
4. Enter your full legal name and date of birth (include maiden or alternate names if relevant), then review the matching record(s).
5. Select the record(s) that are you and set their status to "Suppressed" to complete the request.
6. If the form is inaccessible (it may bot-block direct automated requests), email privacy@peopleconnect.us with your name and the Snoopstation listing URL as an alternative.
