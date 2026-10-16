---
id: postie-com
name: Postie
domain: postie.com
category: marketing_data_broker
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "https://optout.postie.com/"
opt_out_email: "info@postie.com"
phone: "855-931-2869"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [full_name, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "2026-10-16 maintainer run (Fixes #41): fetched https://optout.postie.com/ directly (HTTP 200, 'Postie Opt Out'). The form asks only for first name, last name, street address, apartment (optional), city, state and ZIP. There is no email field. It has a visible Google reCAPTCHA (div.g-recaptcha with a sitekey, and a 'Please check the recaptcha' error), so captcha: true, tier assisted -> guided, required_fields [full_name, address]. Nothing was submitted. Background from the earlier pass (postie.com/privacy-policy): Postie licenses consumer data from third-party providers to build targeted-marketing and lookalike-audience profiles for direct-mail clients, so it is a data broker as well as a mail vendor. The policy also lists info@postie.com and 855-931-2869 for requests and reports a median 1-day response time. last_verified stays null."
---

1. Go to https://optout.postie.com/.
2. Enter your first and last name and your mailing address (street, apartment if any, city, state and ZIP). The form does not ask for an email address.
3. Complete the reCAPTCHA and click "Opt Out".
4. Alternatively, email info@postie.com and say you are exercising your CCPA right to opt out of sale/sharing (and, if you want, deletion); include your name and mailing address.
5. Or call 855-931-2869 to make the same request by phone.
6. Postie also licenses data from third-party providers for its clients' mail campaigns. Opting out with Postie stops Postie's own targeting but does not necessarily reach those original providers.
