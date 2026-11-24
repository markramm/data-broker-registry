---
id: fi-navigator-com
name: "FI Navigator"
domain: fi-navigator.com
category: b2b_contact_data
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "https://www.fi-navigator.com/remove/"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Listed in the California data broker registry (FI Navigator Corporation, Atlanta), whose rights URL is fi-navigator.com/remove/. On 2026-11-24 I fetched that page with curl. Titled 'Request to Remove Your Information', it says FI Navigator builds professional profiles (name, business and mobile phone numbers, email, job title, office address, employer, work history, social profile links, inferences) of people working at or selling to financial institutions and licenses them to customers for sales, marketing and recruiting, and that 'You can opt out of our database by submitting a removal request.' The request form is embedded in an iframe from dsr.trustsuperset.com, which I rendered in a headless browser without typing anything or submitting. That form, 'Data Subject Access Request Form', has a required Email Address field, a required Request Type select (including 'Right to Erasure' and 'Right to Opt-out of Sales'), optional First Name and Last Name fields, and a Cloudflare Turnstile 'Please verify you're human' check, so captcha is true and tier guided. Neither page says whether a confirmation email follows, so verification is null. B2B contact data about banking professionals, so priority standard. Not walked through by a human: last_verified null."
---

1. Open FI Navigator's removal page at https://www.fi-navigator.com/remove/ and scroll to the embedded "Data Subject Access Request Form".
2. Enter the email address FI Navigator might hold for you (usually a work email). First and last name are optional but help them find your profile.
3. Under "Request Type", choose "Right to Erasure" to have your profile removed. If you only want them to stop selling it, choose "Right to Opt-out of Sales" instead.
4. Complete the Cloudflare "verify you're human" check and click "Submit Request".
5. Watch your inbox for any confirmation or follow-up from FI Navigator.
