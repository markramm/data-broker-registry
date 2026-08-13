---
id: usmarketinggrp-com
name: "US Marketing Group"
domain: usmarketinggrp.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "<verify: exact CCPA opt-out page/form URL on usmarketinggrp.com -- main site and /ccpa returned errors on fetch>"
opt_out_email: "privacy@usmarketinggrp.com"
phone: "866-581-4810"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: identity_confirmation
required_fields: [full_name, email, address, phone]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on the homepage and privacy policy confirms US Marketing Group provides 'live and aged leads, affiliate and aggregator services, marketing lists, opt in email marketing, data append, telephone append and customer database hygiene' across mortgage/solar/insurance/roofing/home-services verticals -- consistent with data-broker/lead-aggregator functions even though the site doesn't use that exact label. The privacy policy (fetched) describes an opt-out form embedded on the privacy-policy page itself requiring name, address, phone, email, and identity confirmation, plus email privacy@usmarketinggrp.com and phone 866-581-4810 ext 102, with ~30-day compliance and a 12-month wait before reauthorization requests. A direct WebFetch attempt on usmarketinggrp.com/ccpa 404'd, so the exact live opt-out page URL is unconfirmed -- opt_out_url is left as a verify placeholder and last_verified is null accordingly. Lead-generation/marketing list company rather than a consumer people-search tool -> people_search false; smaller-scale lead broker rather than a major aggregator -> priority standard. Because the form requires 'identity confirmation' beyond just name/email, tier is assisted rather than auto."
---

1. Go to the US Marketing Group privacy policy page (linked from the site footer) and locate the embedded "Do Not Sell My Info" / CCPA opt-out form -- confirm the exact current URL, since a direct guess at /ccpa did not resolve.
2. Fill in your full name, mailing address, phone number, and email address, and complete any identity-confirmation step the form requests.
3. Submit the form.
4. If you cannot locate or load the form, email privacy@usmarketinggrp.com directly and state you are submitting a CCPA opt-out/do-not-sell request, including your name, address, phone, and email.
5. Alternatively, call 866-581-4810 ext. 102 to make the same request by phone, or mail a written request to: US Marketing Group, 3639 Harbor Blvd #212, Ventura, CA 93001.
6. Expect a response within about 30 days; the company states it will not act on repeat/reauthorization requests within 12 months of a prior request.
