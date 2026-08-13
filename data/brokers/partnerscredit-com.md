---
id: partnerscredit-com
name: "Partners Credit And Verification Solutions"
domain: partnerscredit.com
category: credit_verification
people_search: false
tier: guided
priority: standard
method: portal
opt_out_url: "https://www.optoutprescreen.com"
opt_out_email: null
phone: "888-567-8688"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, address]
readd_days: null
legal_basis: [none]
last_verified: null
source: "dbw+tcp-research"
notes: "SAME ENTITY / SAME OPT-OUT MECHANISM as creditinterlink-com.md (already authored in a prior round): partnerscredit.com is Partners Credit And Verification Solutions' primary/marketing domain, while creditinterlink.com hosts the same company's consumer-facing pcvs_* pages (advcredit.creditinterlink.com). Both share the pkarbo@creditinterlink.com contact. curl-fetched http://www.partnerscredit.com/pcvs_privacy.html and http://www.partnerscredit.com/consumers/pcvs_optout.html directly (both HTTP 200/301->200, static HTML) this session and confirmed the opt-out page under this domain independently redirects/points to the same industry-wide FCRA prescreen system: www.optoutprescreen.com or 888-567-8688, covering the four major credit bureaus (Experian, TransUnion, Equifax, Innovis). The company is a California-based mortgage/consumer-lending credit-verification and background-check reseller regulated under FCRA, not a people-search site. No CCPA-specific mechanism was found on partnerscredit.com itself (the privacy policy fetched this session made no CCPA mention); opt-out is the shared federal/bureau prescreen system, same as creditinterlink-com.md. Authored as a distinct domain entry per instructions, since it is a genuinely separate hostname the company operates, but the underlying opt-out process, contact person, and impact are identical to the creditinterlink-com.md entry -- treat the two as the same removal action performed once. Not independently re-verified beyond this session's fetch; last_verified left null."
---

1. Go to https://www.optoutprescreen.com, the official consumer opt-out system jointly operated by the major credit bureaus (Equifax, Experian, TransUnion, Innovis) that Partners Credit And Verification Solutions draws its prescreen lists from.
2. Alternatively, call 888-567-8688 (the same opt-out system, by phone) if you prefer not to use the website.
3. Choose either a 5-year opt-out or a permanent opt-out; the permanent option requires signing and mailing a confirmation form.
4. Provide your name and address as prompted -- this is the minimum information the bureaus need to match and suppress your prescreen record.
5. Note this single opt-out also covers creditinterlink.com (data/brokers/creditinterlink-com.md in this dataset) -- Partners Credit And Verification Solutions operates both domains and both route to the same bureau-run system, so you do not need to repeat this process for each domain.
6. For questions about the company's own handling of your data, you can also contact them directly at pkarbo@creditinterlink.com.
