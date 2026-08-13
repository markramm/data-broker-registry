---
id: peopleconnect-us
name: Peopleconnect
domain: peopleconnect.us
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://suppression.peopleconnect.us/"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, dob]
readd_days: null
legal_basis: []
last_verified: "2026-08-13"
source: "data-brokers-watch + tcp-verified + chrome-verified"
notes: "MIGRATED research_note: central suppression portal (Intelius/TruthFinder/Instant Checkmate/US Search); no third-party opt-outs. Confirmed via WebSearch (direct fetch returned only a bare page title, no CAPTCHA blocked it, just thin content): this is PeopleConnect's centralized 'Suppression Center' -- one request here suppresses records across the whole PeopleConnect family (Intelius, TruthFinder, Instant Checkmate, US Search, PeopleLookup, PeopleSmart all route here). Flow is email verify -> DOB -> name/aliases -> select matching record(s) -> mark 'Suppressed'. No CAPTCHA or ID upload found in current guides, so kept at assisted rather than guided; re-verify on next pass since PeopleConnect has added CAPTCHA steps in the past. Chrome-driven check (2026-08-13): CONFIRMED. Page loads at this exact URL, Step 1 is 'Enter your email address' with a Terms/Privacy checkbox, no CAPTCHA visible at this step. The page's own on-screen copy explicitly states: 'Our Suppression Tool provides a free way to manage the display of your Background Report when searched by name on all people search sites in the PeopleConnect family including TruthFinder.com, InstantCheckmate.com, Intelius.com and USSearch.com.' Also independently confirmed intelius-com's documented opt_out_url (intelius.com/opt-out) redirects directly to this exact page -- see intelius-com.md."
---

1. Go to suppression.peopleconnect.us and enter an email address you can access, then agree to the terms and continue.
2. Check your inbox for a verification email from PeopleConnect and click "Verify Email."
3. Enter your date of birth when prompted -- this is used to match your identity to records and cannot be edited later.
4. Enter your legal name and any alternate names (maiden name, nickname, former married name) to widen the match.
5. Review the records the portal surfaces and select the one(s) that are actually you.
6. In the "Desired Behavior" dropdown choose "Suppressed" and save. This single request suppresses your data across the whole PeopleConnect network (Intelius, TruthFinder, Instant Checkmate, US Search, PeopleLookup, PeopleSmart), so you should not need to repeat it separately on those sites.
