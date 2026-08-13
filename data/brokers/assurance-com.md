---
id: assurance-com
name: "Assurance IQ"
domain: assurance.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://assurance.com/ccpa-opt-out"
opt_out_email: null
phone: "1-844-311-6099"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Assurance IQ (a Prudential-owned insurance-lead marketing company) publishes a CCPA disclosure at assurance.com/ccpa-disclosure describing sale of personal information and a dedicated opt-out page at assurance.com/ccpa-opt-out (Data Request Form) plus a phone alternative at 1-844-311-6099, per its own disclosure page and corroborated by Privacy Rights Clearinghouse. Note: direct WebFetch to both assurance.com/ccpa-disclosure and assurance.com/ccpa-opt-out failed with 'certificate has expired' -- independently confirmed via curl -sv that assurance.com's TLS certificate is genuinely expired as of this research date, not a fetch-tool artifact. Could not verify exact form fields/CAPTCHA on the live page as a result; required_fields inferred conservatively from generic CCPA data-request-form norms. The CCPA disclosure notes exemptions for GLBA/HIPAA-covered financial/health data (Assurance sells life/health insurance leads), so some requests may be declined in part. last_verified left null; flagging the expired certificate as a real, currently observable problem with the broker's own site."
---

1. Go to the Assurance CCPA opt-out page at [assurance.com/ccpa-opt-out](https://assurance.com/ccpa-opt-out) and complete the Data Request Form with your name and email (note: as of this writing, assurance.com's SSL certificate has expired, which may trigger browser security warnings -- proceed with caution or use the phone option instead).
2. Alternatively, call 1-844-311-6099 and request that Assurance opt you out of the sale/sharing of your personal information under the CCPA.
3. Be aware Assurance states some categories of information (tied to insurance products you've actually purchased, covered by GLBA/HIPAA) may be exempt from the opt-out and processed anyway.
4. Watch for a confirmation of your request; if you don't receive one within a reasonable time, follow up by phone.
