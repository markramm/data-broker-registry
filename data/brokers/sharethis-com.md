---
id: sharethis-com
name: ShareThis
domain: sharethis.com
category: adtech_audience_data
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://sharethis.com/data-subject-privacy-request/"
opt_out_email: "privacy@sharethis.com"
phone: "1-800-272-1765"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on sharethis.com/privacy/ confirmed ShareThis is an adtech/social-sharing company that collects pseudonymous cross-site browsing data via its widely embedded share buttons/analytics tags and uses it for targeted advertising -- a genuine, large-scale data broker (widely covered in prior data-broker reporting for exactly this reason). It runs a dedicated Data Subject Privacy Request form at sharethis.com/data-subject-privacy-request/, plus privacy@sharethis.com and access@sharethis.com emails, a toll-free CCPA hotline (1-800-272-1765), and honors DAA/EDAA industry opt-out tools. No CAPTCHA or ID mentioned in fetched text. High priority: large-scale cross-site tracking broker, though not a people-search/home-address product, so not crucial. 2026-10-15 maintainer re-check (Refs page-monitor #28): fetched the request page (HTTP 200). The form (request type: opt-out of hashed-email use / deletion / correction, plus email address) has a 'CAPTCHA Verification' step with a visible reCAPTCHA v2 widget (div.g-recaptcha) that enables the submit button, so captcha -> true and tier assisted -> guided. Nothing was submitted."
---

1. Go to https://sharethis.com/data-subject-privacy-request/, choose the request type (opt-out of their use of your hashed email, or deletion), enter your email address, complete the CAPTCHA, and submit.
2. Alternatively, email privacy@sharethis.com (general privacy questions) or access@sharethis.com (data access requests) directly.
3. California residents can also call the toll-free CCPA hotline at 1-800-272-1765 to submit a request by phone.
4. For broader ad-tracking opt-out beyond ShareThis specifically, use the Digital Advertising Alliance's tool at optout.aboutads.info (US) or Your Online Choices at youronlinechoices.eu (EU), and enable "Limit Ad Tracking" on mobile devices.
5. Watch for a confirmation of your request; ShareThis's policy does not specify an exact turnaround time in the fetched text.
