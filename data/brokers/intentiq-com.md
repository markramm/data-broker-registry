---
id: intentiq-com
name: Intent IQ LLC
domain: intentiq.com
category: adtech_identity
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.intentiq.com/opt-out/"
opt_out_email: "privacy@intentiq.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on intentiq.com and intentiq.com/opt-out/ succeeded and rendered live content. Intent IQ is an ad-tech identity-resolution/cookieless-audience company (not a people-search site) that describes itself as able to 'opt-out of the selling, sharing or targeted advertising with the personal information that we possess.' The opt-out page offers a browser-cookie opt-out button, a mobile-device opt-out, and an email option to privacy@intentiq.com (matches the legacy CSV contact). Because the primary mechanism is a portal with per-browser/per-device buttons rather than a single universal email fix (the page itself warns users must repeat the process on every browser/device), classified as method:form / tier:guided rather than tier:auto, even though an email path exists. No CAPTCHA or ID requirement observed on the opt-out page content returned. people_search:false because this is an advertising identity/data-matching company, not an individual-lookup reseller."
---

1. Go to https://www.intentiq.com/opt-out/ (the "Your Privacy Choices" page).
2. Click the browser/cookie opt-out button to stop sale/sharing and targeted advertising tied to your browser's identifiers, and use the mobile opt-out option if you also want to cover a phone or tablet.
3. Because Intent IQ's matching works per browser and per device, repeat step 2 on every browser (Chrome, Safari, Firefox, etc.) and every device you use.
4. If you'd rather not use the button flow, or want to request deletion of information already collected, email privacy@intentiq.com directly with your opt-out/deletion request.
5. Note that Intent IQ also does some "probabilistic" matching across devices on the same network, so an opt-out on one device may not fully cover others sharing your network -- re-check periodically.
