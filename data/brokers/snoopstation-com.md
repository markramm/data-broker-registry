---
id: snoopstation-com
name: Snoopstation.Com
domain: snoopstation.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://suppression.peopleconnect.us/"
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
notes: "MIGRATED research_note: Intelius-network; opt out at intelius.com/opt-out (bot-block 403, live). WebFetch on intelius.com/opt-out returned HTTP 403 (bot-blocked), confirming the prior note. Snoopstation is one of several PeopleConnect-owned people-search brands (with Intelius, Instant Checkmate, TruthFinder); opting out via Intelius's shared PeopleConnect Suppression Center covers Snoopstation too. Multi-step verified-email + DOB flow, so classified guided rather than assisted. Not freshly confirmed against a rendered page -- last_verified left null. 2026-10-14 maintainer: the page monitor found https://www.intelius.com/opt-out/ now redirects to https://suppression.peopleconnect.us/ (PeopleConnect - Suppression Center); opt_out_url and steps updated to point there directly, with steps following the flow already confirmed in peopleconnect-us.md. The redirect itself was observed by the monitor (the suppression center returns 403 to scripted fetches, so its content was not re-read in this run). last_verified unchanged."
---

1. Go to https://suppression.peopleconnect.us/ -- PeopleConnect's shared Suppression Center, which is where Snoopstation's own opt-out link now lands. Enter an email address you can access, agree to the terms, and continue. Complete a CAPTCHA if one is shown.
2. Check your inbox for the verification email from PeopleConnect and click "Verify Email" promptly -- the link can expire.
3. Enter your date of birth when prompted; it is used to match you to records.
4. Enter your legal name and any alternate names (maiden name, former married name, nickname) to widen the match.
5. Review the records the portal surfaces and select the one(s) that are you.
6. Under "Desired Behavior" choose "Suppressed" and save.
7. If the form is inaccessible, email privacy@peopleconnect.us with your name and the Snoopstation listing URL instead.
