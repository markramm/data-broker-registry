---
id: coleinformation-com
name: Cole Information
domain: coleinformation.com
category: marketing_data_broker
people_search: true
tier: assisted
priority: high
method: form
opt_out_url: "https://info.coleinformation.com/ccpa-opt-out"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, address, email, dob]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Cole Information is a registered CA data broker (registration 188251) that compiles and resells consumer household/contact records (name, address, phone) used for people-search and marketing lookups -- sold both to marketers and, per its product line, to background/skip-trace-adjacent buyers, so treated as people_search:true. WebSearch results (CA AG registration listing) give a CCPA opt-out form at info.coleinformation.com/ccpa-opt-out and a separate deletion-request contact at coleinformation.com/contact-us/; a curl DNS check for info.coleinformation.com failed to resolve in this session (ENOTFOUND) even though the base domain coleinformation.com resolves fine, so the exact opt-out subdomain could not be independently confirmed live -- flagged here rather than silently trusted. Typical guidance for this class of broker (per general opt-out-guide context) is entering DOB, address, and email; no CAPTCHA or ID-upload requirement was found in any source, so kept at assisted. Not freshly confirmed; last_verified left null."
---

1. Go to https://info.coleinformation.com/ccpa-opt-out (verify this subdomain resolves for you -- it did not resolve via direct DNS lookup during this research pass, so it may have moved; if it fails, use the contact form at https://www.coleinformation.com/contact-us/ instead and explicitly request a CCPA opt-out/deletion).
2. Complete the opt-out form with your full name, current address, email, and date of birth so Cole Information can match your record.
3. Submit the request and note any confirmation reference or email you receive.
4. If the dedicated opt-out page is unavailable, email or use the general contact form at coleinformation.com/contact-us/, state that you are exercising your CCPA right to opt out of sale and to delete your personal information, and include the identifying details above.
5. Allow the standard multi-day processing window typical of this class of broker; if you don't hear back, follow up citing the CCPA.
