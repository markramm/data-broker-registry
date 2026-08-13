---
id: gumgum-com
name: GumGum Inc.
domain: gumgum.com
category: ad_tech
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://privacyportal-cdn.onetrust.com/dsarwebform/fbe4d6b4-7f02-4251-bc4b-142d5109ae3e/1683277a-0ae1-47dd-8845-5e811a07e307.html"
opt_out_email: "dataprivacy@gumgum.com"
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
notes: "WebFetch on gumgum.com/privacy-policy succeeded and rendered current text. GumGum is a contextual ad-tech company; the policy states two ways to opt out: a OneTrust-hosted 'Do Not Sell' web form, or calling a toll-free vanity number quoted verbatim as '866-I-OPT-OUT' with service code 319. Left phone field null rather than guessing the numeric keypad translation, which is not a clean/verifiable digit-for-letter mapping -- the vanity number is quoted as-is in the instructions instead. No CAPTCHA or ID requirement described -> assisted tier (real form, not gated). The opt_out_url is a OneTrust-hosted third-party DSAR form (long tokenized path is the vendor's stable form URL, not a PII query string). last_verified left null -- summarized by the fetch tool, not independently re-rendered by a human."
---

1. Go to the GumGum 'Do Not Sell' web form at https://privacyportal-cdn.onetrust.com/dsarwebform/fbe4d6b4-7f02-4251-bc4b-142d5109ae3e/1683277a-0ae1-47dd-8845-5e811a07e307.html (a OneTrust-hosted privacy request portal used by GumGum).
2. Select the appropriate request type (opt-out of sale/sharing, or deletion) and provide your email address as requested.
3. Submit the form and watch for a confirmation email.
4. Alternatively, call the toll-free number 866-I-OPT-OUT and enter service code 319 when prompted to submit the same request by phone.
5. You can also email dataprivacy@gumgum.com directly if you prefer a written record of your request.
