---
id: firstorion-com
name: First Orion Corporation
domain: firstorion.com
category: caller_id_data_broker
people_search: false
tier: guided
priority: standard
method: portal
opt_out_url: "https://privacy.firstorion.com/"
opt_out_email: "privacy@firstorion.com"
phone: "1-877-640-4220"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [phone, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "First Orion provides branded-calling and call-verification/anti-spoofing infrastructure (INFORM, ENRICH, SENTRY, PROTECT+, AFFIRM) primarily sold B2B to businesses (16,000+ clients including Fortune 500 companies). It is not a general people-search identity broker, but it does process and monetize consumer phone-number/call-metadata data as part of its caller-ID and branded-calling products, and it maintains a dedicated CCPA 'Do Not Sell My Info' / 'Your Privacy Choices' presence, including a standalone privacy-request portal at privacy.firstorion.com (confirmed live via curl -- a JavaScript single-page app, title 'First Orion Privacy', consistent with a OneTrust-style CCPA request tool) plus a listed privacy contact email and phone number in the main privacy policy fetch. Because the portal is JS-rendered, its exact form fields/CAPTCHA could not be directly observed, so tier kept guided and method set to portal rather than form. people_search left false since this is call/phone metadata for businesses, not individual identity/address lookups; priority standard given the B2B orientation and the real-but-narrow personal-safety relevance of phone metadata."
---

1. Go to https://privacy.firstorion.com/, First Orion's dedicated privacy-request portal, and follow the prompts to submit a CCPA "Do Not Sell My Info" opt-out or a data-access/deletion request.
2. If the portal is unclear or does not load, you can instead email privacy@firstorion.com directly with your request, including the phone number(s) you want covered.
3. You can also call First Orion's privacy line at 1-877-640-4220 (or write to First Orion Corp., Legal Department, 520 Main Street, Suite 400, North Little Rock, AR 72114) to submit the same request.
4. Note that First Orion primarily serves businesses (branded caller ID, spam/fraud call detection) rather than operating a public people-search product, so this opt-out chiefly affects how your phone number is processed/labeled in their caller-ID and call-verification systems.
