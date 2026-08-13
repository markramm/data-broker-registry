---
id: backgroundcheck-run
name: "BackgroundCheck.run"
domain: backgroundcheck.run
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "<verify: exact opt-out/control-profile form URL on backgroundcheck.run>"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Multiple independent 2026 opt-out-guide writeups (DeleteMe, Optery, Incogni, PurePrivacy) consistently describe backgroundcheck.run as a live people-search site publishing aliases, DOB/age, address history, phone numbers, email addresses, marriage/divorce records, family relations, and property records on named individuals -- squarely a people-search broker with real stalking/doxxing risk, hence crucial priority. Process described consistently: search by name+location, open your profile, click 'Control this profile' / a similar claim link, fill a form with the profile URL + full name + email, solve a CAPTCHA, submit, then confirm via an emailed link; removal reportedly completes in 24-48 hours. Direct WebFetch/curl to backgroundcheck.run itself did not succeed in this environment (DNS/connection issues), so I did not render the live page myself -- this entry is built entirely from secondhand guide consensus, not a direct fetch, which is why opt_out_url is left as a placeholder and last_verified is null despite the consistent secondary sourcing. Domain registrant is privacy-shielded (Domains By Proxy) per WHOIS lookups referenced in search results, consistent with many people-search operators."
---

1. Go to backgroundcheck.run and search for your own listing using your first name, last name, and city/state.
2. Open the profile that matches you and copy its exact profile URL.
3. Look for a "Control this profile" (or similarly worded) link/button on that profile and click it to start the opt-out process.
4. Paste in your profile URL, enter your full name and an email address, and solve the CAPTCHA.
5. Submit the opt-out request, then check your email for a confirmation link and click it to finalize -- the removal reportedly does not take effect until confirmed.
6. Repeat for any other profiles that match you (aliases, past addresses, or family-linked entries can create duplicate listings), and re-check every few months since people-search sites re-scrape public records and can re-list you.
