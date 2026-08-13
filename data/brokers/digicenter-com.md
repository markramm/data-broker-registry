---
id: digicenter-com
name: "DigiCenter, LLC."
domain: digicenter.com
category: advertising_adtech
people_search: false
tier: auto
priority: high
method: email
opt_out_url: "<verify: digicenter.com/opt-out/ and digicenter.com/privacy-policy/ both returned empty/unrenderable content on every WebFetch attempt during this research pass -- confirm the opt-out form renders and check its exact fields>"
opt_out_email: "privacy@digicenter.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: ["full_name", "email"]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebSearch confirmed DigiCenter LLC is a registered California data broker (AG registration 190133) providing identity and cross-device graph data for marketers/publishers/ad-tech (320M unique people, 180M households, 1B unique emails per its own marketing claims); acquired by Kochava in 2021 but still separately registered as a data broker under the digicenter.com domain. Its own CA AG registration filing lists 'privacy [at] digicenter.com' as the consumer-rights contact email and https://www.digicenter.com/opt-out/ as the opt-out URL -- this is an authoritative regulatory-filing source, not a third-party guide. However, every WebFetch attempt against digicenter.com (root, /privacy-policy/, /privacy, /ccpa, /opt-out/) returned either HTTP 403 or fully empty page content (likely a JS-rendered SPA that doesn't serve readable content to non-browser fetchers), so I could not independently confirm the opt-out form's fields, CAPTCHA, or gating -- opt_out_url is a <verify:> placeholder and last_verified is null. Given the registry-confirmed email is unambiguous, method:email/tier:auto."
---

1. Email privacy@digicenter.com and state that you are submitting a CCPA opt-out/deletion request regarding personal information DigiCenter has collected or derived about you (including cross-device/identity graph data).
2. Include your full name and the email address you'd like DigiCenter to use in reply.
3. Ask explicitly to opt out of the sale/sharing of your personal information, and request deletion if you want your record removed outright.
4. You may also try DigiCenter's opt-out page at https://www.digicenter.com/opt-out/ (per DigiCenter's own California data-broker registration filing), though this page could not be independently rendered during research -- if it doesn't load, the email above is the confirmed fallback.
5. Keep a copy of your email as a record of the request date, since DigiCenter is now part of Kochava and processing times weren't confirmed.
