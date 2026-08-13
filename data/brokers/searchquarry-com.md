---
id: searchquarry-com
name: SearchQuarry
domain: searchquarry.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://members.searchquarry.com/opt-out"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on searchquarry.com and members.searchquarry.com/opt-out succeeded directly (not bot-blocked). SearchQuarry is a public-records/background-check people-search site (criminal, court, civil, driving, vehicle records) with a paid 'JOIN' membership funnel. Footer carries both 'Exercise My Privacy Rights' and 'Do Not Sell / Share My Personal Information' links, both routing to the same members.searchquarry.com/opt-out page. The standard opt-out form asks for first name, last name, state, and optional city -- no CAPTCHA or ID was observed in the fetched content, but there is also a separate OneTrust-hosted 'Data Subject Rights' portal for broader requests, and a separate email path (privacy@searchquarry.com) specifically for legally-covered persons (judges, law enforcement, family under the Daniel Anderl Judicial Security and Privacy Act). Classified guided rather than assisted because the standard form only locates matching records by name/state rather than a submitted listing URL, so multiple matching profiles/manual confirmation is likely required; last_verified left null since this is single-session research, not a repeat-confirmed process."
---

1. Go to [searchquarry.com](https://www.searchquarry.com) and search your own name to see what listings exist about you (you do not need to pay to see that a listing exists).
2. Scroll to the site footer and click "Do Not Sell / Share My Personal Information" (or go directly to the [opt-out form](https://members.searchquarry.com/opt-out)).
3. Enter your first name, last name, and state (city is optional but helps narrow the match) and submit the form.
4. Review the matching record(s) SearchQuarry surfaces and confirm the ones that are you for removal.
5. If you are a judge, law enforcement officer, or an immediate family member of one, you may instead qualify for expedited removal under the Daniel Anderl Judicial Security and Privacy Act: email privacy@searchquarry.com with your full name, residence, email address, and a note confirming your covered-person status, using the subject line "Attention Covered Person Removal Request."
6. For broader data-subject-rights requests (access, deletion, correction) beyond the simple opt-out, use the linked OneTrust privacy-rights portal referenced on the same page.
7. Recheck periodically, since public-records aggregators like SearchQuarry re-pull source data and listings can reappear.
