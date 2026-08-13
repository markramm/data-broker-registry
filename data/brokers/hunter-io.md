---
id: hunter-io
name: "Hunter Web Services Inc"
domain: hunter.io
category: b2b_contact_data_broker
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://hunter.io/claim"
opt_out_email: "privacy@hunter.io"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [email]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on hunter.io/privacy-policy confirmed Hunter states it 'does not sell your personal data to third parties for monetary consideration' but does compile and publish professional email addresses (name + company + email) scraped/inferred from public web sources into its lookup database, which is the harm this entry addresses. WebFetch on hunter.io/claim confirmed a self-serve 'Claim' flow: enter the email address, and Hunter says it will 'immediately process the deletion of all data associated with it' plus stop re-adding it from that source. No login, CAPTCHA, or ID appeared in the fetched page, so tier assisted rather than guided. privacy@hunter.io is also listed in the privacy policy as a direct contact for CCPA/GDPR requests (opt_out_email set to this address as a fallback/alternate channel; the primary path is the claim form). Business contact data (not people-search of private individuals in the traditional sense, but a searchable database of named professionals' emails), so priority high rather than crucial."
---

1. Go to [hunter.io/claim](https://hunter.io/claim).
2. Enter the email address you want removed from Hunter's database.
3. Submit the claim; Hunter states it will immediately delete all data associated with that email address and stop re-associating it with its original source page.
4. If you have multiple email addresses or want a broader deletion/access request handled directly, email privacy@hunter.io instead and describe what you want removed.
5. For California residents, Hunter maintains a separate CCPA notice at hunter.io/privacy-policy/california with additional rights details; requests submitted by email are acknowledged within 45 days (extendable by another 45 days if needed).
