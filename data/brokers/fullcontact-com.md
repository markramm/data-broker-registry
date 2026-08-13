---
id: fullcontact-com
name: FullContact, Inc.
domain: fullcontact.com
category: identity_resolution
people_search: true
tier: guided
priority: crucial
method: portal
opt_out_url: "https://platform.fullcontact.com/your-privacy-choices"
opt_out_email: "privacy@fullcontact.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, full_name]
verification: identity_confirm
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: "2026-08-13"
source: "dbw+tcp-research+chrome-verified"
notes: "FullContact is a well-documented identity-resolution/identity-verification data broker that matches contact records (email, phone, social profiles) to a unified identity graph, sold to businesses for enrichment and fraud prevention -- high personal-safety impact given the breadth of matched PII. WebFetch on fullcontact.com/privacy-center/ confirmed a live Privacy Portal at https://platform.fullcontact.com/your-privacy-choices with explicit 'Right to Delete' and 'Right to Opt-Out of Sales and Targeted Advertising' language, plus an interactive webform reachable through that portal and a privacy@fullcontact.com email as an alternate channel. The legacy CSV's dashboard.fullcontact.com/claim URL was checked and does NOT resolve (DNS failure) -- it appears stale/retired, so the current platform.fullcontact.com/your-privacy-choices URL was used instead. Chrome-driven check (2026-08-13): CONFIRMED. Page took ~8s to fully render (loading skeleton before content -- worth knowing if a future automated check gives up too early) but then showed exactly 5 options: Access My Data / Correct My Data / Do Not Sell or Share My Data / Limit Sharing Of My Sensitive Data / Delete My Data. Clicked into 'Do Not Sell or Share My Data': first step is a country selector (defaulted to United States), no CAPTCHA seen through that step. California requests additionally require signed written permission or power of attorney if submitted by an agent."
---

1. Go to https://platform.fullcontact.com/your-privacy-choices, FullContact's Privacy Portal.
2. Select the option for deleting your personal data (Right to Delete) or opting out of data sales/targeted advertising, depending on what you want.
3. Complete the interactive webform with your name and email address so FullContact can locate and process your record.
4. Be ready to verify your identity if asked -- FullContact's policy states it may need to confirm identity/clarify the request before completing it.
5. If you'd rather not use the portal, email privacy@fullcontact.com directly with your full name, the email addresses associated with your online accounts, and a clear statement that you are requesting deletion of your personal data and opting out of any sale/sharing of it.
6. If you are a California resident submitting the request through an authorized agent rather than yourself, be aware FullContact requires signed written permission or power-of-attorney documentation from you first.
7. Watch for a confirmation email and follow up if you don't receive a response within the timeframe required by applicable law (typically 45 days under CCPA/CPRA).
