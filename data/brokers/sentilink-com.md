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
opt_out_email: "legal.notices@sentilink.com"
phone: null
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
notes: "SentiLink is a known identity-verification/fraud-detection vendor serving banks and fintechs (confirmed via its own tagline 'The fraud experts' and third-party search summaries); it processes consumer identity signals as part of fraud-risk scoring for its business clients rather than reselling consumer profiles directly to the public, but it does hold consumer data and offers CCPA rights. Direct WebFetch of sentilink.com/privacy-policy repeatedly returned only an empty JS-rendered shell (Next.js SPA, confirmed via curl showing only script tags, no body text) -- content below is reconstructed from a third-party search-engine summary of the same policy, not a direct render, so treat with extra caution. That summary states SentiLink recognizes CCPA rights to know/delete/opt-out of sale, handled via a plain email to legal.notices@sentilink.com -- method:email, so tier:auto per schema convention. A Google reCAPTCHA script was seen loaded site-wide in the raw HTML, but there is no confirmation it gates the email opt-out channel itself, so captcha left false rather than inferring. opt_out_url kept as the real known page (not a placeholder) since the URL itself is confirmed correct even though its rendered content wasn't independently verified by me. last_verified left null given the unverified render."
---

1. Email legal.notices@sentilink.com and state that you are exercising your CCPA rights to know what personal information SentiLink has about you, and/or requesting deletion or opt-out of sale.
2. Include your full name and the email address(es) SentiLink may have associated with you, since SentiLink primarily receives identity data through its bank/fintech clients rather than directly from consumers.
3. Watch for a reply confirming receipt and any further identity-verification steps SentiLink requires before acting on the request.
4. Because SentiLink primarily receives your data via banks/fintechs it contracts with, also consider that the underlying financial institution may be a more effective point of control for the data itself.
