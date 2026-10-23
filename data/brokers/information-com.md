---
id: information-com
name: "Information.com"
domain: information.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://information.com/opt-out"
opt_out_email: "support@information.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-10-23 by the daily maintainer from California's data broker registry (INFORMATION.COM, LLC; registry rights URL https://information.com/privacy-rights/). That page loaded with HTTP 200 in a plain fetch. The site sells name, phone, address and email lookups, public records, criminal records and background checks, so people_search is true and priority is crucial. The privacy-rights page offers three choices: 'Right To Know' (emailed data report), 'Right To Delete' (deletes your user account and subscriptions, not your listing) and 'Right To Opt-Out' ('remove your data from our people search results, whether or not you are a member', taking 5-7 days). In a headless browser, the 'EXERT RIGHT TO OPT-OUT' button opens https://information.com/opt-out, a 'Suppression Center' for 'people search websites owned by Information.com'. The first step asks only for an email address and a terms/consent checkbox, then sends a verification email with a link to continue. The later steps (picking your records) sit behind that email link and were not seen. No CAPTCHA was visible on the first step, but the page's stylesheet has 'optout__captcha' classes, so a later step may show one; that's why the tier is guided. The footer gives support@information.com as the contact address. Nothing was submitted and no email was entered; last_verified is null."
---

1. Go to https://information.com/opt-out (the "Exert right to opt-out" button on https://information.com/privacy-rights/ leads here too).
2. Enter an email address you can check, tick the box agreeing to the terms, and submit.
3. Open the verification email from Information.com and click its link to continue in the Suppression Center.
4. Search for your listing and select every record that is you, then confirm the opt-out. Solve a CAPTCHA if one appears.
5. Allow 5-7 days for the records to drop out of Information.com's search results; search engines can take longer to catch up.
6. The "Right To Delete" option on the privacy-rights page only deletes a user account. It does not remove your listing, so use the opt-out above for that. For problems, email support@information.com.
