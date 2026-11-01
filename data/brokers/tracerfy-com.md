---
id: tracerfy-com
name: "Tracerfy"
domain: tracerfy.com
category: real_estate_data
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.tracerfy.com/privacy-choices"
opt_out_email: "support@tracerfy.com"
phone: "1-888-891-8053"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [full_name, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "New from the California data broker registry (registry rights_url is just www.tracerfy.com). Maintainer run 2026-11-01 fetched the homepage. Tracerfy sells pay-per-hit skip tracing: give it a property address or APN list and it returns the owners' phone numbers, emails and mailing addresses. It also sells reverse phone/email/name append and 'motivated seller' lead lists to real-estate investors, agents, contractors and lenders, via web app and API. That is a home-address/phone reseller, so people_search is true and priority is crucial. The footer link 'Do Not Sell or Share My Personal Information' goes to /privacy-choices, which was fetched and has two forms. (1) Opt-out of sale/sharing: first name, last name, street address, city and state required; ZIP optional; phone OR email (one is enough). (2) Access/Delete/Correct/Appeal: request type, self vs authorized agent, name, street address, city, state, phone, email, state of residence. The page says 'we won't ask for ID' and that Tracerfy emails to confirm receipt. The page HTML has a visible Cloudflare Turnstile widget (cf-turnstile) on the forms, so captcha is true and tier guided. Alternatives listed: email with subject 'Privacy Request' (the address is obfuscated on the page; the site's structured contact data gives support@tracerfy.com, used here as opt_out_email but not confirmed as the privacy inbox) and toll-free 1-888-891-8053. The page also says a Global Privacy Control signal is honored as an opt-out. Responses come within 45 days, extendable by 45. Nothing was submitted. last_verified left null."
---

1. Go to https://www.tracerfy.com/privacy-choices (footer link "Do Not Sell or Share My Personal Information").
2. In the opt-out form, enter your first and last name and the street address, city and state of any property you own or have owned. Tracerfy's data is keyed on property owners. Add ZIP if you like.
3. Give either a phone number or an email address (you don't need both), complete the Cloudflare check, and click "Submit Opt-Out Request."
4. To have your records deleted rather than only withheld from sale, also use the second form on the same page: choose "Deletion," select that you are the person whose information this is, fill in your name, address, phone, email and state of residence, and submit.
5. Repeat for each property address you want covered.
6. Tracerfy emails to confirm it received the request and says it responds within 45 days (up to 90 with an extension). If the form fails, call 1-888-891-8053 or email support@tracerfy.com with the subject "Privacy Request."
