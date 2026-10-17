---
id: directmail-com
name: DirectMail.Com
domain: directmail.com
category: direct_marketers
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "http://www.directmail.com/directory/mail_preference/"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, address, email]
readd_days: null
legal_basis: []
last_verified: "2026-07-03"
source: data-brokers-watch
notes: "Fetched live 2026-07-03: page is a simple 'National Do Not Mail List' registration form, no CAPTCHA. DirectMail.com is a mail-list aggregator/reseller (B2B-ish direct-marketing data), not a people-search site, so priority is standard (spam-reduction, not personal-safety) despite people_search:false already matching category direct_marketers. 2026-10-16 maintainer run (Fixes #35): the opt_out_url now redirects within the same site to https://www.directmail.com/mail_preference/ (HTTP 200, same 'National Do Not Mail List' form). The form now has a visible Google reCAPTCHA (div.g-recaptcha with a sitekey, placed after the email field), so captcha: true and tier assisted -> guided. Telephone is optional on the form, so phone was removed from required_fields. Nothing was submitted. last_verified keeps the human 2026-07-03 date because the URL and fields are otherwise unchanged; a reviewer may want to re-check it."
---

1. Go to https://www.directmail.com/directory/mail_preference/ (it now redirects to https://www.directmail.com/mail_preference/).
2. Fill in your title, first name, last name, address, city, state, and ZIP code.
3. Enter your email address (used to confirm the request) and, optionally, a phone number.
4. Check the box for "I do not want to receive any special offers in the mail."
5. Complete the reCAPTCHA, then click Submit to add yourself to DirectMail.com's internal National Do Not Mail List.
6. Note this only stops DirectMail.com's own use of your data — it does not forward your request to the other mailers/list compilers it resells data to, so pair it with DMAchoice registration for broader effect.
