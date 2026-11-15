---
id: catalist-us
name: "Catalist"
domain: catalist.us
category: voter_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://catalist.us/your-privacy-choices/"
opt_out_email: "privacy@catalist.us"
phone: "(800) 938-9516"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [full_name, address, dob, email, phone]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Registered California data broker (CA registry row catalist.us, Catalist LLC), a national voter-file and political data company. 2026-11-15 maintainer run: WebFetch of catalist.us/privacy-policy found a request form at /your-privacy-choices/ and phone (800) 938-9516. privacy@catalist.us is listed for general questions, not explicitly for requests. The policy says an opt-out removes your record from Catalist's files and suppresses it, while 'deletion' covers only data collected directly from you, not the products. So opt-out is the request that matters here. WebFetch of the form showed required fields: state of residence, request type, name, full street address, birthdate, email and phone, plus an emailed verification code and a penalty-of-perjury attestation. A headless render found an invisible reCAPTCHA v3 and a Cloudflare Turnstile widget (size=normal). Turnstile often passes without interaction, but a person must check, so captcha true and guided. The policy also says Catalist may ask for identification, which is why id_required is false but unconfirmed. Nothing was submitted. Not people search, but it holds name, address and voting data on most US adults, so priority high. last_verified null: no human has walked through the opt-out."
---

1. Go to Catalist's [Your Privacy Choices form](https://catalist.us/your-privacy-choices/).
2. Pick your state, then choose the option to delete and opt out of the sale of your personal information. Opting out is what removes you from Catalist's data products; "deletion" alone only covers data you gave Catalist directly.
3. Say you're making the request for yourself, and tick the declaration.
4. Enter your name, full street address, date of birth, email and phone number. Catalist says it uses the email and phone only for this request.
5. Click "Send Verification Code," enter the code from your email and click "Verify."
6. Complete the security check if one appears, tick the final attestation and submit.
7. If the form doesn't work, call (800) 938-9516 to make the same request.
