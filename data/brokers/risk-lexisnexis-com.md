---
id: risk-lexisnexis-com
name: "LexisNexis Risk Solutions -- Consumer Disclosure & Opt-Out Portal"
domain: risk.lexisnexis.com
category: risk_and_identity_data
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://consumer.risk.lexisnexis.com/request"
opt_out_email: null
phone: null
captcha: false
id_required: true
phone_required: false
charges_fee: false
required_fields: [full_name, address, dob, ssn, gov_id]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "risk.lexisnexis.com is the B2B-facing marketing site for LexisNexis Risk Solutions (fraud/identity/compliance data products for enterprise customers); its footer's 'Your Privacy Choices' link routes to a distinct consumer-facing portal at consumer.risk.lexisnexis.com, which is the same underlying system SageStream LLC (sagestreamllc.com, also in this batch, now part of LexisNexis Risk Solutions) points to. WebFetch on consumer.risk.lexisnexis.com/request confirmed a Consumer Disclosure Request form requiring first/last name, street address, city, zip, DOB, plus at least one of SSN or driver's license number+state; California residents can additionally choose Full Opt-Out, Partial Opt-Out (allows professional-data sales only), Opt-In, Limit Use of Sensitive PI, or Delete. Response is by U.S. Mail with an access code, not instant online. This is distinct from the existing lexisnexis-com.md entry (which points to www.lexisnexis.com/privacy/for-consumers/opt-out-of-lexisnexis.aspx, a lighter-weight suppression form) -- risk.lexisnexis.com/consumer.risk.lexisnexis.com is LexisNexis Risk Solutions' identity-verification/FCRA-adjacent consumer-report arm specifically, with a heavier ID-verification bar (SSN or driver's license required) reflecting its role in credit/insurance/identity data, not general marketing data. Kept as a separate entry given the distinct product, portal, and verification requirements. gov_id/ssn required_fields correctly trigger the sensitive-data guardrail. last_verified left null; captcha not observed but not exhaustively tested."
---

1. Go to the LexisNexis Risk Solutions consumer request portal at https://consumer.risk.lexisnexis.com/request.
2. Select the request type you want: a Consumer Disclosure Report, a CCPA-style Opt-Out (Full or Partial), Opt-In, Limit Use of Sensitive Personal Information, or Delete Personal Information (California residents get the fullest menu of these options).
3. Complete the required identifying fields: first name, last name, street address, city, ZIP code, and date of birth.
4. Provide at least one strong identifier: either your Social Security number, or your driver's license number plus issuing state. This step is mandatory -- the request cannot be submitted without it.
5. Optionally add middle name, suffix, phone, and email; note that including email may broaden which records are matched to you.
6. Submit the form. LexisNexis Risk Solutions verifies identity and mails a paper letter containing an access code to your address on file, in compliance with statutory response timeframes.
7. Use the mailed access code to log in and view your report or confirm your opt-out/deletion request was processed.
8. Remember this portal governs LexisNexis Risk Solutions' identity/credit/insurance-adjacent data (including data from affiliates like SageStream LLC) specifically -- it is separate from the general LexisNexis marketing-data suppression form at lexisnexis.com, so you may need to submit both if you want broader coverage.
