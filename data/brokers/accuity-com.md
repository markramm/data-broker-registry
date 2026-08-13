---
id: accuity-com
name: Accuity Inc. (LexisNexis Risk Solutions)
domain: accuity.com
category: identity_verification
people_search: false
tier: guided
priority: standard
method: portal
opt_out_url: "https://consumer.risk.lexisnexis.com/california"
opt_out_email: "consumer.documents@lexisnexis.com"
phone: "1-888-217-1591"
captcha: false
id_required: true
phone_required: false
charges_fee: false
verification: id_upload
required_fields: [full_name, address, dob, gov_id]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "accuity.com/privacy-policy/ redirects (301) to risk.lexisnexis.com/financial-services/financial-crime-compliance -- Accuity is a LexisNexis Risk Solutions subsidiary providing bank KYC/AML/sanctions-screening data (B2B financial-crime compliance), not a consumer-facing people-search product. Registered as a CA data broker (oag.ca.gov/data-broker/registration/562391) and consumer requests route through the shared LexisNexis Risk consumer portal at consumer.risk.lexisnexis.com/california, which per WebFetch is a landing page describing online-form, mail, and phone (1-888-217-1591) options but did not itself expose the actual form fields/CAPTCHA -- LexisNexis's consumer-report products are known to require identity verification (name/address/DOB/last-4-SSN or ID) for access/deletion requests, hence id_required true and guided tier. Financial-compliance data broker, not people-search -- standard priority."
---

1. Go to https://consumer.risk.lexisnexis.com/california.
2. Choose the online request option (or download the mail-in form, or call 1-888-217-1591).
3. Complete the identity-verification steps LexisNexis requires -- typically full name, address, date of birth, and possibly a government ID -- since this affects consumer-report-adjacent financial data.
4. Submit your request to opt out of sale/sharing and/or request access or deletion under the CCPA.
5. Alternatively, email consumer.documents@lexisnexis.com or write to: Consumer Center, Attn: CCPA Request, P.O. Box 105108, Atlanta, GA 30348-5295.
6. Allow up to 45 days for LexisNexis to process the request.
