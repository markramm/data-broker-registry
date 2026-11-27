---
id: infousa-com
name: InfoUSA
domain: infousa.com
category: direct_marketers
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
required_fields: [full_name, address, email, phone]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "data-brokers-watch+tcp-research"
notes: "Re-checked 2026-11-27 by the daily maintainer (Refs page-monitor issue #271). The page monitor's fetch of the previous opt_out_url, https://www.data-axle.com/do-not-sell-my-data/, ends at https://www.data-axle.com/privacy-rights-request/ (Consumer Privacy Rights Request | Data Axle), the same shared form the Lake Group Media and Exact Data entries use, so opt_out_url now points there directly (a direct curl of the do-not-sell URL still returns 403). Fetched the form page (HTTP 200): it is a Gravity Form requiring first name, last name, street address/city/state/ZIP, email, phone, a Privacy Choice dropdown (opt out of sale/sharing, correct, delete, access, limit use of sensitive data) and an identity-verification acknowledgement checkbox, followed by a visible Cloudflare Turnstile widget. So captcha is true, tier is guided (CAPTCHA-gated), and required_fields now include address and phone. The earlier notes' claim that address/phone were optional came from web-search copy, not the form, and no longer matches. No Data Axle privacy email was visible in the fetched form page, so the email alternative was dropped from the steps (the Exact Data entry lists privacyteam@data-axle.com from Exact Data's own privacy policy). Nothing was submitted; last_verified stays null. Earlier research: InfoUSA was rebranded to Data Axle (Salesgenie is its consumer-facing product). The migrated opt_out_url 301-redirected to dataaxleusa.com and then to salesgenie.com's privacy policy, confirming the brand has moved off the old infousa.com domain; updated opt_out_url to Data Axle's current do-not-sell form. Direct WebFetch of that form was blocked (403), so not freshly verified -- based on web search of Data Axle's own do-not-sell page copy, which describes a footer link to a form requiring first name, last name, and email (address/phone optional), or emailing them directly. B2B direct-marketing data broker, not people-search, so priority standard. last_verified left null pending a direct fetch."
---

1. Go to https://www.data-axle.com/privacy-rights-request/ -- InfoUSA's data and brand now operate under Data Axle, and its consumer privacy requests go through Data Axle's shared request form.
2. Fill in your first name, last name, street address, city, state, ZIP code, email, and phone number (all are marked required).
3. From the "Privacy Choice" dropdown, select "Request to opt out of sale/sharing" (or "Request to delete" if you also want your record removed).
4. Check the box acknowledging that Data Axle may need to verify your identity, complete the Cloudflare "verify you are human" check, and submit the form.
5. Watch for a follow-up email in case Data Axle asks for more information to verify your identity, and respond to complete the request.
