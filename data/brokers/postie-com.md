---
id: postie-com
name: Postie
domain: postie.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://optout.postie.com/"
opt_out_email: "info@postie.com"
phone: "855-931-2869"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [full_name, email, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirmed via WebFetch on postie.com/privacy-policy (rendered successfully). Postie licenses consumer data from third-party data providers to build targeted-marketing/'lookalike audience' profiles for its direct-mail clients -- a genuine data broker as well as a direct-mail vendor, not merely a mail fulfillment shop. The privacy policy describes a dedicated opt-out form at optout.postie.com covering sale/sharing/targeted-advertising, plus email (info@postie.com) and phone (855-931-2869) contact options, and reports the company processed ~285,000 opt-out requests in the prior year with a median 1-day response time -- suggesting a working, low-friction process. No CAPTCHA or ID requirement reported in the fetched policy text, so classified assisted rather than guided; opt_out_email listed for reference but method is form (the dedicated optout.postie.com form) not email, so tier is assisted not auto. last_verified left null since the optout.postie.com form itself was not directly rendered in this pass, only described by the privacy-policy text."
---

1. Go to https://optout.postie.com/ and follow the prompts to opt out of the sale, sharing, or targeted-advertising use of your personal information.
2. If the form requires it, provide your name, email address, and mailing address so Postie can match you to any profile or mailing-list record.
3. Alternatively, email info@postie.com and state you are exercising your CCPA right to opt out of sale/sharing (and, if you want, request deletion); include your name and mailing address.
4. Or call 855-931-2869 to make the same request by phone.
5. Postie's stated median response time for opt-out requests is about one day; check back at optout.postie.com or via a follow-up email if you don't receive confirmation.
6. Note Postie also licenses data from third-party providers for its clients' direct-mail campaigns -- your opt-out with Postie stops Postie's own targeting but does not necessarily reach the original third-party data providers it licensed your information from.
