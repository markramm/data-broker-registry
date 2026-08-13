---
id: classmates-com
name: Classmates.com
domain: classmates.com
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://www.classmates.com/privacy"
opt_out_email: "privacy@classmates.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Classmates.com is a PeopleConnect Inc brand (same family as Intelius/USSearch/TruthFinder in this repo -- see peopleconnect-us.md and ussearch-com.md) that hosts profiles, yearbook photos, and alumni/reunion data on named individuals -- a genuine people-search broker with real personal-safety stakes (digitized yearbook photos in particular are hard to fully suppress). WebFetch on classmates.com and peopleconnect.us/privacy both failed (403 / 404) in this session; routing reconstructed from consistent third-party 2025 opt-out guides (Optery, PrivacyOn, BlueOceanGlobalTech) describing two parallel paths: (1) sign in, scroll to footer, click 'Do Not Sell My Personal Information', which opens a CCPA opt-out form; (2) email privacy@classmates.com directly requesting removal, citing CCPA if in California. Unlike ussearch.com and peopleconnect.us in this repo, Classmates does NOT appear to route through the central suppression.peopleconnect.us portal in these guides -- it has its own site-specific opt-out -- so it is authored as a distinct entry per the task instructions rather than merged into peopleconnect-us.md. No CAPTCHA or ID requirement reported by any guide, so kept at assisted; guides note yearbook-photo removal specifically may require a separate, more specific request beyond the standard opt-out. Not freshly confirmed against a rendered page; last_verified left null."
---

1. Go to https://www.classmates.com/ and sign in to your account (create a free account with your email if you don't already have one, since the site associates profile data with logged-in sessions).
2. Scroll to the bottom of any page and click "Do Not Sell My Personal Information" in the footer.
3. On the privacy page, find section 3 ("Updating or Removing Your Information") and click the "click here" link to start the removal request.
4. Alternatively, skip the web form and email privacy@classmates.com directly asking that your personal information be removed; mention the CCPA (or your state's privacy law) if you don't get a response within 7-10 business days.
5. If you have a paid Classmates+ subscription, go to My Classmates > Account > Account & Billing and turn off automatic renewal before requesting deletion, so you aren't charged again while the request processes.
6. Note that digitized yearbook photos may remain visible in the site's yearbook-browsing section even after your profile is removed, since Classmates treats them as historical scans rather than personal profile data -- if a yearbook photo of you needs to come down, say so explicitly in your removal email.
7. Because Classmates is part of the PeopleConnect family, also check Intelius, TruthFinder, Instant Checkmate, and US Search for the same listing -- see this repo's peopleconnect-us.md for the shared suppression portal covering those other brands.
