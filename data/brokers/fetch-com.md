---
id: fetch-com
name: "Fetch (Fetch Rewards, LLC)"
domain: fetch.com
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://preferences.fetch.com/"
opt_out_email: "privacy@fetch.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: identity_check
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-11-09 by the daily maintainer from the California data broker registry row for Fetch Rewards, LLC (contact privacy@fetch.com; rights URLs fetch.com/privacy-policy and preferences.fetch.com). Fetch is a consumer receipt-scanning rewards app. Fetched https://fetch.com/privacy-policy (HTTP 200): it says sale/sharing opt-outs are made through the 'Do Not Sell or Share My Personal Information' link at preferences.fetch.com and honored within 15 business days; deletion and access requests go through the same page or by email to privacy@fetch.com; no account is needed to make a request, and Fetch says it will try to answer any U.S. resident; it confirms receipt within 10 business days and answers verified requests within 45 days, and a deletion must be confirmed separately. Rendered https://preferences.fetch.com/ headless (a DataGrail 'Privacy Request Center'): country and state pickers, then 'Start Opt Out Request', 'Start Access Request' and 'Start Deletion Request' buttons. The form behind those buttons was not opened, so its exact fields and whether it has a CAPTCHA are unknown; required_fields is a best guess and the tier is guided for that reason. Consumer app with a working opt-out -> high priority. Nothing was submitted. last_verified left null."
---

1. Go to https://preferences.fetch.com/ (Fetch's Privacy Request Center). You don't need a Fetch account.
2. Pick your country and state of residence.
3. Click "Start Opt Out Request" to stop Fetch selling or sharing your personal information, and fill in the form it opens with the details Fetch asks for (expect at least your name and email address).
4. Go back and click "Start Deletion Request" to ask Fetch to delete your information as well. If you use the Fetch app, use the email address tied to your account.
5. Watch for an email from Fetch: it confirms receipt within 10 business days, may ask you to verify your identity, and asks you to confirm separately that you want your data deleted.
6. If the web form doesn't work for you, email privacy@fetch.com with the same request (opt out of sale/sharing and delete my personal information), your full name and the email address Fetch may know you by.
7. If Fetch denies a request, you can appeal within 60 days by emailing privacy@fetch.com with the subject "Privacy Request Decision Appeal."
