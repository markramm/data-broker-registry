---
id: knowwho-com
name: Knowwho, Inc.
domain: knowwho.com
category: data_brokers
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://go.knowwho.com/lp-ccpa-request"
opt_out_email: "privacyandsecurity@knowwho.com"
phone: "1-888-566-9946"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirmed via WebFetch on kw1.knowwho.com/service/privacy/. KnowWho provides government-official and constituent contact data (B2B/political-data broker, similar space to L2). Privacy policy links a 'Do Not Sell My Personal Information' form hosted on Salesforce Pardot at go.knowwho.com/lp-ccpa-request; direct WebFetch of that URL failed on a TLS handshake error, but curl confirmed it is a live Pardot/Salesforce landing page (HTTP 302 redirect with Pardot cookies and CSP headers), consistent with a real, functioning form. Pardot forms of this kind typically do not use CAPTCHA. Policy also lists privacyandsecurity@knowwho.com and a toll-free number as alternate channels. The privacy policy states the company does not believe it 'sells' data as CCPA defines it, but still provides the mechanism. B2B/political contact-data broker, not consumer people-search -- standard priority. Simple form with no confirmed CAPTCHA/ID gating -> assisted tier."
---

1. Go to https://go.knowwho.com/lp-ccpa-request and fill out the "Do Not Sell My Personal Information" form with your name and contact details.
2. Alternatively, email privacyandsecurity@knowwho.com and state you are exercising your CCPA right to opt out of the sale of your personal information.
3. Or call KnowWho's toll-free line at 1-888-566-9946 to make the same request by phone.
4. KnowWho should acknowledge and process your request within the CCPA-mandated timeframe (typically within 45 days).
5. Keep a copy of your form submission or email for your records.
