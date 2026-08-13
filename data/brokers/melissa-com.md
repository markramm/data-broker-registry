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
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [email, full_name, address, phone]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on the melissa.com homepage failed directly (blocked), but curl -L retrieved it and surfaced the real Consumer Privacy Request Form at apps.melissa.com/user/consumerprivacy.aspx, which I fetched via curl and parsed (stripped HTML). Melissa sells contact/identity/address verification data (an identity-data broker, B2B-facing data products but built on real consumer PII) -- confirmed via their own form, which offers delete, opt-out of sale/sharing, right-to-know, correct, and limit-sensitive-use options. The form requires email, first/last name, address, city, state, ZIP, and phone as required fields; ID/driver's license upload is only required for 'know'/'correct' requests, NOT for delete or opt-out-of-sale, which is why id_required is false. No CAPTCHA was observed. melissadata.com (also in my assigned batch) 301-redirects permanently to www.melissa.com (confirmed via curl -sI -L) -- it is the same company/product under a legacy domain, not a separate broker, so no separate file was created for it. Legacy CSV's CCParequest@melissa.com email was not confirmed as a live inbox during this research (the form appears to be the primary/preferred channel), so opt_out_email is left null rather than asserting it -- form-only -> guided tier given the number of required fields and identity-adjacent nature, even without CAPTCHA."
---

1. Go to https://apps.melissa.com/user/consumerprivacy.aspx (Melissa's Consumer Privacy Request Form).
2. Review the linked Privacy Policy and, if you are a California resident, the linked Privacy Notice for Residents of California to understand which rights apply to you.
3. Fill in the required fields: email address, first name, last name, address line 1, city, state, ZIP code, and phone.
4. Under "Consumer Privacy Request Options," check "I want Melissa to delete any personal information they have collected about me" and/or "I want to opt out of the sale or sharing of my personal information." (These two options do not require identity-document verification.)
5. Do not check the "know," "obtain a copy," or "correct" options unless you are prepared to upload a copy of your driver's license or other ID -- Melissa requires document verification for those specific requests.
6. Submit the form.
7. If you prefer not to use the web form or need to submit multiple records at once, call 1-800-800-6245 ext. 4 instead.
