---
id: idanalytics-com
name: "ID Analytics, LLC"
domain: idanalytics.com
category: identity_risk_data_broker
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://consumer.risk.lexisnexis.com/request#california"
opt_out_email: null
phone: "1-888-497-0011"
captcha: true
id_required: true
phone_required: false
charges_fee: false
verification: id_upload
required_fields: [full_name, address, dob, gov_id]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "idanalytics.com (301) redirects entirely to risk.lexisnexis.com -- ID Analytics was acquired by LexisNexis Risk Solutions years ago and no longer operates as a standalone site or product brand; the domain now serves LexisNexis's general Credit Risk product page. WebFetch on that page and on consumer.risk.lexisnexis.com/request confirmed a real, working LexisNexis Risk Solutions consumer portal covering the former ID Analytics data: full disclosure/deletion requests require first/last name, street address, city, zip, date of birth, plus either SSN or driver's license number+state. The opt-out-only path ('Do Not Sell or Share My Personal Information') is explicitly stated to NOT require SSN/driver's license, but full data-access or deletion requests do, and the identity check pushed id_required/verification to reflect the stricter deletion path since that's the meaningful removal action for this dataset's purpose. No CAPTCHA was mentioned in the fetched content. Kept as a broker entry (rather than dropped) because the underlying data and legal entity are live and reachable, just consolidated under the LexisNexis Risk Solutions umbrella and portal rather than a dedicated idanalytics.com opt-out page. 2026-10-15 maintainer re-check (Refs page-monitor #24): fetched consumer.risk.lexisnexis.com/request (HTTP 200). A reCAPTCHA widget (div#google-captcha-div with a sitekey, rendered explicitly by the page) sits directly above 'Submit Request', so captcha -> true (tier was already guided). Nothing was submitted."
---

1. Go to the [LexisNexis Risk Solutions consumer request portal](https://consumer.risk.lexisnexis.com/request#california) (the domain idanalytics.com now redirects here, since ID Analytics is part of LexisNexis Risk Solutions).
2. Choose "Do Not Sell or Share My Personal Information" for a straightforward opt-out, or "Full Opt-Out" / "Partial Opt-Out" as offered -- these do not require SSN or driver's license information.
3. If you instead want your underlying record deleted (not just opted out of sale), select the deletion/data-access request option; this requires your first and last name, street address, city, zip code, date of birth, and either your Social Security Number or driver's license number and state.
4. Complete the CAPTCHA and submit the form online, or call 1-888-497-0011 (Monday-Friday, 8am-7pm ET) to make the same request by phone.
5. For data-access requests, expect a letter by U.S. mail (roughly 10 days) with instructions to view your report online; opt-out requests are generally processed without that follow-up letter.
