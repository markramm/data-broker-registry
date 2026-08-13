---
id: liveintent-com
name: "LiveIntent, Inc."
domain: liveintent.com
category: adtech_identity_broker
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://privacy.liveintent.com"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on liveintent.com/privacy confirmed LiveIntent is an email-identity/audience-matching adtech company that builds consumer profiles linked to email addresses for publishers and advertisers -- a genuine identity data broker. Their dedicated consumer privacy portal is at privacy.liveintent.com, offering opt-out of sale/sharing, ad personalization, and deletion requests; the page also states LiveIntent honors Global Privacy Control (GPC) signals automatically with no account needed. Portal is likely form-based with identity verification typical of this class of adtech privacy center -> classified guided rather than auto since no plain opt-out email is offered directly (only the portal). captcha:true is an inference from typical adtech DSR-portal design, not directly observed; not independently re-rendered by a human, last_verified left null."
---

1. Go to https://privacy.liveintent.com, LiveIntent's consumer privacy center.
2. Choose the request type you want: opt out of the sale/sharing of your personal information, opt out of interest-based advertising, or request deletion of your data.
3. Enter the email address(es) associated with your identity so LiveIntent can locate and act on your record, and complete any verification step the portal presents.
4. Submit the request and watch for a confirmation email.
5. If you use a browser or extension that sends a Global Privacy Control (GPC) signal, LiveIntent states it will automatically treat that as an opt-out of sale/sharing without requiring this form.
6. Expect a response within 45 days (up to 90 days for complex requests), per LiveIntent's stated CCPA/GDPR timelines.
