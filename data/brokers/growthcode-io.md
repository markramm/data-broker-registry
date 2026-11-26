---
id: growthcode-io
name: "GrowthCode"
domain: growthcode.io
category: adtech_data_broker
people_search: false
tier: auto
priority: standard
method: email
opt_out_url: "https://www.growthcode.io/do-not-sell"
opt_out_email: "delete@growthcode.io"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [email]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Written 2026-11-26 by the daily maintainer from California's data broker registry (GrowthCode, LLC). The registry's rights URL https://growthcode.io/do-not-sell-or-share-my-personal-information now returns a 404 page. The site footer's 'Do Not Sell or Share My Personal Information' link goes to https://www.growthcode.io/do-not-sell, which a plain fetch returned with HTTP 200. That page says GrowthCode is a registered data broker in California, Texas and Vermont, and sells or shares identity-resolution data collected through publisher and partner networks. It lists four opt-out methods. (1) A request form; it is rendered by JavaScript and not in the static HTML, so its fields were not seen. (2) Email delete@growthcode.io with the subject 'Do Not Sell or Share My Personal Information' and enough identifiers to find your data, such as your email address. The page says requests sent to privacy@growthcode.io will NOT be handled as opt-outs. (3) Global Privacy Control, honored for California and Texas residents. (4) California's DROP platform (cppa.ca.gov), which the page says GrowthCode checks weekly. Requests are confirmed within 15 business days. The plain email route needs no login or form, so tier is auto. The registry lists a staff member's personal address as its contact; it was not used because the page names delete@growthcode.io. Adtech identity graph with no people-search product, so priority is standard. Nothing was sent; last_verified is null."
---

1. Email delete@growthcode.io with the subject line "Do Not Sell or Share My Personal Information". Don't use privacy@growthcode.io. GrowthCode says that inbox doesn't handle opt-outs.
2. In the email, ask GrowthCode to stop selling and sharing your personal information and to delete it. Include the email address(es) and any other identifiers you think its records may have.
3. GrowthCode says it confirms requests within 15 business days. You can also use the request form on https://www.growthcode.io/do-not-sell instead of emailing.
4. Turn on Global Privacy Control in your browser. GrowthCode treats it as an opt-out for California and Texas residents.
5. California residents can instead file one deletion request through the state's DROP platform at cppa.ca.gov, which GrowthCode says it checks every week.
