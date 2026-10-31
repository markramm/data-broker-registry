---
id: outlogic-io
name: "Outlogic, LLC"
domain: outlogic.io
category: location_data_broker
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://outlogic.io/opt-out-form/"
opt_out_email: "privacy@outlogic.io"
phone: "+1 (866) 346-9602"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [email, other]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-10-31 by the daily maintainer from California's data broker registry (Outlogic, LLC; rights URLs https://outlogic.io/opt-out-form/ and https://outlogic.io/privacy-policy/). The opt-out page (curl and WebFetch, HTTP 200; rendered in headless Chromium) covers Outlogic's collection, use and sale of personal information, 'including data that may reveal your device's precise geographic location'; its Texas notice says 'We may sell your sensitive personal data', including precise latitude/longitude of a mobile device. The opt-out form (Gravity Forms) requires a Device ID (advertising ID or installation ID) and an email; a third text input is a hidden honeypot. No CAPTCHA widget or script was found. Deletion is not on the form: the page says to request it by email or phone, also with a Device ID. It also notes that turning off iOS 'Allow apps to request to track' does not stop collection by itself, and that on Android 12+ a deleted (zeroed) advertising ID can't be matched to data already collected, so submit the opt-out before resetting or deleting it. The page doesn't name a parent company and no processing time is stated. Priority high: precise device location data. Nothing was submitted; last_verified null."
---

1. Find your phone's advertising ID before changing any ad settings. On Android it is under Settings > Google > Ads. Don't delete or reset it first: Outlogic says it can't match a zeroed-out ID to data it already has. An app's privacy settings screen may also show an "installation ID", which the form accepts too.
2. Go to https://outlogic.io/opt-out-form/.
3. Enter the Device ID and your email address, and submit. Repeat for each device.
4. To have the data deleted as well, email privacy@outlogic.io or call +1 (866) 346-9602 and ask for deletion, giving the same Device ID.
5. On iPhone, turning off "Allow Apps to Request to Track" helps going forward, but Outlogic says you still need to submit the opt-out.
