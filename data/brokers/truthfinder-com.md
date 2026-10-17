---
id: truthfinder-com
name: Truthfinder
domain: truthfinder.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://suppression.peopleconnect.us/"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: ["email", "full_name", "dob"]
readd_days: null
legal_basis: []
last_verified: null
source: "data-brokers-watch + tcp-verified"
notes: "MIGRATED research_note: live behind Cloudflare; routes through PeopleConnect suppression. Direct fetch returned 403 in this session; assessed from third-party removal-guide consensus (Clearnym, GhostMyData, Security.org, Optery). Flow is CAPTCHA-gated with email + DOB identity verification, so guided rather than assisted despite method:form. Not freshly confirmed against the live page. 2026-10-14 maintainer: the page monitor found https://www.truthfinder.com/opt-out/ now redirects to https://suppression.peopleconnect.us/ (PeopleConnect - Suppression Center); opt_out_url and steps updated to point there directly, with steps following the flow already confirmed in peopleconnect-us.md. The redirect itself was observed by the monitor (the suppression center returns 403 to scripted fetches, so its content was not re-read in this run). last_verified unchanged."
---

1. Go to https://suppression.peopleconnect.us/ -- PeopleConnect's shared Suppression Center, which is where TruthFinder's own opt-out link now lands. Enter an email address you can access, agree to the terms, and continue. Complete a CAPTCHA if one is shown.
2. Check your inbox for the verification email from PeopleConnect and click "Verify Email" promptly -- the link can expire.
3. Enter your date of birth when prompted; it is used to match you to records.
4. Enter your legal name and any alternate names (maiden name, former married name, nickname) to widen the match.
5. Review the records the portal surfaces and select the one(s) that are you.
6. Under "Desired Behavior" choose "Suppressed" and save.
7. Allow 7-14 days, then search your name on truthfinder.com to confirm the listing is gone.
