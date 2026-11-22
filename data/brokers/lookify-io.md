---
id: lookify-io
name: "Lookify"
domain: lookify.io
category: people_search
people_search: true
tier: auto
priority: crucial
method: email
opt_out_url: "https://lookify.io/opt-out"
opt_out_email: "privacy@lookify.io"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [full_name, email, phone]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-11-10 by the daily maintainer from the California data broker registry row for Lookify.io (contact support@lookify.io). Rendered https://lookify.io/ccpa-privacy-statement headless (HTTP 200, last updated July 1, 2026). It says Lookify collects and sells names, emails, phone numbers (including mobile), social profile URLs and employment history, and that California residents can opt out of sale/sharing or ask for deletion either through the Privacy Request Form at https://lookify.io/opt-out or by emailing privacy@lookify.io. Requests must be verifiable; Lookify says it responds within 45 days and treats a deletion it can't verify as an opt-out of sale. The homepage (title 'Reverse Phone Number Lookup and Data Search') sells a reverse phone lookup that returns the owner's full name, email, alternate phones, employment and social profiles, so this is treated as a people-search site -> crucial. The opt-out form itself sat behind a Cloudflare 'Performing security verification' challenge in both curl (HTTP 403) and headless Chromium, so its fields and any CAPTCHA weren't seen; the entry uses the documented email route (-> auto) and lists the form as an alternative. required_fields is a best guess (name, email, and the phone number(s) Lookify shows). Nothing was submitted or sent. last_verified left null."
---

1. Email privacy@lookify.io from an address you can check, with the subject "CCPA request: delete and do not sell or share my personal information."
2. In the body, give your full name, the phone number(s) Lookify may show for you (look one up on lookify.io first if you want to see what it returns), and any email addresses it may hold. Ask Lookify to delete your personal information and to stop selling or sharing it.
3. Lookify may reply asking you to verify your identity. Answer from the same email address.
4. Alternatively, use the Privacy Request Form at https://lookify.io/opt-out. It is behind a Cloudflare check, so expect to complete a browser challenge first.
5. Keep a copy of your request and the date. Lookify says it responds within 45 days; if you hear nothing, reply to your original message.
