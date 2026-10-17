---
id: publicdatacheck-com
name: "Public Data Check"
domain: publicdatacheck.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.publicdatacheck.com/help-center/privacy-requests"
opt_out_email: "privacyinfo@publicdatacheck.com"
phone: "1-800-950-0953"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [full_name, address, email, other]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-10-17 by the daily maintainer from California's data broker registry (National Data Analytics, LLC, dba publicdatacheck.com, listing privacyinfo@publicdatacheck.com). Fetched https://www.publicdatacheck.com/help-center/privacy-requests directly (HTTP 200, 'Personal Information Privacy Requests'). The form offers Do Not Sell My Info, Delete My Info, or Request a Copy, and requires first and last name, city, state, ZIP, an age range and a confirmation email (customer ID only for existing customers). It has a Cloudflare Turnstile widget (div.cf-turnstile, 'Please confirm you are human'). Its FAQ says you search the database, pick your record, then confirm via a verification email, and a second email confirms the opt-out; removal is free, needs no membership and usually takes effect within 24 hours, and Daniel's Law covered persons can ask support for manual help. The layout, fields and FAQ match the publicinfoservices.com, searchpublicrecords.com and kidslivesafe.com privacy pages (proposed in PR #72), so this looks like the same shared platform under a different registered LLC; kept as a separate entry. People-search reports -> people_search true, priority crucial; CAPTCHA -> guided. Nothing was submitted; last_verified null."
---

1. Go to https://www.publicdatacheck.com/help-center/privacy-requests.
2. Choose "Do Not Sell My Info" (or "Delete My Info") as the request type.
3. Enter your first and last name, city, state, ZIP code and age range, plus an email address where you can receive the confirmation. Leave Customer ID blank unless you have an account.
4. Complete the "confirm you are human" check and click Continue.
5. In the search results, select the record that is you.
6. Open the verification email from Public Data Check and confirm the request. If it doesn't arrive within 15 minutes, check spam and the address you typed.
7. Wait for the email confirming the opt-out was processed, then check again after about 24 hours that your record is gone. If it is still there, call 1-800-950-0953.
8. If you are covered by Daniel's Law (judges, prosecutors, law enforcement and their households), you can contact support for help instead of using the automated form.
