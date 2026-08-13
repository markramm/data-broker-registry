---
id: backgroundchecks-com
name: Backgroundchecks.com LLC
domain: backgroundchecks.com
category: background_check
people_search: true
tier: guided
priority: crucial
method: email
opt_out_url: "https://www.backgroundchecks.com/privacypolicy"
opt_out_email: "info@backgroundchecks.com"
phone: null
captcha: false
id_required: true
phone_required: false
charges_fee: false
verification: id_upload
required_fields: [full_name, address, email, phone, gov_id]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on backgroundchecks.com/privacypolicy rendered directly and confirmed the CCPA process: email info@backgroundchecks.com with full name, all physical addresses on file, all email addresses, all phone numbers, all employers, and a legible image of a government-issued ID showing a California address. The policy itself notes the CCPA does not strictly apply to their FCRA-governed background-screening business, but they operate this opt-out mechanism anyway. Government-ID requirement pushes this to guided tier despite the plain-email method (method:email normally implies auto, but the id_required gate overrides that here). Background-check broker reselling records on named individuals -> people_search true, crucial priority."
---

1. Email info@backgroundchecks.com stating you are exercising your CCPA right to opt out of the sale/sharing of your personal information (and/or requesting deletion).
2. In the same email, include: your full name, every physical address associated with your record, every email address on file, every phone number on file, and every employer listed.
3. Attach a legible image of a government-issued ID showing your California address -- Backgroundchecks.com requires this to verify your identity before acting on the request.
4. If your concern is about the accuracy of an FCRA background-check report rather than a CCPA sale opt-out, use their disputes page at backgroundchecks.com/disputes instead, which follows FCRA dispute procedures.
5. Keep a copy of your email and ID submission for your records, and follow up if you don't receive confirmation within a reasonable time.
