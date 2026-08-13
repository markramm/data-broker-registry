---
id: taboola-com
name: Taboola
domain: taboola.com
category: adtech_content_recommendation
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://ccparequest.taboola.com/"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, other]
readd_days: null
legal_basis: [ccpa, cpra, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "Taboola is a major adtech/content-recommendation network (the 'around the web' widget boxes on news sites), not a people-search broker -- it profiles browsing behavior for ad targeting rather than reselling identity/address data. WebFetch on policies.taboola.com/privacy-policy/ confirmed section 5.2.1 points to a 'U.S. State Consumer Rights Portal' at https://ccparequest.taboola.com/ for CCPA/CPRA opt-out of sale/share and cross-context behavioral advertising; a separate accessrequest.taboola.com/access portal handles broader access/deletion requests. The request portal itself is a JS-rendered SPA that WebFetch could not render field-by-field, so exact form fields and CAPTCHA presence on that specific page are inferred from standard CCPA-portal patterns used across Taboola's stack, not directly observed -- treated as guided/captcha:true out of caution per the 'when in doubt, guided' rule. last_verified left null since the portal form itself wasn't directly confirmed."
---

1. Go to Taboola's U.S. State Consumer Rights Portal at https://ccparequest.taboola.com/.
2. Select the type of request (opt out of sale/share of personal information, or a broader access/deletion request).
3. Enter the requested identifying information (typically email address; some request types may ask for additional details) and submit.
4. Complete any CAPTCHA or identity-confirmation step the portal presents.
5. Watch for a confirmation email and follow any verification link it contains.
6. If you also want a full data access or deletion request (beyond opting out of sale/sharing), use the separate portal at https://accessrequest.taboola.com/access.
