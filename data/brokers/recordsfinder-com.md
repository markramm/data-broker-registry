---
id: recordsfinder-com
name: "RecordsFinder"
domain: recordsfinder.com
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://recordsfinder.com/optout/"
opt_out_email: "privacy@recordsfinder.com"
phone: "800-433-0567"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, address]
readd_days: null
legal_basis: [ccpa, cpra, vcdpa, cdpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Directly fetched recordsfinder.com/optout/ (HTTP 200). Page is a people-search opt-out form requiring first name, last name, state (required) and city (optional) -- no CAPTCHA, ID, or phone visible in the fetched HTML, so assisted rather than guided. Separate email path (privacy@recordsfinder.com) exists specifically for 'Covered Person' removal under the Daniel Anderl Judicial Security and Privacy Act (judges/prosecutors/law enforcement and household members), not for general public opt-outs, so method is form (general case) not email. Page also references a broader data-subject-rights form at members.recordsfinder.com/privacyform for residents of listed states. last_verified left null since this was a single-session automated fetch, not a rendered/interactive confirmation."
---

1. Go to the [RecordsFinder opt-out page](https://recordsfinder.com/optout/).
2. Enter your first name, last name, and state (required); city is optional but narrows the search.
3. Submit the form and review the matching record(s) returned.
4. Follow the on-page instructions to request removal of the record(s) that match you.
5. If you are a judge, prosecutor, law enforcement officer, or immediate household member of one, you may instead email privacy@recordsfinder.com with your full name, residence, email address, and covered-person status, using the subject line "Attention Covered Person Removal Request."
6. For broader state-law data rights (access, deletion, correction, opt-out of sale/sharing), use the linked data-subject-rights form referenced on the opt-out page if you are a resident of a covered state.
7. Re-check periodically, since people-search listings can reappear after new data pulls.
