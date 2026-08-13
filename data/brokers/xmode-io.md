---
id: xmode-io
name: "XMode / Outlogic"
domain: xmode.io
category: geolocation_data_broker
people_search: false
tier: guided
priority: crucial
method: form
opt_out_url: "https://outlogic.io/opt-out-form/"
opt_out_email: "privacy@outlogic.io"
phone: "1-866-346-9602"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [email, other]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "xmode.io itself is a live, resolving domain (Apache/PHP, DNS active) but every page tested (homepage, /privacy-policy, /xmode-privacy-policy-2/) returned HTTP 500 (broken WordPress backend) across repeated attempts -- the legacy X-Mode Social / XMode brand's own site is currently non-functional, not merely bot-blocked. However, xmode.io/privacy-policy was observed (before failing on retry) to be a live redirect notice pointing to 'xmode-privacy-policy-2', confirming the domain is still actively configured, not simply parked. X-Mode Social was the subject of well-documented 2020-2021 privacy scandals (selling precise mobile-location data harvested via SDKs embedded in apps including a Muslim prayer app, and reported sales to U.S. military/intelligence-linked buyers), leading Apple and Google to ban apps bundling its SDK. The company rebrand to 'Outlogic' (outlogic.io) is widely reported and matches the public history, though the Outlogic privacy policy itself does not explicitly name X-Mode/XMode as a prior brand. WebFetch on outlogic.io, outlogic.io/privacy-policy, and outlogic.io/opt-out-form/ all succeeded and rendered live content: Outlogic explicitly states it 'may sell your sensitive personal data' including precise geolocation, and describes itself as registered as a data broker in Texas. Given xmode.io's own infrastructure is broken, this entry routes the opt-out to Outlogic's confirmed-working form/email/phone -- treat this as the current operating entity behind the xmode.io domain/brand. Opt-out form requires an email and a device advertising/installation ID (mapped to required_fields as email + other); a validation/CAPTCHA-style field was present on the form. Given ongoing real-world precise-location tracking and documented safety-relevant scandals, priority is crucial per the batch's own guidance. last_verified left null -- xmode.io itself could not be rendered at all during this research pass."
---

1. xmode.io's own website is currently broken (returns a server error on every page as of this research), but the underlying business continues to operate under the name Outlogic at outlogic.io -- use Outlogic's channels below.
2. Find your device's Advertising ID (iOS: Settings > Privacy & Security > Tracking / Apple Advertising; Android: Settings > Privacy > Ads) or an app Installation ID, since Outlogic's opt-out process is keyed to device identifiers rather than your name.
3. Go to https://outlogic.io/opt-out-form/ and submit the form with your email address and device Advertising ID or Installation ID (a phone number field is optional). Complete the validation step shown on the form.
4. Alternatively, email privacy@outlogic.io with the subject line "Data Transfer Opt out," including your device ID, or call the company's toll-free line at 1-866-346-9602.
5. Because this data is collected per-device via SDKs embedded in other apps (not a public profile you can search), there is no single "listing" to point to -- repeat this process for each device/advertising ID you use, and be aware that resetting your device's advertising ID in the future will require submitting a new opt-out for the new ID.
6. If you know or suspect a specific app shared your location data with X-Mode/XMode/Outlogic in the past, consider uninstalling that app or revoking its location permission in addition to filing the opt-out.
