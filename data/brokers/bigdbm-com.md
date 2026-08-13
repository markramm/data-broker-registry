---
id: bigdbm-com
name: BIGDBM
domain: bigdbm.com
category: marketing_data_broker
people_search: true
tier: guided
priority: high
method: portal
opt_out_url: "https://www.bigdbm.com/privacy.html"
opt_out_email: "privacy@bigdbm.com"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [full_name, email, phone, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch directly rendered a BIGDBM consumer-rights-request page confirming the process, corroborated by JoinDeleteMe's opt-out guide. BIGDBM is a registered CA data broker selling consumer identity/marketing data (name, address, email, phone-level records) at bulk scale to businesses -- their own site advertises 'identity data' products. Opt-out is via a form (reachable from the privacy page or footer 'Do Not Sell My Personal Information' link, also mirrored at a separate optoutccpa.com portal) requiring first/last name, email or phone, address/city/state/zip, and a reCAPTCHA ('I'm not a robot') -- no government ID required. CAPTCHA-gated -> guided tier. Sells individual-level identity data used for lookups/marketing -> people_search true, high priority (not marked crucial since it's primarily a B2B marketing-data feed rather than a consumer-facing lookup tool, but the personal data at stake is real)."
---

1. Go to https://www.bigdbm.com/privacy.html (or scroll to the site footer and click "Do Not Sell My Personal Information").
2. Select "Right to Opt Out of Sale" and open the dedicated Opt Out of Sale form.
3. Enter your first name, last name, and at least one contact identifier (email or phone), plus your address, city, state, and zip -- or use the alternate identifier combination the form offers.
4. Complete the "I'm not a robot" CAPTCHA verification and submit the form.
5. Expect processing within about 7 business days; alternatively, email privacy@bigdbm.com if you need help or don't receive confirmation.
