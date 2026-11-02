---
id: fushiamedia-com
name: Fushia Media LLC
domain: fushiamedia.com
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://fushiamedia.com/request/delete"
opt_out_email: "support@fushiamedia.com"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, phone, address]
verification: none
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Fushia Media is a marketing/data-enhancement company selling '600+ demographic and behavioral attributes' for targeted marketing. Its own privacy policy (fetched at fushiamedia.com/privacy) confirms genuine CCPA broker status: explicit 'Request Data Deletion & Opt-Out' language ('Request that FM delete any personal information about you that FM has collected and opt out of the sale of your personal information'), and it lists Cal. Civ. Code 1798.80(e) categories including address, collected from 'Data Compiling Companies,' 'Public or Government Entities,' and 'Telecommunications Companies.' Found two dedicated forms linked from the privacy policy: /request-data (view your data) and /request-delete (deletion + opt-out of sale). No CAPTCHA markup detected in fetched HTML; no ID/phone requirement stated. opt_out_email is the general support@fushiamedia.com from the legacy CSV -- not independently re-confirmed as a privacy-specific address, kept as a fallback alongside the form. required_fields includes address per Cal. Civ. Code 1798.80(e) category the policy says it collects (address-linked info, including data on 'individuals who are moving'). Maintainer update 2026-11-02 (page monitor #167): /request-delete and /request-data now return HTTP 404. The privacy policy's 'deletion request form' link now points to https://fushiamedia.com/request/delete (fetched: 200, title 'Fuchsia Media - Smarter Data Solutions', heading 'Deletion & Opt-Out'). That form requires first and last name, email, phone number, street address, city, state and ZIP, and has a '03. Security Verification' step: the page's JS bundles react-google-recaptcha and the form schema rejects submission with 'Please complete the CAPTCHA verification'. So captcha is now true, phone is a required field, and tier moves assisted -> guided. No separate data-access form was found (/request/data is 404), so that step was removed. Nothing was submitted."
---

1. Go to https://fushiamedia.com/request/delete, Fuchsia Media's "Deletion & Opt-Out" form (linked from its privacy policy). The request covers both deletion and opt-out of sale/sharing.
2. Enter your first and last name, email address and phone number. All four are required.
3. Enter your street address, city, state and ZIP code (all required). Fuchsia Media says it needs these to find and suppress your record; it collects address-linked data, including on people who are moving, so use the address most likely to be in its database.
4. Complete the CAPTCHA in the "Security Verification" section and submit the request.
5. If the form doesn't work, email support@fushiamedia.com saying you are requesting deletion of your personal information and opting out of its sale or sharing under the CCPA.
6. Keep a note of the date. If you hear nothing within 45 days (the CCPA response window), follow up by email.
