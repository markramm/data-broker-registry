---
id: spydialer-com
name: "Spy Dialer, Inc."
domain: spydialer.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.spydialer.com/optout"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: data-brokers-watch
notes: "2026-11-04 maintainer update (page-monitor #178): the old optout.aspx wizard (pick state, CAPTCHA, then name + phone) is gone. Rendered https://www.spydialer.com/optout.aspx headless today: it now redirects (HTTP 200) to https://www.spydialer.com/optout, titled 'Do Not Sell/Right to Opt-out', which is also where the footer 'Remove My Info' link points. The new flow has two stages: (1) choose subject or authorized agent, enter first/middle/last name and email, tick the consent box and pass the anti-bot check (a Cloudflare Turnstile widget and a reCAPTCHA frame were both present); (2) Spy Dialer emails a link, valid 24 hours, to the actual opt-out form, where you enter details matching the record to remove; then a confirmation page and email, with removal at least 3 days after approval. The stage-2 form is behind the emailed link and was not seen, so its exact fields (probably phone number) are unconfirmed. Nothing was submitted. Original URL came from data-brokers-watch. CAPTCHA + email-link multi-step -> guided. last_verified left null."
---

1. Go to https://www.spydialer.com/optout (the "Remove My Info" link in Spy Dialer's footer goes to the same page).
2. Under "I am", choose "The subject of the request" (or "An authorized agent" if you are filing for someone else, which adds agent name and email fields).
3. Enter your first name, optional middle name, last name, and email address, then tick the consent box.
4. Complete the anti-bot check and click "Continue."
5. Open the email Spy Dialer sends and click its link within 24 hours (after that you must request a new one).
6. On the opt-out form the link opens, enter the details exactly as they appear on the listing you want removed (for example the phone number and name) and submit. Fill in every field; incomplete forms slow the request down.
7. You should get a confirmation page and a confirmation email. Allow at least 3 days after approval, then search your number on Spy Dialer to confirm the listing is gone; repeat if it reappears.
