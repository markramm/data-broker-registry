---
id: sentilink-com
name: SentiLink
domain: sentilink.com
category: identity_verification_fraud
people_search: false
tier: auto
priority: standard
method: email
opt_out_url: "https://www.sentilink.com/privacy-policy"
opt_out_email: "privacy@sentilink.com"
phone: "877-676-8565"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "2026-11-20 maintainer update (refs #252): the page monitor now captures the rendered text of sentilink.com/privacy-policy (snapshot dated 2026-11-19; the policy says 'Last updated: June 01, 2026'). Its 'How to Exercise Your California Consumer Rights' section names two channels: email privacy@sentilink.com with the subject line 'California Rights Request', or call 877-6-SNTLNK (877-676-8565). The entry previously used legal.notices@sentilink.com, taken from a third-party search summary when the page only returned an empty JS shell; that address does not appear in the current policy, so opt_out_email and phone now follow the page. The policy says SentiLink may need to verify identity and may ask for more information such as email and mailing address. SentiLink is an identity-verification/fraud-detection vendor for banks and fintechs; it receives consumer identity data through its clients rather than selling profiles to the public. A Google reCAPTCHA script loads site-wide but does not gate the email channel, so captcha stays false. Not walked through by a human: last_verified stays null."
---

1. Email privacy@sentilink.com with the subject line "California Rights Request". SentiLink's privacy policy asks for this subject line.
2. In the body, say which rights you are using: to know what personal information SentiLink holds about you, to delete it, and/or to correct it. Include your full name and the email address(es) SentiLink may have linked to you.
3. Or call 877-6-SNTLNK (877-676-8565) and make the same request by phone.
4. SentiLink may ask for more details, such as your email and mailing address, to verify your identity before it acts. Watch for that reply.
5. SentiLink mostly gets your data through the banks and fintechs it works for. Those companies may also be worth contacting.
