---
id: customers-ai
name: "Customers.ai"
domain: customers.ai
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://app.mobilemonkey.com/opt-out"
opt_out_email: "info@customers.ai"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Listed in the California data broker registry (MobileMonkey, Inc., doing business as Customers.ai). On 2026-11-23, customers.ai/opt-out (the registry's rights URL) answered 301 to https://app.mobilemonkey.com/opt-out, which I rendered in a headless browser without typing anything or submitting. The page, 'Opt Out of Tracking and Personal Data Processing', has a required Email Address field, a Zip Code field, an authorized-agent checkbox and an hCaptcha widget, so captcha is true and tier guided. It lists residents of CA, CO, CT, VA, UT, TX, OR, MT, NE, IA, IN, KY, TN, MD, DC, DE, NJ, RI and NH as eligible. Customers.ai's privacy policy (customers.ai/privacy-policy) describes an identity graph used for website-visitor identification ('associating a visitor to a customer's website with contact or profile information in our identity graph') and says it gives personal information to its customers 'to identify which consumers may be interested in their offerings', which 'may constitute a sale'. The policy says deletion requests go to info@customers.ai, that requests are verified using the email address tied to the data, and that it responds within 45 days. Consumer identity resolution for marketers, not people search, so priority high. Not walked through by a human: last_verified null."
---

1. Open the Customers.ai opt-out form at https://app.mobilemonkey.com/opt-out (customers.ai/opt-out redirects there).
2. Enter the email address you want suppressed, and your zip code.
3. Solve the hCaptcha and click "Opt-Out".
4. To have your data deleted rather than just suppressed, email info@customers.ai and ask for deletion of the personal information tied to that email address. Customers.ai says it verifies requests using that email address and responds within 45 days.
5. Repeat for each email address you use, since the identity graph matches by email.
