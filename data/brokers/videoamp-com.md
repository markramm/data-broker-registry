---
id: videoamp-com
name: "VideoAmp"
domain: videoamp.com
category: adtech
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://videoamp.com/your-privacy-choices/"
opt_out_email: "privacy@videoamp.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: ["email"]
readd_days: null
legal_basis: ["ccpa", "cpra"]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on VideoAmp's privacy policy surfaced a 'Your Privacy Choices' page (confirmed live via direct fetch -- it loads a Ketch consent-management widget, JS-rendered so not readable by curl/WebFetch text extraction) plus a separate bidr.io ad-platform opt-out cookie endpoint and a privacy@ contact email. VideoAmp is a TV/cross-platform measurement and advertising company (adtech), not a people-search site. Marked assisted rather than guided since the visible mechanism is a standard consent-preferences widget, not a CAPTCHA/ID-gated process, though the JS-rendered form could not be fully inspected. last_verified left null since the widget's actual fields were not directly observed."
---

1. Go to VideoAmp's [Your Privacy Choices page](https://videoamp.com/your-privacy-choices/) and use the consent-preferences widget to opt out of data sale/sharing and targeted advertising.
2. For cookie-based ad-targeting opt-out specifically, VideoAmp's policy also references an opt-out endpoint at optout.prod.bidr.io -- note this is device- and browser-specific, so repeat it on each browser/device you use.
3. If the widget doesn't resolve your request, email privacy@videoamp.com directly with your name and email address and ask to opt out of sale/sharing and to delete your data.
4. Sending a Global Privacy Control (GPC) signal from a supporting browser/extension may also register as an automatic opt-out under VideoAmp's policy.
