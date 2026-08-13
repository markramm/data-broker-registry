---
id: datonics-com
name: "Datonics, LLC"
domain: datonics.com
category: advertising_adtech
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.datonics.com/privacy/privacy-choices"
opt_out_email: "privacy@datonics.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: ["email", "other"]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch confirmed Datonics is a programmatic adtech/data provider selling demographic, interest, and behavioral audience segments to DSPs (The Trade Desk, Google DV360, Amazon Xandr, etc.) -- a genuine advertising-data broker, not people-search. Their privacy-choices page (fetched) describes three separate opt-out paths: a browser-based opt-out tool keyed to cookies (for web data), a mobile-ad-ID-based process (for MAID/IDFA/AAID/GAID), and a 'complete this form' flow for hashed-email data, plus a general privacy@datonics.com contact. No single deep-linkable opt-out URL/form field set was fully renderable -- the mechanism is JS-driven and device/ID-dependent rather than a simple static form, so classified guided rather than assisted despite no explicit CAPTCHA being observed. Email given as best documented direct channel."
---

1. Go to https://www.datonics.com/privacy/privacy-choices and use the browser-based "Opt-Out Tool" to see what data Datonics has tied to your current browser and exercise access/delete/opt-out rights for that browser.
2. If you use multiple browsers or devices, repeat the browser tool on each one, since opt-outs are stored per-browser via cookies (clearing cookies will reset your opt-out status).
3. For mobile devices, locate your device's Mobile Advertising ID (IDFA on iOS, AAID/GAID on Android) in your phone's privacy settings, then use the mobile opt-out option on the same page.
4. For data tied to a hashed email address, use the "Complete this form" link on the privacy-choices page to reach a Datonics team member directly.
5. Alternatively (or as a fallback if the tools above aren't accessible), email privacy@datonics.com directly and request that Datonics opt you out of sale/sharing of your personal information under CCPA, including whatever identifying details (email address, general description of devices/browsers used) you're comfortable sharing.
