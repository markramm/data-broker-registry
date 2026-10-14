---
id: peoplefinder-com
name: "PeopleFinder.com"
domain: peoplefinder.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: portal
opt_out_url: "https://suppression.peopleconnect.us/"
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
source: "dbw+tcp-research"
notes: "curl-fetched peoplefinder.com's homepage directly (HTTP 200). It is a live people-search site offering name/phone/address lookups returning owner name, age, address, phone, social media, and background-check-adjacent results -- real personal-safety exposure, priority crucial. Both privacy-related links on the homepage point to intelius.com (https://www.intelius.com/privacy-center/ and https://www.intelius.com/privacy-policy/), not a peoplefinder.com-hosted privacy page, indicating PeopleFinder.com is operated on Intelius/PeopleConnect infrastructure -- the same relationship already documented for instantpeoplefinder-com.md and intelius-com.md in this dataset (both already authored, both point their opt-out at Intelius's own suppression tool). No PeopleFinder-specific opt-out page or form was found; following the same pattern as those existing entries, opt_out_url/phone/process here are copied from the already-authored intelius-com.md entry rather than independently re-derived, since WebFetch could not reach intelius.com directly this session either (consistent with the intelius-com.md note that it's unreachable from this environment) and third-party guide-based reconstruction would be redundant with that existing entry. Tier guided (CAPTCHA + multi-step identity flow, per intelius-com.md). Not independently re-verified beyond confirming the peoplefinder.com->intelius.com link relationship this session; last_verified left null. 2026-10-14 maintainer: the page monitor found https://www.intelius.com/opt-out now redirects to https://suppression.peopleconnect.us/ (PeopleConnect - Suppression Center); opt_out_url and steps updated to point there directly, with steps following the flow already confirmed in peopleconnect-us.md. The redirect itself was observed by the monitor (the suppression center returns 403 to scripted fetches, so its content was not re-read in this run). last_verified unchanged."
---

1. Go to https://suppression.peopleconnect.us/ -- PeopleConnect's shared Suppression Center, which is where PeopleFinder.com's own opt-out link now lands. Enter an email address you can access, agree to the terms, and continue. Complete a CAPTCHA if one is shown.
2. Check your inbox for the verification email from PeopleConnect and click "Verify Email" promptly -- the link can expire.
3. Enter your date of birth when prompted; it is used to match you to records.
4. Enter your legal name and any alternate names (maiden name, former married name, nickname) to widen the match.
5. Review the records the portal surfaces and select the one(s) that are you.
6. Under "Desired Behavior" choose "Suppressed" and save.
7. Allow a few days, then search your name on peoplefinder.com to confirm. Re-check periodically, since re-scraped data can bring a listing back.
