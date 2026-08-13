---
id: mobilewalla-com
name: Mobilewalla, Inc.
domain: mobilewalla.com
category: location_ad_data_broker
people_search: false
tier: auto
priority: high
method: email
opt_out_url: "https://www.mobilewalla.com/california-residents-do-not-sell-my-personal-information"
opt_out_email: "CCPACompliance@mobilewalla.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [email]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on mobilewalla.com/privacy-policy and the CA-residents opt-out page confirmed Mobilewalla is a location/mobile-ad-tech data broker ('Vertical AI' consumer intelligence platform selling location and behavioral data to telecom/finance/retail/travel/media clients). The CA-residents page offers both a 'Personal Information Requests Form' (linked at /global-opt-out-request) and a direct email, CCPACompliance@mobilewalla.com, matching the legacy CSV's contact exactly. Because a direct opt-out email is confirmed live and no CAPTCHA/ID/phone gate was found for the email channel, this is tier:auto via method:email per the schema's tier-derivation rule, even though a form alternative also exists. Not people-search (they don't sell individual identity lookups directly to consumers), but real ad-tech/location data on individuals -> high priority."
---

1. Email CCPACompliance@mobilewalla.com and state that you are a California (or other applicable state) resident exercising your right to opt out of the sale/sharing of your personal information, and request deletion if desired.
2. Include the email address associated with any accounts or the general contact email you want covered by the request.
3. Alternatively, use the "Personal Information Requests Form" linked from https://www.mobilewalla.com/california-residents-do-not-sell-my-personal-information if you prefer a web form over email.
4. Watch for a confirmation reply from Mobilewalla acknowledging your request.
