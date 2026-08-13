---
id: nexxagroup-com
name: "Nexxa Group, Inc."
domain: nexxagroup.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://www.nexxagroup.com/corporate-overview/consumer-opt-out/"
opt_out_email: null
phone: "8005661895"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirmed via curl fetch of nexxagroup.com/corporate-overview/consumer-opt-out/ (HTTP 200, rendered directly). Nexxa Group is a data intelligence / marketing-compliance company (energy solutions, consumer/business marketing lists, identity verification, fraud prevention, 'National Business File', 'New Movers' data). The page confirms a dedicated 'Consumer Opt Out Request' online form: requires a valid email address (a confirmation email is sent to validate the request; the site explicitly states opt-out requests sent via plain email will NOT be processed, only the form or phone). No CAPTCHA markup found in the fetched HTML. Alternative channel: phone (800) 566-1895 for consumers without a valid email address. people_search left false (B2B/consumer marketing data, not general identity/address lookup); priority:standard as a mid-size marketing-data vendor. opt_out_email left null per the site's own instruction that email-only requests aren't honored -- method is the form (or phone), not direct email. last_verified left null despite the direct fetch since the form's exact field list wasn't fully machine-readable (likely JS-rendered)."
---

1. Go to https://www.nexxagroup.com/corporate-overview/consumer-opt-out/ and locate the "Consumer Opt Out Request" form.
2. Fill in your full name and a valid email address, then submit the request. Note: Nexxa explicitly states that opt-out requests sent via plain email are NOT processed -- you must use this form (or call).
3. Check your email for a confirmation message and complete any confirmation step it requires; your opt-out is not final until you confirm.
4. If you don't have a valid email address, call (800) 566-1895 to submit your opt-out request by phone instead.
5. Note this opt-out does not remove data already provided to marketers before your request; expect the standard CCPA-style processing window.
