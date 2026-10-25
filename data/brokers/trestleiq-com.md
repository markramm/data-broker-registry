---
id: trestleiq-com
name: "Trestle (Trestle Solutions, Inc.)"
domain: trestleiq.com
category: identity_verification
people_search: true
tier: guided
priority: high
method: form
opt_out_url: "https://portal.trestleiq.com/do-not-sell"
opt_out_email: "privacy@trestleiq.com"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [full_name, phone, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-10-24 by the daily maintainer from California's data broker registry (Trestle Solutions, Inc.; registry rights URL https://trestleiq.com/privacy-policy/, email privacy@trestleiq.com). Trestle sells phone and identity data APIs to businesses: reverse phone lookup, caller identification, identity and lead verification, and phone-number validation. Its privacy policy (loaded headless, last updated 2025-12-10) says it collects name, email, physical address, phone numbers, line type, carrier and alternative phone numbers from public sources and third-party data providers. That is a phone/identity lookup product, so people_search is true; it is sold to businesses through an API rather than as a public search site, so priority is high rather than crucial. The policy says to use the 'Do Not Sell My Personal Information' footer link to opt out of sale/sharing, and to email privacy@trestleiq.com to access, delete or correct data. The trestleiq.com footer link goes to https://portal.trestleiq.com/do-not-sell, which embeds a form from dsr.trustsuperset.com. Loaded headless, that form ('Trestle's Opt out Form') requires first name, last name, phone number, email and a request type (options include Right to Opt-out of Sales and Right to Erasure); middle name, address line, state and ZIP are optional. It shows a 'Please verify you're human' check, so captcha is true and the tier is guided. No confirmation step is described. Nothing was submitted; last_verified is null."
---

1. Go to https://portal.trestleiq.com/do-not-sell (the "Do Not Sell My Personal Information" link in the trestleiq.com footer). Dismiss the cookie banner if the form doesn't show.
2. Enter your first and last name, the phone number you want suppressed, and your email address. Address, state and ZIP are optional.
3. Under "Request Type", choose "Right to Opt-out of Sales".
4. Complete the "verify you're human" check and submit.
5. Submit a second request with "Right to Erasure" if you also want your data deleted, and repeat for any other phone numbers you use.
6. Alternatively, email privacy@trestleiq.com to ask for deletion and an opt-out of sale or sharing.
