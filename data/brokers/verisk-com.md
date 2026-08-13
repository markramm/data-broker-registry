---
id: verisk-com
name: "Verisk Analytics, Inc."
domain: verisk.com
category: insurance_risk_data
people_search: false
tier: guided
priority: high
method: email
opt_out_url: "<verify: Verisk operates dozens of separate per-product/per-subsidiary CCPA notice pages (e.g. /privacy-policies/ccpa-velocity/, /privacy-policies/iso-claims-solutions-ccpa-faqs/, /privacy-policies/xactware-ccpa/, /privacy-policies/vde-service-desk-ccpa-notice/) rather than one unified consumer opt-out page -- confirm which product's data actually concerns you before picking a URL>"
opt_out_email: "privacy@verisk.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: identity_confirmation
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Verisk is a large insurance/risk-data conglomerate (parent of ISO ClaimSearch, Xactware, and many other subsidiaries, and separately acquired Infutor, a consumer identity-resolution/contact-database company, per Verisk newsroom sitemap entries) -- confirming the hint that this is a major, high-value entry. Verisk's corporate and client privacy notices (fetched: /privacy-policies/online-privacy-notice/ and /privacy-policies/client-privacy-notice/) both state Verisk 'does not sell or otherwise disclose personal data that you provide to us or that we collect' through its own website/account sign-up -- i.e. these cover Verisk-as-website-operator, not Verisk's insurance data products. The substantive consumer-impact business (ISO ClaimSearch claims-history database, used industry-wide by insurers) is addressed in a separate FAQ page (/privacy-policies/iso-claims-solutions-ccpa-faqs/, fetched via curl+regex extraction): it takes the legal position that Verisk acts as a 'service provider' to the insurers who contribute claims data, and therefore CCPA's opt-out-of-sale right does NOT apply to that contributory database -- consumers cannot opt ISO ClaimSearch out of sale in the way they could with a marketing data broker. That same FAQ page gives one general contact for CCPA questions: privacy@verisk.com. Other subsidiary products (Velocity, Xactware, VDE Service Desk) have their own separate CCPA notice pages not individually verified here. Given this fragmentation and the explicit no-opt-out-right position on its flagship consumer-relevant database, method is set to email (the one consistently-documented contact) and tier guided (a human needs to figure out which subsidiary/product applies and may hit the service-provider exemption). people_search is false -- Verisk itself is not a consumer-facing lookup site, though its Infutor subsidiary (separate domain, not in scope here) is identity-resolution-adjacent. Priority high given Verisk's scale and the real (if limited) consumer rights involved (access/correction under FCRA-adjacent processes for claims history, similar to a LexisNexis C.L.U.E. report). last_verified left null."
---

1. Recognize that Verisk is a holding company with many subsidiary data products (ISO ClaimSearch insurance-claims history, Xactware, Velocity, and others), each with its own separate CCPA notice page -- there is no single unified consumer opt-out portal.
2. For Verisk's flagship consumer-relevant product, ISO ClaimSearch (used by insurers to check claims history, similar to a LexisNexis CLUE report): note that Verisk's own FAQ states it treats itself as a "service provider" to the insurers who contribute this data, and therefore does not recognize a CCPA opt-out-of-sale right for this database -- your practical options are limited to requesting access/correction rather than a sale opt-out.
3. Email privacy@verisk.com with your CCPA request (access, correction, or opt-out as applicable), including your full name and email address, and specify which Verisk product or subsidiary's data you are asking about if you know it.
4. If your concern involves a specific named subsidiary (e.g. Xactware, Velocity, VDE Service Desk), search "[subsidiary name] CCPA" on verisk.com to find that product's dedicated privacy notice, since each has separate contact details.
5. Expect Verisk to require identity confirmation before acting on access or correction requests, consistent with its general privacy notices.
