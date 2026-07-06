---
id: peoplelookup-com
name: "People Lookup (Data Source Intelius)"
domain: peoplelookup.com
category: people_search
people_search: true
tier: assisted
priority: crucial
method: portal
opt_out_url: "https://suppression.peopleconnect.us/"
opt_out_email: null
phone: "866-974-6185"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, dob]
readd_days: null
legal_basis: []
last_verified: null
source: data-brokers-watch
notes: "WebFetch of the migrated privacy-policy URL 302-redirected to ussearch.com/?feeder=peoplelookup, confirming peoplelookup.com is now folded into the PeopleConnect family (Intelius/US Search) and no longer runs its own opt-out flow. Corrected opt_out_url to the same PeopleConnect Suppression Center used by peoplesmart.com and peopleconnect.us -- one suppression request there covers this listing too. Corrected method from form to portal. last_verified left null (not freshly re-fetched after the redirect)."
---

1. Note that peoplelookup.com no longer runs its own removal process -- it now redirects to USSearch, part of the PeopleConnect network.
2. Go to suppression.peopleconnect.us and enter an email address you can access, then continue.
3. Verify your email via the link PeopleConnect sends you.
4. Enter your date of birth, then your legal name and any alternate names.
5. Select the matching record(s) from the results shown.
6. Set "Desired Behavior" to "Suppressed" and save -- this covers PeopleLookup along with the rest of the PeopleConnect-owned sites (Intelius, US Search, TruthFinder, Instant Checkmate, PeopleSmart).
