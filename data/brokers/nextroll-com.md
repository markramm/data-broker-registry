---
id: nextroll-com
name: "NextRoll, Inc."
domain: nextroll.com
category: adtech_data_broker
people_search: false
tier: assisted
priority: standard
method: portal
opt_out_url: "https://app.adroll.com/optout/email"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "NextRoll operates AdRoll (D2C e-commerce retargeting/ad marketing) and RollWorks (B2B account-based marketing) -- an ad-tech company that collects and uses cookie/device data for cross-channel ad targeting. WebFetch of nextroll.com/privacy directly hit a TLS certificate mismatch in this session; content summarized from search-engine snippets referencing the site instead. Confirmed opt-out mechanism: a dedicated 'Do Not Sell or Share My Personal Information' page at app.adroll.com/optout/email, plus automatic honoring of Global Privacy Control (GPC) browser signals and a browser-based opt-out (app.adroll.com/optout/safari for Safari's ITP handling). No ID or phone required per the summarized privacy policy language; opt-out relies primarily on browser/cookie-based signals rather than an identity-verification flow. people_search left false (ad-tech targeting data, not identity/address resale). Classified assisted (self-serve web form/portal, no CAPTCHA/ID found) rather than auto since it isn't a plain email address. last_verified left null since the primary source was a search summary, not a directly rendered page."
---

1. Go to https://app.adroll.com/optout/email and submit the "Do Not Sell or Share My Personal Information" request with your email address.
2. Alternatively, enable Global Privacy Control (GPC) in your browser (many privacy-focused browsers and extensions support this) -- NextRoll states it automatically honors GPC signals for opt-out purposes.
3. If you use Safari, note NextRoll also provides a browser-specific opt-out flow at https://app.adroll.com/optout/safari to work around Safari's Intelligent Tracking Prevention behavior.
4. Because NextRoll operates as an ad-tech intermediary (serving ads via AdRoll/RollWorks across many partner sites), opting out here addresses NextRoll's own tracking but does not opt you out of every ad network you may be tracked by.
