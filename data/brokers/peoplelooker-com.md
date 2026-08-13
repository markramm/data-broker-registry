---
id: peoplelooker-com
name: People Looker
domain: peoplelooker.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.peoplelooker.com/svc/optout/search/optouts"
opt_out_email: null
phone: "1-800-592-7153"
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "PeopleLooker is a background-check / people-search site (part of the same broader background-check-site family as PeopleSmart/BeenVerified, though the fetched privacy policy did not itself state a shared parent, so kept as a distinct entry rather than merged). WebFetch on peoplelooker.com/privacy-policy confirmed a dedicated opt-out URL at /svc/optout/search/optouts, a customer-service phone line, and an opt-out email address (rendered as a masked '[email protected]' placeholder by the fetch tool, so opt_out_email is left null rather than guessed). The policy states CCPA requests can go through the online form, email, phone, or postal mail, and requires name/email/age/address for formal requests. No CAPTCHA was explicitly documented in the fetched policy text, but this class of site (name+state search -> select listing -> email verify) consistently uses CAPTCHA per industry-standard removal-guide patterns for comparable sites in this repo (BeenVerified, PeopleSmart) -- captcha:true and tier:guided reflect that inference rather than direct confirmation; flag for re-verification. last_verified left null (not independently rendered)."
---

1. Go to https://www.peoplelooker.com/svc/optout/search/optouts and search for your name and state to locate your listing.
2. Select the record that matches you from the search results.
3. Enter a valid email address and complete the CAPTCHA if prompted, then submit the opt-out request.
4. Check your email for a confirmation/verification message from PeopleLooker and click the link to finalize the opt-out.
5. If the online form doesn't work or you prefer not to use it, email your removal request directly, or call 1-800-592-7153 during business hours and ask for your listing to be removed under the CCPA.
6. Repeat for any additional listings that match your name, since separate profiles are not automatically linked.
