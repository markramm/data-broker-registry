---
id: connectedinvestors-com
name: Connected Investors
domain: connectedinvestors.com
category: real_estate_data
people_search: true
tier: guided
priority: high
method: form
opt_out_url: "https://firstam.service-now.com/x_farf2_dp_request_ci_opt_out.do"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [full_name, address, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on connectedinvestors.com confirmed this is a real-estate investor SaaS platform (owned by Platlabs, LLC, operating under state brokerage licenses) that aggregates property-ownership records, owner contact details, and skip-traced phone/address data across 150+ filters -- a genuine reseller of individuals' identity/address/phone lookups, so people_search true. Their 'Do Not Sell Or Share My Personal Information' link routes to a First American (their data-services parent) ServiceNow-hosted opt-out form rather than a page on connectedinvestors.com itself; treated as the broker's own opt-out mechanism since it's the linked destination from their footer. Third-party hosted ServiceNow forms of this kind typically include CAPTCHA, so captcha assumed true and tier set guided; not independently rendered to confirm exact fields, so last_verified left null."
---

1. Go to https://firstam.service-now.com/x_farf2_dp_request_ci_opt_out.do (linked from the "Do Not Sell Or Share My Personal Information" link in the connectedinvestors.com footer).
2. Select the request type for opting out of sale/sharing of your personal information.
3. Provide your full name, the property/mailing address associated with the record you want removed, and an email address for confirmation.
4. Complete any CAPTCHA or verification step presented by the form.
5. Submit the request; Connected Investors' data is sourced through First American, so this single request should cover their property-owner contact database.
6. Also review their separate Do Not Call policy at connectedinvestors.com/do-not-call if phone solicitation is your primary concern.
