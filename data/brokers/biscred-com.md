---
id: biscred-com
name: "Biscred"
domain: biscred.com
category: b2b_contact_data
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "https://www.biscred.com/do-not-sell-my-information"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [email, full_name, other]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Listed in the California data broker registry (Biscred, LLC), whose rights URL is biscred.com/do-not-sell-my-information. On 2026-11-24 I fetched that page with curl and rendered it in a headless browser without typing anything or submitting. The page, 'Do Not Sell or Share My Information – Including CCPA and TDPSA Rights', has an 'Opt-Out' form with required First Name, Last Name and Email fields, two required dropdowns (an option select and 'State of residence'), an optional 'Country of residence' field, and a required Google reCAPTCHA (enterprise) checkbox, so captcha is true and tier guided. It says you will receive an email to verify your address and must follow its instructions to finish the request, so verification is email_confirm. Biscred sells prospect and contact data on people working in commercial real estate to sales and marketing teams, so this is a B2B contact-data broker: priority standard. The site lists support@biscred.com as a contact address, but the page does not offer it as an opt-out channel, so opt_out_email is null. I could not see the options in the first dropdown without interacting with the form. Not walked through by a human: last_verified null."
---

1. Open Biscred's opt-out page at https://www.biscred.com/do-not-sell-my-information.
2. Enter your first name, last name and the email address Biscred might hold for you (often a work email).
3. Choose an option in the first dropdown and select your state of residence. Country of residence is optional.
4. Check the reCAPTCHA box and click "Submit".
5. Open the verification email Biscred sends and follow its instructions to complete the request.
6. Repeat for each work email address you have used in commercial real estate.
