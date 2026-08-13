---
id: arity-com
name: "Arity 875, LLC"
domain: arity.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://arity.com/yourprivacychoices/"
opt_out_email: "privacy@arity.com"
phone: "1-800-654-1412"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, phone]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch confirmed Arity (an Allstate subsidiary; telematics/mobility-data company collecting driving behavior and location data via mobile apps and connected cars, used for insurance risk-scoring and advertising) states 'We do not sell personal information for monetary value' while still offering an opt-out of targeted-advertising 'sharing' at arity.com/yourprivacychoices/ and a CA notice-at-collection page. The opt-out form itself matches records via hashed email address or phone number, or a mobile ad ID (MAID) via the DAA AppChoices app; language references 'verifying your name and email address' for some requests. No SSN/gov-ID/CAPTCHA/fee found in the fetched text. Because it's a webform without CAPTCHA or ID gating, classified assisted rather than guided. last_verified left null -- process reconstructed from fetched privacy-choices/notice-at-collection pages, not a live end-to-end run of the form."
---

1. Go to Arity's privacy choices page at https://arity.com/yourprivacychoices/.
2. Follow the form's instructions to opt out of targeted-advertising data sharing, providing your email address and/or phone number so Arity can match your record (it uses hashed versions of these, not raw values, to find your profile).
3. If you want to opt out at the mobile-device level (advertising ID used by apps that share data with Arity), use the Digital Advertising Alliance's AppChoices app instead, following Arity's linked instructions.
4. Alternatively, email privacy@arity.com or call 1-800-654-1412 to request opt-out or deletion directly.
5. If a request is denied, Arity provides a separate appeals webform -- check the privacy choices page for the current link.
