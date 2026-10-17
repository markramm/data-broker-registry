---
id: compactlists-com
name: Compact Information Systems
domain: compactlists.com
category: marketing_data_broker
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "https://privacy.deepsync.com/request/opt-out"
opt_out_email: "privacy.compliance@deepsync.com"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: "identity_questions"
required_fields: [full_name, email, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "2026-10-16 maintainer run (Fixes #34): privacy.compactlists.com/request/opt-out now redirects to https://privacy.deepsync.com/request/opt-out (HTTP 200, 'Do Not Sell My Personal Information, Deep Sync'). This dataset already routes accudata-com and aslmarketing-com to the same Deep Sync privacy center. The page itself does not name Compact Information Systems, so the link rests on the redirect from Compact's own privacy subdomain. The form asks who the request is for (yourself, a deceased person, someone you represent), first and last name, email, phone, a primary address (up to five more), and which actions you want (do not sell/share, no targeted advertising, no profiling, limit sensitive PI, delete). It has a Cloudflare Turnstile widget (div.cf-turnstile) and says identity is verified through dynamically generated questions before a request is completed. captcha: true, tier assisted -> guided, verification identity_questions. The page lists privacy.compliance@deepsync.com for anything the form cannot handle; that replaces the old compactlists.com address. Nothing was submitted. Compact Information Systems is a CA-registered marketing/mailing-list broker (postal and demographic data). last_verified stays null."
---

1. Go to https://privacy.deepsync.com/request/opt-out. Compact Information Systems' old privacy site now redirects to this Deep Sync privacy center.
2. Say who the request is for (yourself, a deceased person, or someone you are authorized to represent).
3. Enter your first and last name, email address, phone number and primary mailing address. Add past addresses (up to five) and extra emails or phone numbers so every record is found.
4. Tick the actions you want: do not sell or share, no targeted advertising, no profiling, limit sensitive information, and/or delete.
5. Complete the Cloudflare check and submit. Deep Sync verifies your identity with generated questions before it acts on the request, so answer them when they appear.
6. For anything the form can't handle (more than five addresses, removal from client data, or not wanting a suppression record kept after deletion), email privacy.compliance@deepsync.com.
