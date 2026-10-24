---
id: bbdirect-com
name: BB Direct, Inc.
domain: bbdirect.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://www.bbdirect.com/resources/privacy/privacy-compliance.html"
opt_out_email: null
phone: "866-501-6273"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [full_name, address, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch of bbdirect.com's privacy-compliance page 403'd directly, but WebSearch and a fetch of JoinDeleteMe's BBDirect opt-out guide corroborate the process: BB Direct is a direct-mail list broker (New Mover list, Bankruptcy Masterfile, Registered Voters list, etc. -- rents third-party consumer lists to marketers) registered as a CA data broker. Opt-out is via a 'CCPA Compliance' link in the site footer leading to an online form requiring first/last name, address, city, state, zip, and which mail piece prompted the request -- no CAPTCHA mentioned in the guide. Simple form, no CAPTCHA/ID -> assisted tier. Marketing list broker (not a people-search product) but does resell real consumer mailing/contact data -> high priority, people_search false. Update 2026-10-24 (daily maintainer, page-monitor #118): the monitor had been getting a bot-check interstitial, and on 10-23 got the real page. Loaded in a headless browser today, https://www.bbdirect.com/resources/privacy/privacy-compliance.html shows an embedded Cognito Forms 'Opt-Out Privacy Compliance Form' with three required fields: Name (first, last), Address (line 1, line 2, city, state, ZIP) and Email. There is no longer a field for which mail piece prompted the request. The page says BB Direct adds the submission to its 'Opt-Out Privacy Suppression Database' so the record is excluded from future marketing data. The site loads Google reCAPTCHA Enterprise in invisible mode (badge hidden, no visible challenge), so captcha stays false and the tier stays assisted. Nothing was submitted; last_verified stays null."
---

1. Go to https://www.bbdirect.com/resources/privacy/privacy-compliance.html (the "Privacy Compliance & Opt-Out Form" link in the site footer).
2. Fill in all three required fields: your first and last name, your full mailing address (street, city, state, ZIP), and your email address.
3. Submit the form. BB Direct says it adds your record to its opt-out suppression database so it's left out of the marketing data it provides to customers.
4. The form takes one name and one address, so submit it again for any other address you've lived at.
5. Alternatively, call BB Direct at (866) 501-6273 or write to PO Box 151261, Cape Coral, FL 33915 to make the same request.
