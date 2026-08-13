---
id: qualfon-com
name: Qualfon
domain: qualfon.com
category: bpo_data_broker
people_search: false
tier: auto
priority: standard
method: email
opt_out_url: "https://www.qualfon.com/privacy-policy/consumer-privacy-choices/"
opt_out_email: "consumerprivacy@qualfon.com"
phone: "8883802190"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirmed via curl (server-rendered HTML) that qualfon.com is primarily a BPO/call-center outsourcing company, but its own privacy policy discloses selling/sharing personal information with third parties including 'data brokers,' 'ad networks,' and other partners, so it is treated as a broker for opt-out purposes. Fetched privacy-policy page shows a mailto: link for consumerprivacy@qualfon.com and a dedicated /privacy-policy/consumer-privacy-choices/ page, plus a toll-free number (888) 380-2190 for submitting requests. Because a working direct opt-out email exists, tier set to auto per method:email rule even though a portal also exists as an alternative. last_verified left null -- I did not render the interactive consumer-privacy-choices form itself, only confirmed the links/email exist on the fetched policy page."
---

1. Email consumerprivacy@qualfon.com and state that you are a California (or other applicable state) resident requesting that Qualfon not sell or share your personal information, and/or that Qualfon delete personal information it holds about you.
2. Include your full name and the email address you want Qualfon to reply to, so they can locate and verify your request.
3. Alternatively, submit the same request through Qualfon's online form at https://www.qualfon.com/privacy-policy/consumer-privacy-choices/, or by calling their toll-free privacy line at (888) 380-2190.
4. Watch for a confirmation or follow-up verification email from Qualfon.
5. If you don't hear back within a few weeks, follow up by email, since response times for BPO-style privacy teams can be slow.
