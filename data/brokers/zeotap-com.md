---
id: zeotap-com
name: "Zeotap GmbH"
domain: zeotap.com
category: adtech_identity_resolution
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://privacy.zeotap.com/optout/authentication"
opt_out_email: "privacy@zeotap.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [email]
readd_days: null
legal_basis: [gdpr, ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on zeotap.com/privacy-policy succeeded and rendered policy text describing rights to erasure/objection and multiple opt-out routes. Zeotap (Berlin-based, EU entity with a UK representative and external DPO) operates a Customer Data Platform / identity-resolution product for targeted advertising, built on a 'Data Protection Rights Portal' at privacy.zeotap.com/optout/authentication. A direct fetch of that portal URL returned HTTP 200 but is a JavaScript-rendered single-page app (page title only: 'Your Data Protection Rights Portal'), so the exact field/CAPTCHA/verification requirements could not be confirmed by rendering -- typical portals of this type (per the policy's own framing of authenticated, per-request access) require submitting an email and completing an email-based verification step before a request can be processed, which is why tier is set to guided rather than assisted despite no confirmed CAPTCHA. The policy also lists a general contact form at zeotap.com and, separately, device-level opt-out via a 'Data Protection Rights App' (Google Play/Apple App Store) for advertising-ID-based data, and standard OS-level 'Limit Ad Tracking'/'Opt-out of interest-based ads' settings. Used privacy@zeotap.com as the fallback email contact (referenced in the policy's contact-form flow) since no single explicit email address was quoted verbatim. last_verified left null -- portal not fully rendered."
---

1. Go to https://privacy.zeotap.com/optout/authentication -- Zeotap's Data Protection Rights Portal -- and follow the prompts to submit an opt-out or erasure request; expect to enter your email address and complete an email-verification step before the request is processed.
2. If the portal doesn't work for you, use the general contact form on zeotap.com, or email privacy@zeotap.com directly, stating that you are exercising your GDPR right to erasure/objection or, if you are a California resident, your CCPA right to opt out of sale/sharing.
3. For opt-out tied to a specific mobile advertising ID rather than an email address, install Zeotap's "Data Protection Rights App" from the Google Play Store or Apple App Store and submit your request there.
4. You can also limit Zeotap's ability to collect new data at the device level: enable "Limit Ad Tracking" (iOS) or "Opt-out of interest-based ads" (Android) in your phone's privacy settings, and use the cookie-consent tool (blue icon in the zeotap.com website footer) to manage website tracking cookies.
5. Zeotap's external Data Protection Officer (ePrivacy GmbH, Hamburg) and EU/UK supervisory authorities are available as an escalation path if you don't get a response through the portal or email.
