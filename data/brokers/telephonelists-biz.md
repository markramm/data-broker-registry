---
id: telephonelists-biz
name: TelephoneLists.biz
domain: telephonelists.biz
category: telemarketing_list_broker
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "<verify: exact 'Do not sell my Personal Info' footer link URL on telephonelists.biz>"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on telephonelists.biz described a B2B/telemarketing contact-list seller (189M US/Canada consumer and business records sold via subscription portal or bulk state files, $99-1499/mo or $549/state) -- not an individual-lookup people-search site, so people_search:false and standard priority given the primarily B2B commercial-list nature, though it does sell consumer records too. The page reported a 'Privacy Policy' at /privacy-policy-of-telephonelists-biz, a 'California Privacy Notice' at /privacy-notice-for-residents-of-california, and a 'Do not sell my Personal Info' footer link, plus optional DNC-registry scrubbing before download. I was not able to independently WebFetch the privacy-policy or opt-out pages themselves to confirm the exact opt-out URL, so opt_out_url is left as a verify-placeholder pending direct confirmation; last_verified is null per the placeholder rule."
---

1. Go to telephonelists.biz and open the "Do not sell my Personal Info" link in the site footer.
2. Also review the "Privacy Policy" (at /privacy-policy-of-telephonelists-biz) and "California Privacy Notice" (at /privacy-notice-for-residents-of-california) for the current opt-out mechanism, since the exact form has not yet been independently confirmed.
3. Provide your full name and email address (and any other identifying details requested) to submit an opt-out/do-not-sell request.
4. Submit the request and watch for a confirmation email.
5. Note: this site primarily sells bulk telemarketing/contact lists rather than running individual lookups, so if you find yourself in one of its list products, ask the opt-out process to explicitly confirm suppression from future list pulls, not just removal of a single record.
