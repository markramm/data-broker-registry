---
id: checkthem-com
name: CheckThem
domain: checkthem.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.checkthem.com/optout/"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, email, full_name]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Direct WebFetch of checkthem.com/optout/ returned empty content (likely JS-rendered), so the process below is reconstructed from multiple independent, mutually consistent 2026 opt-out-guide writeups (DeleteMe, PrivacyHawk, MyDataRemoval, RemoveMyPhone) that all describe the same flow: search by name+city/state on the optout page, select the matching listing, paste its URL plus an email into a form, solve a CAPTCHA, and click an emailed confirmation link, with removal completing within ~24 hours. CAPTCHA-gated -> guided tier. CheckThem is a people-search site returning background-check-style results (name, age, city/state, relatives), so people_search:true and priority:crucial. Not freshly confirmed against a rendered page -- last_verified left null."
---

1. Go to the [CheckThem opt-out page](https://www.checkthem.com/optout/).
2. Search for yourself using your first name, last name, and the city/state where you're listed, then click "Search Now."
3. Find the listing that matches you in the results and click "Choose."
4. Copy that listing's URL and enter it in the opt-out form along with your email address, then solve the CAPTCHA and click "Send Verification Email."
5. Open the confirmation email from CheckThem and click the verification link -- the removal isn't final until you confirm.
6. Your listing should be removed within about 24 hours. If you have multiple listings (different ages, cities, or name variants), repeat the process separately for each one.
7. If the form doesn't find your listing or you hit issues, you can email a removal request directly with your full name, age as listed, and most recent city/state on file.
