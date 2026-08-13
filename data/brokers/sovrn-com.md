---
id: sovrn-com
name: Sovrn
domain: sovrn.com
category: adtech
people_search: false
tier: auto
priority: standard
method: email
opt_out_url: "<verify: exact Sovrn Privacy Center opt-out page URL>"
opt_out_email: "privacy@sovrn.com"
phone: "+1 (888) 280-8085"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch of Sovrn's privacy policy confirmed it is an adtech/publisher-monetization company that primarily collects device and browser identifiers (cookie IDs, IP addresses, mobile ad IDs, hashed emails, CTV identifiers) rather than direct identifiers -- its policy states verbatim it does not collect direct personal identifiers like names or plain-text emails about readers. Opt-out/opt-in instructions point to a 'Privacy Center' page (exact URL not confirmed by the fetch) or enabling Global Privacy Control (GPC) in-browser, plus email privacy@sovrn.com (subject line 'CCPA Consumer Request') and phone +1 (888) 280-8085. GDPR requests go to the same email; an EU representative (IT Governance Europe Limited) is also listed. Because the specific Privacy Center URL wasn't independently confirmed, opt_out_url is a verify-placeholder and last_verified is null. Given Sovrn deals mainly in device/cookie identifiers rather than name/address/phone people-search data, this is adtech not people-search -- priority standard, not crucial."
---

1. The simplest opt-out is to enable Global Privacy Control (GPC) in your browser (e.g. via a GPC-supporting extension or browser setting) -- Sovrn's policy states it honors GPC signals as an opt-out of sale/sharing.
2. Alternatively, email privacy@sovrn.com with "CCPA Consumer Request" in the subject line, stating you want to opt out of the sale/sharing of your personal information.
3. If you're in the EEA/UK/Switzerland, the same email address (privacy@sovrn.com) can be used to exercise GDPR rights (access, deletion, objection).
4. You can also call +1 (888) 280-8085 to reach Sovrn's privacy team directly.
5. Note that Sovrn's policy states it primarily processes device/browser-level identifiers (cookie IDs, IP addresses, hashed emails, ad IDs) rather than directly-identifying data like your name, so an opt-out mainly stops those identifiers from being used for ad targeting/sale rather than removing a "profile" in the people-search sense.
