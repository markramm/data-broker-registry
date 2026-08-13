---
id: peoplefinder-com
name: "PeopleFinder.com"
domain: peoplefinder.com
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
source: "dbw+tcp-research"
notes: "curl-fetched peoplefinder.com's homepage directly (HTTP 200). It is a live people-search site offering name/phone/address lookups returning owner name, age, address, phone, social media, and background-check-adjacent results -- real personal-safety exposure, priority crucial. Both privacy-related links on the homepage point to intelius.com (https://www.intelius.com/privacy-center/ and https://www.intelius.com/privacy-policy/), not a peoplefinder.com-hosted privacy page, indicating PeopleFinder.com is operated on Intelius/PeopleConnect infrastructure -- the same relationship already documented for instantpeoplefinder-com.md and intelius-com.md in this dataset (both already authored, both point their opt-out at Intelius's own suppression tool). No PeopleFinder-specific opt-out page or form was found; following the same pattern as those existing entries, opt_out_url/phone/process here are copied from the already-authored intelius-com.md entry rather than independently re-derived, since WebFetch could not reach intelius.com directly this session either (consistent with the intelius-com.md note that it's unreachable from this environment) and third-party guide-based reconstruction would be redundant with that existing entry. Tier guided (CAPTCHA + multi-step identity flow, per intelius-com.md). Not independently re-verified beyond confirming the peoplefinder.com->intelius.com link relationship this session; last_verified left null."
---

1. Go to Intelius's opt-out page at https://www.intelius.com/opt-out -- PeopleFinder.com's own privacy links point directly to Intelius, meaning Intelius operates the underlying database and removal tool behind this site (the same relationship as instantpeoplefinder.com in this dataset).
2. Enter your email address and complete the CAPTCHA, then submit to receive a verification email.
3. Open the email and click the verification link promptly -- it typically expires after about 15 minutes.
4. Provide your legal name and date of birth, completing another CAPTCHA if prompted, and submit.
5. From the list of matching records, locate your listing (cross-check address or other details) and click "Remove This Record."
6. Open the confirmation email that follows and click its link -- the removal doesn't finalize until you do. If you'd rather not use the web form, you can call Intelius directly at (206) 301-5800. Full removal typically takes about 72 hours, and re-scraping can reintroduce a listing after a few days, so periodic re-checks are worthwhile.
