---
id: apollo-io
name: Apollo.io
domain: apollo.io
category: marketing_data_broker
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://www.apollo.io/privacy-policy/remove"
opt_out_email: "privacy@apollo.io"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch confirmed Apollo's CCPA privacy statement and removal page describe a 'Contributor Database' of B2B contact data (work emails, phone numbers, job titles) that Apollo sells to customers for sales/marketing/recruiting, with an explicit right-to-opt-out-of-sale section pointing to the Removal Page in the Privacy Center or privacy@apollo.io. The removal form itself asks only for a business email address -- no name/address/DOB/SSN, no CAPTCHA mentioned in the fetched text. This is B2B professional-contact data rather than consumer people-search data, so people_search is false and priority is high rather than crucial; single-field form with no CAPTCHA/ID gating keeps it at assisted tier. Not independently rendered live -- last_verified left null."
---

1. Go to the Apollo.io removal page at https://www.apollo.io/privacy-policy/remove (part of Apollo's Privacy Center).
2. Enter the business/work email address you want removed from Apollo's Contributor Database.
3. Submit the form to request opt-out of sale/sharing of that contact record.
4. Alternatively, email privacy@apollo.io directly with the work email address(es) you want removed, referencing your CCPA/CPRA right to opt out of sale.
5. If you have multiple work email addresses tied to past employers, repeat separately for each one.
