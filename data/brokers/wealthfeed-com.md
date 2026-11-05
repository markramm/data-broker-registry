---
id: wealthfeed-com
name: "WealthFeed, Inc."
domain: wealthfeed.com
category: wealth_screening
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://portal.wealthfeed.com/opt-out"
opt_out_email: "privacy@wealthfeed.com"
phone: "(941) 867-1761"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [email, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-11-05 by the daily maintainer from California's data broker registry (WealthFeed, Inc., listing privacy@wealthfeed.com and www.wealthfeed.com). WealthFeed sells consumer leads to financial advisors. Its privacy policy (fetched; last updated January 31, 2024) says it buys consumer identifiers (name, email, phone) and purchase data from other data brokers and sells them to clients as leads under the CCPA. The site markets net-worth and 'money-in-motion' signals. That is consumer data tied to a name and home address, so priority high; it isn't a people-search site. I fetched https://www.wealthfeed.com/do-not-sell-my-data/ (HTTP 200). It says records are keyed by name and address, asks for full name, current mailing address and email, and says a phone number matching their records may be requested to verify you. Its 'Submit an opt-out request' button goes to https://portal.wealthfeed.com/opt-out, a JavaScript app. I rendered that page in a headless browser without submitting. It asks for first and last name (optional), email, phone (optional), address line 1, address line 2, city, state and ZIP, and shows a visible Cloudflare Turnstile 'Verify you're human' check, so captcha is true and tier is guided. The same page offers email instead: privacy@wealthfeed.com with 'Opt-Out Request' in the subject and the same details. That address is also the access/correction/deletion channel, so opt_out_email is set. The phone number is the site footer's general contact number. last_verified null."
---

WealthFeed sells consumer contact and wealth leads to financial advisors. It matches opt-out requests by name and home address.

1. Go to https://portal.wealthfeed.com/opt-out. The "Submit an opt-out request" button on https://www.wealthfeed.com/do-not-sell-my-data/ links to the same page.
2. Enter your first and last name, email address, and current mailing address (street, city, state, ZIP). Name and phone are marked optional, but WealthFeed says its records are keyed by name and address, so include your name.
3. Complete the "Verify you're human" check and submit.
4. If WealthFeed asks you to confirm your identity, it may ask for a phone number that matches its records.
5. If you'd rather not use the form, or you also want access, correction or deletion, email privacy@wealthfeed.com with "Opt-Out Request" in the subject and include your full name, current mailing address and email.
6. If you've moved recently, submit once for each address you've lived at, since records are matched by address.
