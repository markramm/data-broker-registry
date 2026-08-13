---
id: crunchbase-com
name: Crunchbase
domain: crunchbase.com
category: people_search
people_search: true
tier: assisted
priority: high
method: form
opt_out_url: "<verify: locate Crunchbase's current 'delete my person profile' / CCPA opt-out request form URL -- support articles reference a form but the exact live URL was not directly rendered>"
opt_out_email: "privacy@crunchbase.com"
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
notes: "WebSearch of Crunchbase's own support-center articles ('Who does the CCPA affect?', 'Do Not Sell Rights under CCPA') confirms Crunchbase publishes public 'person profiles' (name, role, company affiliations, sometimes contact info) sourced in part from public records and third parties, and offers a form to request deletion of your person profile as their CCPA 'do not sell' mechanism -- functionally a people-search/professional-profile data broker, since profiles are compiled about individuals (often without their direct involvement) and displayed/sold via their API. Crunchbase's support article explicitly frames a deletion request as opting out of sale. The exact current form URL could not be directly rendered (privacy/us-residents page returned HTTP 403), so opt_out_url is left as a <verify:> placeholder; last_verified is null. privacy@crunchbase.com is Crunchbase's general privacy contact and is offered as a fallback channel pending confirmation of the dedicated form."
---

1. Search your name on crunchbase.com and locate any "person profile" matching you.
2. Go to Crunchbase's Support Center and look for the article "Do Not Sell Rights under CCPA" (support.crunchbase.com), which links to the current deletion-request form for person profiles.
3. Complete the form with your name and the URL of your Crunchbase profile, and submit it as a request to delete your person profile / opt out of sale.
4. Note that submitting this request will remove your profile from Crunchbase's site, API, and any products built on it -- you will no longer be discoverable via Crunchbase search.
5. If you can't locate the form, email privacy@crunchbase.com directly, reference CCPA "do not sell" / deletion of your person profile, and include your profile URL.
6. Watch for a confirmation email and respond if identity verification is requested.
