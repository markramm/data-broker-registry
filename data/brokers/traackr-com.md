---
id: traackr-com
name: Traackr
domain: traackr.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: standard
method: email
opt_out_url: "https://www.traackr.com/data-opt-out"
opt_out_email: "datarequest@traackr.com"
phone: "+1-855-872-2257"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch confirmed Traackr is an influencer-marketing platform (AI-powered creator discovery/campaign/measurement) that maintains a separate Influencer Privacy Notice (traackr.com/legal/influencer-privacy-notice) distinct from its general customer-facing privacy policy. That notice explicitly states: 'We sell your personal data to our business customers, whose representatives are users of our platform' -- covering influencer/creator names, emails, ages, social handles, public posts, audience/engagement metrics, and (for Studio users) phone/address/social-login auth data. This is a genuine CCPA 'sale' of personal data about identifiable individuals (influencers), not just B2B contact data, so treated as a real data-broker entry rather than pure B2B/dropped. The general privacy policy (traackr.com/legal/privacy-policy) separately states Traackr does NOT sell data covered by that policy (i.e. site-visitor/customer data) -- the sale disclosure applies specifically to influencer data under the Influencer Privacy Notice. Opt-out channels confirmed via WebFetch of both privacy pages: web form at traackr.com/data-opt-out (identity verification follow-up, no CAPTCHA marker found in a curl fetch of that page, though it may be JS-rendered), email datarequest@traackr.com (or legal@traackr.com), and phone +1 (855) TRAACKR / 872-2257. Categorized marketing_data_broker (not people_search) since it targets influencers/creators for brand marketing use cases, not general public address/phone lookups. Priority standard: real working opt-out but not a personal-safety-critical people-search site. Page not rendered by a human at time of authoring -- last_verified left null."
---

1. Go to https://www.traackr.com/legal/influencer-privacy-notice and confirm you are covered as an "influencer" under Traackr's data-sale disclosure (this applies to creators/influencers whose public social profiles and content Traackr tracks for its brand customers).
2. To opt out of the sale/sharing of your personal data, either:
   a. Visit https://www.traackr.com/data-opt-out and complete the request form with your name and email/contact details, or
   b. Email datarequest@traackr.com (or legal@traackr.com) directly, stating you are requesting to opt out of the sale of your personal data under CCPA, and include your full name plus the email address(es)/social handles associated with your public profile.
3. You can also call +1 (855) TRAACKR (872-2257) to initiate the same request by phone.
4. Expect Traackr to follow up by email to verify your identity before completing the opt-out -- respond to that confirmation message.
5. Because Traackr's data comes from public social platforms, it may re-collect your public profile/content in future re-scrapes; there is no documented re-add cadence, so periodically re-check your profile status on the platform if you remain a public creator/influencer.
