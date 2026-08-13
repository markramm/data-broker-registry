---
id: socialgist-com
name: Socialgist
domain: socialgist.com
category: social_media_data_licensing
people_search: false
tier: auto
priority: standard
method: email
opt_out_url: "https://www.socialgist.ai/c/privacy-and-terms/"
opt_out_email: "privacy@socialgist.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [email, other]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on socialgist.com/privacy-policy (redirects to socialgist.ai/privacy-policy, then to socialgist.ai/c/privacy-and-terms/) confirmed Socialgist is a B2B data-infrastructure company that aggregates and licenses ~34B/year public social-media/forum/blog conversations to enterprise clients (Brandwatch, Meltwater, Snowflake Marketplace, etc.) for social-listening and AI training -- it self-discloses as 'a data broker under Texas law.' It is not a consumer-facing people-search or home-address product; the personal data involved is public social-media content/handles, not identity/contact records. Opt-out is by email only to privacy@socialgist.com, and the policy specifically requires the requester to include the social media handles/usernames the request should apply to -- required_fields includes 'other' for this handle/username requirement, which has no dedicated schema enum value. Response window 45 days; authorized agents accepted with signed permission. method:email -> tier:auto per schema convention. Standard priority: B2B social-data licensing, not a personal-safety-critical people-search product, though it does process identifiable public posts/handles."
---

1. Email privacy@socialgist.com to submit your opt-out or data-subject request.
2. In the email, include any social media handles or usernames you want the request to apply to -- Socialgist's policy states this is required for them to locate and act on your data.
3. State which right you are exercising: opt-out of sale/sharing, access/know, deletion, or correction.
4. If you are acting through an authorized agent, include signed written permission establishing that authorization.
5. Socialgist's policy states a target response window of 45 days.
