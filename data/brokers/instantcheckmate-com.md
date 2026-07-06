---
id: instantcheckmate-com
name: "Instant Checkmate"
domain: instantcheckmate.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: portal
opt_out_url: "https://suppression.peopleconnect.us/login"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, full_name, dob]
readd_days: 2
legal_basis: [ccpa]
last_verified: null
source: "data-brokers-watch + tcp-verified"
notes: "MIGRATED research_note: PeopleConnect suppression portal. This is the shared opt-out hub for PeopleConnect's whole network -- one request here also covers TruthFinder, Intelius, and USSearch (and other files in this batch, e.g. instantpeoplefinder-com, intelregistry-com, point at Intelius/this same corporate family). Direct WebFetch returned only a bare page title (JS-rendered app, no static content), so not freshly confirmed by fetch; assessed from consistent, detailed third-party opt-out guides (OneRep, iolo, PrivacyOn, security.org) describing today's flow: email verify -> DOB -> full legal name -> select matching record -> re-verify identity if needed -> set 'Desired Behavior' to Suppressed. No CAPTCHA, no ID upload, no account/payment required per those sources, but it's a real multi-stage identity-matching flow, not a single deep-linkable form, so tier is guided. Records reportedly suppressed within ~48 hours; readd_days set to 2 as a rough re-check nudge, though PeopleConnect does not publish a formal re-scrape cadence."
---

1. Go to the PeopleConnect Suppression Center (linked above) -- this single portal also covers TruthFinder, Intelius, and USSearch, so you only need to do this once.
2. Enter your email address and agree to the Terms and Privacy Policy, then submit.
3. Check your inbox (including spam) for a confirmation email from PeopleConnect and click "Verify email."
4. Enter your date of birth, confirm it's correct, and click Continue.
5. Enter your first, middle, and last legal name, confirm it, and click Continue.
6. Select the record that matches you from the list shown; if your identity isn't automatically verified, you may need to confirm it via an email address or phone number tied to that record.
7. Set the "Desired Behavior" dropdown to "Suppressed" and click Save -- your listing should be hidden within about 48 hours.
