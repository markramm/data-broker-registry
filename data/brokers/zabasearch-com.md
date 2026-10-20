---
id: zabasearch-com
name: Zabasearch
domain: zabasearch.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://suppression.peopleconnect.us/"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: ["full_name", "address", "dob"]
readd_days: null
legal_basis: []
last_verified: null
source: data-brokers-watch
notes: "MIGRATED opt_out_url pointed at intelius.com/optout, which did not resolve for fetch tooling in this session; corrected to the documented intelius.com/opt-out path per removal-guide consensus (GhostMyData, Security.org, Incogni, Clearnym, mydataremoval.com). ZabaSearch is a PeopleConnect brand; per multiple guides, opting out of ZabaSearch means going through the shared Intelius/PeopleConnect suppression form, then separately checking addresses.com and anywho.com since they can carry duplicate listings. Requires email verification and DOB entry; no CAPTCHA reported but the multi-step verification loop and DOB requirement warrant guided rather than assisted. Not freshly confirmed against the live page. 2026-10-14 maintainer: the page monitor found https://www.intelius.com/opt-out now redirects to https://suppression.peopleconnect.us/ (PeopleConnect - Suppression Center); opt_out_url and steps updated to point there directly, with steps following the flow already confirmed in peopleconnect-us.md. The redirect itself was observed by the monitor (the suppression center returns 403 to scripted fetches, so its content was not re-read in this run). last_verified unchanged."
---

1. Go to https://suppression.peopleconnect.us/ -- PeopleConnect's shared Suppression Center, which is where ZabaSearch's own opt-out link now lands. Enter an email address you can access, agree to the terms, and continue. Complete a CAPTCHA if one is shown.
2. Check your inbox for the verification email from PeopleConnect and click "Verify Email" promptly -- the link can expire.
3. Enter your date of birth when prompted; it is used to match you to records.
4. Enter your legal name and any alternate names (maiden name, former married name, nickname) to widen the match.
5. Review the records the portal surfaces and select the one(s) that are you.
6. Under "Desired Behavior" choose "Suppressed" and save.
7. Afterward, search zabasearch.com, addresses.com and anywho.com separately to confirm the listing is gone from each -- these affiliated sites can carry duplicate records.
