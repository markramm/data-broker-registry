---
id: pipl-com
name: Pipl, Inc
domain: pipl.com
category: identity_verification
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://pipl.com/legal/privacy/"
opt_out_email: "privacy@pipl.com"
phone: "(877) 616-1115"
captcha: false
id_required: true
phone_required: false
charges_fee: false
required_fields: [full_name, email, address]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "Pipl is a B2B identity-verification and fraud-prevention data aggregator: it doesn't run a public consumer search UI, but it compiles and sells identity profiles (names, emails, addresses, phone numbers, IPs) from public sources and third-party providers to business customers for identity verification -- a genuine people-search-grade broker with real personal-safety stakes despite the enterprise framing. WebFetch on pipl.com/legal/privacy/ confirmed CCPA opt-out-of-sale rights and a GDPR-scope deletion/access/objection framework, with three routes: privacy@pipl.com, phone (877) 616-1115, or an online removal-request form -- the policy explicitly states the online removal form requires identity verification, which is why id_required is set true and tier is guided rather than auto despite an email channel also being available. No CAPTCHA was mentioned. people_search:true reflects that the underlying data (identity profiles matched against personal details) is the same category of information covered by classic people-search sites, even though Pipl sells access to businesses rather than directly to consumers. last_verified left null (not independently re-rendered beyond the WebFetch summary)."
---

1. Go to https://pipl.com/legal/privacy/ and review the "Your Rights" / CCPA section to identify the current removal-request process.
2. Use the online removal-request form linked from that page if available; be prepared to verify your identity (name, email, address, and possibly additional details) since Pipl states it verifies requesters before acting on removal requests.
3. Alternatively, email privacy@pipl.com directly, stating you are requesting deletion/opt-out of your personal information under the CCPA (or GDPR if you are an EU/UK/Swiss resident), and include your full name, email, and any addresses associated with you.
4. If you don't get a timely response, you can also call (877) 616-1115 to follow up on your request.
5. If your CCPA/GDPR request goes unresolved, the policy notes that EU/UK/Swiss residents can escalate to BBB National Programs for Data Privacy Framework dispute resolution.
