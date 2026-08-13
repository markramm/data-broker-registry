---
id: maxmind-com
name: MaxMind, Inc.
domain: maxmind.com
category: ip_geolocation_data_broker
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://www.maxmind.com/en/opt-out"
opt_out_email: "privacy@maxmind.com"
phone: "1-844-802-0220"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [email, other]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirmed via direct curl of maxmind.com/en/privacy-policy and maxmind.com/en/opt-out. MaxMind sells IP-address geolocation and fraud-risk intelligence (GeoIP, minFraud) that associates IP addresses with approximate location -- a data-broker product, but its own policy states the data 'never identifies a household or street address' and location points are deliberately offset to a public place within a 5km+ radius (its 'Safe Coordinates' program), which is why priority is standard rather than crucial despite being a genuine data reseller. The opt-out form (/en/opt-out) has fields request_type/description/confirm_opt_out/csrf_token and no CAPTCHA markup found in the rendered HTML -> assisted tier. Also documented: a GeoIP data-correction request page (/en/geoip-data-correction-request) for correcting an inaccurate location association, and a Nevada-specific do-not-sell page (/en/nevada-do-not-sell). privacy@maxmind.com is used for Oregon/Minnesota third-party-disclosure-list requests per the policy text; a Nevada-specific contact (nevada-privacy@maxmind.com) also exists. last_verified left null since the form was read via curl, not manually submitted/rendered with JS."
---

1. Go to https://www.maxmind.com/en/opt-out.
2. Select the applicable request type (e.g., "Do Not Sell/Share My Personal Information") and fill in the description field explaining you want your data excluded from MaxMind's IP-intelligence products.
3. Note MaxMind's own warning: opting out may interfere with services (e.g., fraud-prevention checks) that rely on their IP data when you interact with sites that use MaxMind.
4. Submit the form; no CAPTCHA or ID upload was found on this page as rendered.
5. Separately, if you want an inaccurate location tied to your IP address corrected rather than opted out entirely, use https://www.maxmind.com/en/geoip-data-correction-request instead.
6. For Nevada-specific do-not-sell requests, use https://www.maxmind.com/en/nevada-do-not-sell or email nevada-privacy@maxmind.com; for Oregon/Minnesota third-party-disclosure-list requests, email privacy@maxmind.com. You can also call 1-844-802-0220.
7. Allow up to 45 days for MaxMind to process the request.
