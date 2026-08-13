---
id: goodhire-com
name: GoodHire
domain: goodhire.com
category: background_checks
people_search: false
tier: auto
priority: high
method: email
opt_out_url: null
opt_out_email: "dpo@inflection.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on goodhire.com/privacy succeeded and rendered the current CCPA section. GoodHire is an employment background-check provider owned by Inflection Risk Solutions, LLC; it screens applicants on behalf of employers rather than selling identity lookups directly to the public, so people_search is false. The privacy policy gives two CCPA contact addresses (dpo@inflection.com and legal@inflection.com) and explicitly states background-check data regulated by the FCRA is exempt from CCPA data-subject rights -- so this opt-out mainly covers marketing/site-usage data, not the underlying consumer report. Plain email contact with no form/CAPTCHA -> tier auto. last_verified left null since no human has re-confirmed since this fetch."
---

1. Note that GoodHire's background-check reports on you are governed by the Fair Credit Reporting Act (FCRA), not CCPA -- if you want to dispute or correct an actual background-check report, you must go through the employer that ordered it or GoodHire's FCRA dispute process, not this opt-out.
2. For CCPA-covered data (e.g., marketing data, website usage data GoodHire holds about you as a California resident), email dpo@inflection.com and state that you are exercising your CCPA rights to know, delete, or opt out of sale/sharing of your personal information.
3. Include your full name and the email address associated with any GoodHire-related activity so the privacy team can locate your record.
4. You may also send the request to legal@inflection.com as an alternate contact listed in the same policy.
5. Expect a response verifying your identity before the request is processed; GoodHire's mailing address (Inflection Risk Solutions, LLC, Attn: Privacy Team, 1 Montgomery St. Ste 2400, San Francisco, CA 94104) is available if you prefer a written request.
