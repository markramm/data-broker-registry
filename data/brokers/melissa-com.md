---
id: melissa-com
name: Melissa Corporation
domain: melissa.com
category: identity_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://apps.melissa.com/user/consumerprivacy.aspx"
opt_out_email: null
phone: "1-800-800-6245 ext. 4"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [email, full_name, address]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on the melissa.com homepage failed directly (blocked), but curl -L retrieved it and surfaced the real Consumer Privacy Request Form at apps.melissa.com/user/consumerprivacy.aspx, which I fetched via curl and parsed (stripped HTML). Melissa sells contact/identity/address verification data (an identity-data broker, B2B-facing data products but built on real consumer PII) -- confirmed via their own form, which offers delete, opt-out of sale/sharing, right-to-know, correct, and limit-sensitive-use options. The form requires email, first/last name, address, city, state, ZIP, and phone as required fields; ID/driver's license upload is only required for 'know'/'correct' requests, NOT for delete or opt-out-of-sale, which is why id_required is false. No CAPTCHA was observed. melissadata.com (also in my assigned batch) 301-redirects permanently to www.melissa.com (confirmed via curl -sI -L) -- it is the same company/product under a legacy domain, not a separate broker, so no separate file was created for it. Legacy CSV's CCParequest@melissa.com email was not confirmed as a live inbox during this research (the form appears to be the primary/preferred channel), so opt_out_email is left null rather than asserting it -- form-only -> guided tier given the number of required fields and identity-adjacent nature, even without CAPTCHA. Maintainer update 2026-11-24 (page-monitor #263): the 2026-11-23 monitor snapshot of the form and a curl fetch of the live page the same day both show that the form now asks you to check a reCAPTCHA 'I'm not a robot' box (the page loads recaptcha/api) and to click 'Send Confirmation Code', which emails a one-time code that must be entered before the request is submitted; so captcha is now true and verification email_confirm. Phone is no longer marked required (only email, first/last name, address line 1, city, state and ZIP carry the asterisk). The form now also offers 'opt out of targeted ads/profiling' and 'limit sensitive information' options, and the Right to Correct section says ID documents are normally not needed. Not walked through by a human: last_verified stays null."
---

1. Go to https://apps.melissa.com/user/consumerprivacy.aspx (Melissa's Consumer Privacy Request Form).
2. Fill in the required fields: email address, first name, last name, address line 1, city, state and ZIP code. Phone is optional.
3. In the "Delete/Opt-Out" section, check "I want Melissa to delete any personal information it has collected about me" and "I want to opt out of the sale or sharing of my personal information". You can also check the targeted-ads/profiling and limit-sensitive-information options.
4. Check the reCAPTCHA "I'm not a robot" box and click "Send Confirmation Code". This does not submit the request yet.
5. Open the email Melissa sends and enter the one-time code on the form to submit the request.
6. If you prefer not to use the web form or need to submit multiple records at once, call 1-800-800-6245 ext. 4 instead.
