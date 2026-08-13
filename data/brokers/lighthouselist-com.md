---
id: lighthouselist-com
name: Lighthouse List Company, LLC
domain: lighthouselist.com
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://unsubscribe.stirista.com"
opt_out_email: "privacy@stirista.com"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on lighthouselist.com's homepage confirmed a live consumer data broker: audience-targeting/list company claiming 240M consumers, 600M unique emails, 165M households, and 6B devices in its data, delivered across direct mail/email/digital/CTV/gaming channels. Its footer privacy policy and 'Do Not Sell' links both point to its parent company Stirista (privacy policy at stirista.com/privacy-policy/, opt-out at unsubscribe.stirista.com), and Stirista's own privacy policy confirms it operates the opt-out/do-not-sell process for its brands and is reCAPTCHA-protected -- captcha: true, hence guided tier. Stirista's privacy policy did not name Lighthouse List specifically as a covered brand, so this affiliation is inferred from Lighthouse List's own footer links pointing to Stirista rather than confirmed on the Stirista side; flagging that gap. Scale of consumer/household data (not just B2B contacts) pushes this to high priority; not crucial since it is audience-segment marketing data rather than a people-search identity/address lookup tool. required_fields based on Stirista's policy statement that opt-outs need 'confirming your possession of an identifier (such as an email address)'; the unsubscribe.stirista.com form itself only rendered a 'Loading...' placeholder in this session's fetch (JS-rendered), so the full field list wasn't directly observed. last_verified left null."
---

1. Go to https://unsubscribe.stirista.com (the opt-out portal used by Lighthouse List's parent company, Stirista).
2. Follow the form's prompts, providing your email address to identify the record.
3. Solve the CAPTCHA (reCAPTCHA) to submit the request.
4. If the form doesn't load or you'd rather use email, send a request to privacy@stirista.com, referencing Lighthouse List specifically and your CCPA right to opt out of the sale/sharing of your personal information.
5. Stirista's policy states opt-out requests are typically processed within about 10 business days -- watch for a confirmation.
