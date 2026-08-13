---
id: allpeople-com
name: "AllPeople"
domain: allpeople.com
category: people_search
people_search: true
tier: guided
priority: high
method: form
opt_out_url: "https://allpeople.com/privacy"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: ["listing_url", "full_name"]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Legacy CSV only had a 'privacyduck.com' source_url with no other fields -- independently researched via WebSearch/WebFetch on third-party opt-out guides (DeleteMe/JoinDeleteMe writeup) since allpeople.com itself wasn't directly fetchable in this session. Site aggregates professional/business contact profiles (name, position, email, phone, employer, address) searchable by name -- functions as a people-search/contact-lookup broker even though guides describe it as oriented toward B2B contacts, so people_search is true given it exposes individual contact details. Process per guide: search your name, open your profile, click Remove, fill a reason dropdown, and pass an 'I'm not a robot' checkbox CAPTCHA. CAPTCHA-gated -> guided tier. Not independently confirmed against the live site; last_verified left null and priority kept high rather than crucial since matches skew toward business/professional contact info rather than home-address people-search."
---

1. Go to [allpeople.com](https://allpeople.com) and search for your name (you can add city/state to narrow results).
2. Open the profile matching you and click "Details," then find and click the "Remove" (or similar) button on your profile page.
3. Select a reason for removal from the dropdown, add any needed details, and complete the "I'm not a robot" CAPTCHA checkbox.
4. Submit the removal request. Per third-party guides this typically clears within about 24 hours.
5. If you have more than one matching profile, repeat the search-and-remove steps for each one -- AllPeople does not appear to offer a single request that covers every listing.
