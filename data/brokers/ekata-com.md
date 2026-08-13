---
id: ekata-com
name: Ekata
domain: ekata.com
category: identity_verification
people_search: true
tier: guided
priority: crucial
method: unsupported
opt_out_url: "<verify: exact Mastercard consumer privacy-rights / opt-out URL that covers Ekata Identity Engine data>"
opt_out_email: null
phone: null
captcha: true
id_required: true
phone_required: false
charges_fee: false
required_fields: [full_name, address, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Prior pass found Ekata is a real identity-verification broker (address/phone/identity risk-scoring on individuals, sold to businesses for fraud/KYC checks), now Mastercard-owned, but every fetch attempt was Cloudflare/Akamai bot-blocked. This round: confirmed ekata.com/, /privacy, /opt-out, and /ccpa all return blanket HTTP 301 redirects to a single generic Mastercard marketing page (mastercard.com/us/en/business/cybersecurity-fraud-prevention/identity.html) -- meaning Ekata no longer has any standalone branded site or opt-out flow; it has been fully absorbed into Mastercard's identity/fraud-prevention business line. ekata.com/privacy-policy separately redirects to mastercard.com/global/en/identity-privacy-policy.html. Every Mastercard URL attempted (the identity-privacy-policy page, mastercard.us data-responsibility page, mastercard.com/global/en/vision/privacy.html, privacy.mastercard.com) returned HTTP 403 from Akamai's bot-protection on every fetch attempt (both WebFetch and direct curl), so I could not confirm the exact current consumer opt-out/deletion request mechanism, whether it's a form or portal, or its CAPTCHA/ID requirements. Given Mastercard is a large, heavily regulated financial-services company that acquired a firm whose core product was resold identity/address/phone data on named individuals, I'm treating id_required, captcha as true and tier as guided by conservative default (consistent with the schema's 'when in doubt, pick guided' guidance) rather than asserting unconfirmed specifics. method left as unsupported since I could not confirm an actual working self-service channel exists at all post-merger. opt_out_url is a <verify:> placeholder accordingly and last_verified is null. priority:crucial preserved because the underlying data (identity/address risk profiles on individuals) remains squarely people-search-equivalent even though the corporate wrapper changed."
---

1. Ekata no longer operates a standalone consumer-facing website -- ekata.com now redirects entirely into Mastercard's identity and fraud-prevention business pages, so there is no Ekata-specific opt-out page left to use directly.
2. Because Mastercard's privacy pages are aggressively bot-protected, this entry could not be independently verified end-to-end; treat the following as a starting point, not a confirmed working flow.
3. Search Mastercard's site (mastercard.com) for its consumer privacy rights / "Do Not Sell or Share" or data subject request page, which should be the umbrella mechanism now covering Ekata Identity Engine data.
4. If you cannot locate a working self-service form, consider filing a CCPA/CPRA deletion or opt-out request through Mastercard's general privacy contact channel, referencing "Ekata" and "Ekata Identity Engine" by name so the request is routed to the right data set.
5. Because this broker's data (identity/address/phone risk profiles) is high personal-safety-impact and the routing is unconfirmed, this entry is flagged for follow-up verification -- if you find a working direct link, please help update this record.
