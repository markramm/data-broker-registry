---
id: bisi-com
name: "BISI (Background Information Services, Inc.)"
domain: bisi.com
category: background_check
people_search: false
tier: assisted
priority: standard
method: email
opt_out_url: "https://www.bisi.com/?pg=privacy"
opt_out_email: "compliance@bisi.com"
phone: "800-433-6010"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: ["full_name", "email"]
readd_days: null
legal_basis: [ccpa]
last_verified: 2026-07-29
source: "data-brokers-watch + tcp-research"
notes: "WebFetched bisi.com/?pg=privacy directly and it loaded a genuine CCPA privacy notice. BISI is a pre-employment/volunteer/residential background-screening company (screens people for employers and landlords), not a classic people-search address broker -- the legacy CSV's 'People Search' tag overstates it. It does publish real CCPA rights (know/access, correct, delete, limit use, opt-out of sale/sharing) with a straightforward email-based request channel and identity verification limited to name + email + state of residence (no ID upload, no fee, no CAPTCHA mentioned), so tier is assisted rather than guided. Priority standard: it's a legitimate consumer-reporting/screening business under FCRA, and the CCPA opt-out is a real but narrow lever (it mostly governs marketing-style 'sale/share', not report content, which has its own FCRA dispute channel at bisi.com/consumer)."
---

1. Go to [bisi.com/?pg=privacy](https://www.bisi.com/?pg=privacy) and review the California Privacy Notice section for the specific right you want (know/access, delete, correct, limit use, or opt-out of sale/sharing).
2. Email your request to compliance@bisi.com (or service@bisi.com for general report questions), including your full name, email address, and state of residence so BISI can verify you.
3. Expect BISI to request "any other information... to verify your identity or your request" if what you send isn't enough -- respond to keep the request moving.
4. If your request is about the *contents* of a background report BISI prepared on you (not a marketing opt-out), use [bisi.com/consumer](https://www.bisi.com/consumer) instead, or call 800-433-6010, to request your file or dispute inaccuracies.
5. There's no fee and no CAPTCHA/ID-upload gate on the CCPA request path; you should get a response directly from BISI's compliance team.
