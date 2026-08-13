---
id: revealmobile-com
name: "Reveal Mobile"
domain: revealmobile.com
category: location_data_broker
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://www.revealmobile.com/privacy-form"
opt_out_email: "privacy@revealmobile.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [other]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Fetched revealmobile.com/privacy-policy. Reveal Mobile is a mobile-location-data company that collects device advertising identifiers (IDFA/Android Advertiser ID) via apps and sells/shares location data with advertisers. Policy describes a dedicated privacy-request form at /privacy-form for all US consumers to access, delete, or opt out of sale of their data, plus a direct email (privacy@revealmobile.com) where consumers can request removal by providing their device's IDFA or Android Advertiser ID. Policy also notes that disabling ad tracking at the OS level automatically stops collection. No CAPTCHA or ID requirement described. Company self-reported only 19 opt-out requests in 2024 with a 26-day median response time, suggesting the process is real but slow. required_fields set to [other] since the identifying value needed is a device advertising ID, not a field in the schema's enum. High priority: real opt-out from a genuine location-data broker, not a people-search/address site."
---

1. Go to the [Reveal Mobile privacy request form](https://www.revealmobile.com/privacy-form).
2. Follow the form's instructions to submit an access, deletion, or opt-out-of-sale request for your data.
3. Alternatively, email privacy@revealmobile.com directly with your device's advertising identifier -- the IDFA (Identifier for Advertisers) on iPhone, or the Advertiser ID on Android -- which you can find in your device's privacy/ads settings.
4. As an additional step, disable ad tracking/personalized ads at the operating-system level on your phone or tablet; Reveal Mobile states this automatically stops it from collecting or storing data about that device.
5. Allow time for a response -- Reveal Mobile has reported response times averaging several weeks, and its 2024 transparency disclosure cites a median response time of 26 days.
