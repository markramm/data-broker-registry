---
id: cogensia-com
name: Cogensia LLC
domain: cogensia.com
category: marketing_data_broker
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "<verify: locate the specific opt-out/CCPA form under cogensia.com's Privacy Policy section -- CA AG registration says forms are 'readily available on our company website under our Privacy Policy section' but no direct form URL was found>"
opt_out_email: "info@cogensia.com"
phone: null
captcha: false
id_required: true
phone_required: false
charges_fee: false
required_fields: [full_name, address, email, gov_id]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "Cogensia LLC is a registered CA data broker (registration 186112) providing B2B/B2C marketing data and analytics services (list brokerage, data hygiene, co-op database). WebFetch of the CA AG registration page (oag.ca.gov/data-broker/registration/186112) rendered successfully and states opt-out forms are available on cogensia.com under its Privacy Policy section, but did not give a direct URL, so opt_out_url is left as a verify-placeholder per instructions and last_verified is null. Notably, the same registration page states that consumers seeking DELETION of their information must validate identity via a cancelled check or utility bill sent to info@cogensia.com -- a government/financial-ID-adjacent verification step, which is why id_required is true and tier is guided despite this being a B2B-leaning marketing data broker (priority kept standard, not high/crucial, since Cogensia's core business is list brokerage/co-op data rather than address/phone lookups on individuals). A secondary source (dataremoval.ca) described a different process citing Canadian PIPEDA, which reads as templated/generic third-party opt-out-guide boilerplate rather than Cogensia-specific fact and was NOT relied on for this entry -- only the CA AG registration (a primary source) was used for the frontmatter."
---

1. Go to cogensia.com and look under the Privacy Policy section of the site for their opt-out/CCPA request form (the exact form URL was not confirmed in this research pass -- verify the current path before relying on it).
2. If you specifically want deletion of your information (not just an opt-out of sale), skip the web form and email info@cogensia.com directly.
3. Attach a copy of a cancelled check or a utility bill to verify your identity -- Cogensia's own CA data-broker registration states this is required before they will process a deletion request. Redact sensitive numbers (account numbers, routing numbers) you don't need to disclose, keeping only what confirms your name and address.
4. State clearly that you are requesting deletion of your personal information under the CCPA/CPRA.
5. Keep a copy of your email and any reply as your record of the request.
