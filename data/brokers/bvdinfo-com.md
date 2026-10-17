---
id: bvdinfo-com
name: Bureau van Dijk Electronic Publishing Ltd. (a Moody's company)
domain: bvdinfo.com
category: marketing_data_broker
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "https://www.bvdinfo.com/en-gb/legal/personal-data-request-form"
opt_out_email: "privacy@bvdinfo.com"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, address]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "2026-10-16 maintainer run (Fixes #32): https://www.bvdinfo.com/en-gb/legal/personal-data-request-form now redirects to a Moody's-hosted Alchemer survey, https://survey.alchemer.com/s3/8534043/Do-Not-Sell-Request (HTTP 200, title 'Do Not Sell Request - 2026'). opt_out_url is kept on the bvdinfo.com address because the survey's title carries a year and may be replaced; the redirect is what users land on today. The form is for California residents. It requires first and last name, email, a California street address, city and ZIP, a California-residence confirmation, which Moody's product the request covers (Moody's Analytics Pulse or Moody's CRE Solutions/Catylist-Reis; one per form), and the request type (access, deletion, correction, right to know, opt out, limit sensitive PI). The survey has a visible reCAPTCHA (div.g-recaptcha, data-size=compact), so captcha: true; tier stays guided. Nothing was submitted. Background kept from the earlier pass: Bureau van Dijk, now part of Moody's, sells company-intelligence data (e.g. Orbis) that includes limited personal data on company owners, directors and commercial real-estate brokers/tenants; it is registered as a CA data broker and lists privacy@bvdinfo.com. last_verified stays null."
---

1. Go to https://www.bvdinfo.com/en-gb/legal/personal-data-request-form. It redirects to Moody's "Do Not Sell Request" survey on survey.alchemer.com.
2. Choose whether you are making the request for yourself or as an authorized agent.
3. Enter your first and last name, email address, and California street address, city and ZIP code.
4. Pick which Moody's product the request applies to: Moody's Analytics Pulse (trade-credit data on people in payment/procurement roles) or Moody's CRE Solutions (Catylist/Reis commercial real-estate data). The form takes one per submission, so fill it in twice to cover both.
5. Select "Opt out" (or "Deletion") as the request type, confirm you are a California resident, complete the reCAPTCHA and submit.
6. If the form is unavailable or you are not a California resident, email privacy@bvdinfo.com with the same request, naming the product and describing how you appear in it.
7. Because much of this data comes from public company filings and records, full deletion may not be possible where the source stays public. Expect a reply within the CCPA window (up to 45 days).
