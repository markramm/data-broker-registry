---
id: thedatagroup-com
name: The Data Group
domain: thedatagroup.com
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://thedatagroup.com/privacy/consumer-optout-request-form/"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, other]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "The Data Group is a data append/enrichment and mailing-list broker; its own site footer discloses 'The entity maintaining this website is a data broker under Texas law,' registered with the Texas Secretary of State. It sells email/phone/demographic/psychographic data-append services and operates opt-out mechanisms for California plus a listed multi-state group (CO, CT, DE, IN, IA, MT, NJ, FL, OR, NE, TN, TX, UT, VA, VT, NH, MN). Not people_search -- this is a B2B/marketing append vendor, not an individual-lookup product. Updated 2026-10-31 by the daily maintainer after page-monitor issue #156: the privacy page links to the Consumer Privacy Request Form at https://thedatagroup.com/privacy/consumer-optout-request-form/ (curl, HTTP 200). That page says privacy requests 'cannot be processed by email' and that requests sent to compliance@thedatagroup.com get an automated reply pointing to the form, so the email route was removed and opt_out_email set to null (compliance@thedatagroup.com remains a general-questions contact). The Ninja Forms config embedded in the page defines the form: First Name, Last Name, US State, Zip5, Email and a legal-certification checkbox are required; Address, City and Phone are optional; it includes a reCAPTCHA field with size 'visible' (v2 checkbox), so captcha: true. The form scripts are lazy-loaded and did not render in a headless browser, so the widget itself was not seen on screen. The CAPTCHA the monitor flagged on /privacy/ itself belongs to an email-only footer form (Cloudflare Turnstile), not the opt-out. Nothing was submitted; last_verified left null."
---

1. Go to The Data Group's Consumer Privacy Request Form at https://thedatagroup.com/privacy/consumer-optout-request-form/. Email requests are not accepted: The Data Group replies to them with a pointer to this form.
2. Enter your first and last name, US state, 5-digit ZIP code and email address. Address, city and phone are optional, but adding the address and phone they may hold helps them match your record.
3. Check the box certifying that you are the person whose information you are submitting.
4. Complete the reCAPTCHA ("I'm not a robot") and submit. If the form won't submit, the page suggests turning off any VPN and trying again.
5. The Data Group says it will remove your information within the time required by law. The privacy policy covers California and the multi-state group it lists (CO, CT, DE, IN, IA, MT, NJ, FL, OR, NE, TN, TX, UT, VA, VT, NH, MN).
