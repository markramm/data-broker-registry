---
id: lakegroupmedia-com
name: Lake Group Media, inc.
domain: lakegroupmedia.com
category: marketing_data_broker
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "https://www.data-axle.com/privacy-rights-request/"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: identity_confirm
required_fields: [full_name, address, email, phone]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Re-checked 2026-11-27 by the daily maintainer (Refs page-monitor issue #272): fetched https://www.data-axle.com/privacy-rights-request/ (HTTP 200). The shared Data Axle Gravity Form now includes a visible Cloudflare Turnstile widget (gfield type turnstile, data-size normal) before the Submit button, replacing the Akismet honeypot it had before; the monitor's new input_17 field is a hidden honeypot, not a user field. Required fields are unchanged: first name, last name, street address/city/state/ZIP, email, phone, a Privacy Choice dropdown (opt out of sale/sharing, correct, delete, access, limit use of sensitive data) and an identity-verification acknowledgement checkbox. captcha set to true and tier to guided per CONTRIBUTING (CAPTCHA-gated). Nothing was submitted; last_verified stays null. Earlier research: lakegroupmedia.com now 301-redirects (confirmed via curl) to https://www.data-axle.com/?visitor=lake_group -- Lake Group Media has been absorbed into Data Axle. WebFetch on data-axle.com/privacy-policy confirmed 'Lake Group Media, Inc.' is explicitly listed among Data Axle's affiliates/subsidiaries. Requests for all Data Axle brands route through the shared Consumer Privacy Rights Request form. WebFetch on that form found required fields: first name, last name, street address, city, state, ZIP, email, and phone, plus a dropdown to select opt-out/correct/delete/access/limit-use and a checkbox acknowledging identity verification may be required. No government-ID upload observed (no CAPTCHA at the time; see 2026-11-27 re-check above). opt_out_email left null since no Lake-Group-specific or Data-Axle-specific email address was confirmed (page uses a Cloudflare-obfuscated mailto). B2B/marketing list data broker, no consumer-facing people-search product -- standard priority. Was assisted tier until the Turnstile CAPTCHA appeared."
---

1. Go to https://www.data-axle.com/privacy-rights-request/ -- Lake Group Media is now operated as a Data Axle brand, and consumer privacy requests for it are handled through Data Axle's shared form.
2. Fill in your first name, last name, street address, city, state, ZIP code, email, and phone number.
3. From the "Privacy Choice" dropdown, select "Opt out of sale/sharing" (or "Delete personal information" if you also want your record removed).
4. Check the box acknowledging that Data Axle may need to verify your identity, complete the Cloudflare "verify you are human" check, and submit the form.
5. Watch for a follow-up email if additional identity verification is requested, and respond to complete the process.
6. Data Axle should process the request within the CCPA-mandated timeframe (typically within 45 days).
