---
id: phonebooks-com
name: "Phonebooks.Com (Now Redirects To Spy Dialer)"
domain: phonebooks.com
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
notes: "2026-11-08 maintainer update (page-monitor #196): phonebooks.com no longer has its own opt-out. Fetched https://www.phonebooks.com/contact.html and https://www.phonebooks.com/ today: both answer HTTP 301 to https://www.spydialer.com/, so the whole site now redirects to Spy Dialer, and the old contact.html form is gone. Fetched https://www.spydialer.com/optout (HTTP 200, 'Do Not Sell/Right to Opt-out'): it is the same two-stage process the old phonebooks.com form used ('I am: The subject of the request', name + email, consent box, emailed link to a follow-up form), now with an anti-bot check (Cloudflare Turnstile markup present). This entry therefore points at Spy Dialer's opt-out and matches the spydialer-com entry. The stage-2 form behind the emailed link was not seen. Nothing was submitted. Earlier research (PRC listing, onerep guide) tied phonebooks.com to the Intelius/PeopleConnect network, so the PeopleConnect suppression center is kept as an extra step; whether that link still holds after the redirect is unconfirmed. CAPTCHA + email-link multi-step -> guided. last_verified left null."
---

1. Note that phonebooks.com now redirects to spydialer.com, so phonebooks.com listings are removed through Spy Dialer's opt-out.
2. Go to https://www.spydialer.com/optout.
3. Under "I am", choose "The subject of the request" (or "An authorized agent" if you are filing for someone else).
4. Enter your first name, optional middle name, last name, and email address, tick the consent box, complete the anti-bot check, and click "Continue."
5. Open the email Spy Dialer sends and click its link within 24 hours.
6. On the form the link opens, enter the details exactly as they appear on the listing you want removed and submit.
7. Keep the confirmation email. Allow at least 3 days after approval, then search your number on Spy Dialer to confirm the listing is gone.
8. Because phonebooks.com was historically part of the Intelius/PeopleConnect network, also consider opting out at the PeopleConnect Suppression Center (suppression.peopleconnect.us).
