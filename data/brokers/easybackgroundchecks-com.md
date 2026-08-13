---
id: easybackgroundchecks-com
name: Easy Background Checks
domain: easybackgroundchecks.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: portal
opt_out_url: "https://suppression.peopleconnect.us/login"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, dob, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "EasyBackgroundChecks.com is a people-search/background-check site whose data and privacy infrastructure is run by Intelius / PeopleConnect -- confirmed via WebFetch on the live site's footer, which links its 'Do Not Sell Or Share My Personal Information' and 'Exercise My Data Privacy Rights' controls directly to intelius.com/privacy-policy/ and intelius.com/privacy-center/, not to a page on its own domain. Multiple 2026 third-party opt-out guides (Cloaked, PurePrivacy) independently describe the real removal mechanism as PeopleConnect's shared suppression portal at suppression.peopleconnect.us/login, requiring email, legal name, and date of birth, plus email confirmation -- I confirmed that URL is live (HTTP 200) via direct request. Intelius's own pages were Cloudflare/Turnstile bot-blocked on direct WebFetch attempts, so the field-level process is reconstructed from guides rather than a freshly rendered page -- CAPTCHA presence noted by guides at the account-creation step of the suppression portal, guided tier. This is the legacy CSV's flagged 'likely real people-search' domain -- confirmed genuine and priority: crucial. Overrides the CSV's opt_out_method: 'No' -- an opt-out does exist via the shared PeopleConnect suppression system, it's just not hosted on easybackgroundchecks.com itself."
---

1. Go to https://suppression.peopleconnect.us/login (PeopleConnect's shared suppression center, which also covers Intelius, Instant Checkmate, and other affiliated people-search sites including EasyBackgroundChecks.com).
2. Create an account or sign in, then search for your own listing using your legal name and location.
3. Select your matching record(s) and set them to "Suppressed."
4. Enter your email address and date of birth to verify the request, and solve any CAPTCHA presented.
5. Confirm the request via the verification link sent to your email.
6. Because this is a shared backend, suppressing your record here should also remove you from Intelius and other PeopleConnect-affiliated sites, including EasyBackgroundChecks.com. Re-check periodically since these sites re-ingest public records.
