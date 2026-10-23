---
id: l2political-com
name: "L2, Inc."
domain: l2political.com
category: voter_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://l2-data.com/optout1-667457/"
opt_out_email: "privacyrequests@l2political.com"
phone: "1-800-842-5478"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [full_name, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "l2political.com now 301-redirects (confirmed via WebFetch) to https://www.l2-data.com/ -- the company rebranded from L2 Political to L2 Data. L2 is a large-scale voter-file and consumer-data broker (217M voter records, 260M consumer records per their homepage) used for political targeting, comparable in scale/impact to i360. WebFetch confirmed a working opt-out form at l2-data.com/optout1-667457/ requiring first/last name, full address, and a consent checkbox, with a simple arithmetic CAPTCHA ('14 + 3 =') -- optional phone/email fields. A privacy policy PDF (L2-Privacy-Notice) and a dedicated California 'Do Not Sell My Personal Data' page were also referenced but not directly rendered. Alternate contacts: support@l2-data.com, info@l2-data.com, phone 1-800-842-5478; privacy companies seeking bulk opt-outs are directed to privacyrequests@l2political.com specifically. Because the form requires full name and home address and covers voter-file data (not just marketing lists), and CAPTCHA-gates submission, classified guided tier. Not classified people_search (no per-lookup identity/address resale product was found -- data is sold in bulk/targeting feeds to campaigns), but given the scale of address-level voter data and its use for political targeting, priority raised to high rather than standard. 2026-10-22 (daily maintainer, page-monitor issue #101): fetched https://l2-data.com/optout1-667457/ (HTTP 200). The form is unchanged (name, address, consent box, '14 + 3 =' math question) but its intro now reads: if you are a California resident, click a link to https://l2-data.com/california-privacy-rights-for-california-residents-only/; the form is for people who are not California residents. Fetched that page too (HTTP 200): a CCPA request form (email, name, phone, address with a California check, and a choice of rights). Opt-out of sale needs no identity verification and L2 says it deletes your data on receipt; access and deletion need verification via a ConsumerMapping login or an uploaded signed declaration (or power of attorney for an agent). The steps now route California residents there. Nothing was submitted; last_verified stays null."
---

1. If you don't live in California, go to https://l2-data.com/optout1-667457/ (the L2 Political opt-out form, now hosted under L2's rebranded l2-data.com site). California residents: skip to step 6.
2. Enter your first and last name and your full mailing address (street, city, state, ZIP) so L2 can locate your voter/consumer record.
3. Optionally add a phone number or email address.
4. Solve the simple math CAPTCHA (e.g. "14 + 3 =") and check the consent box confirming your identity.
5. Submit the form. L2 states it will remove your contact information "as soon as reasonably practicable."
6. If you live in California, L2 says this form is not for you. Use its California page instead: https://l2-data.com/california-privacy-rights-for-california-residents-only/. Fill in your email, name, phone and address (it checks that the address is in California), then choose the right you want. "Right to Opt-Out of Sale of Your Data" needs no identity check, and L2 says it deletes your data from its database when it gets one. "Right to Delete Your Data" needs identity verification: either an L2 ConsumerMapping login, or a signed declaration under penalty of perjury that you upload with the request. L2 says it won't delete data it uses for constitutionally protected political speech.
7. You can also email privacyrequests@l2political.com, support@l2-data.com or info@l2-data.com, or call 1-800-842-5478.
8. Keep a record of your submission; re-check periodically since voter files are refreshed from public records on an ongoing basis.
