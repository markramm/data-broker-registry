---
id: reversephonelookup-com
name: "Reverse Phone Lookup"
domain: reversephonelookup.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.reversephonelookup.com/remove.php"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, phone, email]
readd_days: null
legal_basis: []
last_verified: null
source: data-brokers-watch
notes: "WebFetch of reversephonelookup.com was blocked (host unreachable via WebFetch). Third-party guides confirm remove.php is a working search-and-select removal form (search by name/phone, select record, submit, confirm by email), but note the site is powered by Intelius/PeopleConnect, so a listing may reappear unless you also complete the Intelius suppression process. Assumed CAPTCHA present given PeopleConnect-network norms; not freshly confirmed, so last_verified is null."
---

1. Go to `https://www.reversephonelookup.com/remove.php`.
2. Search for your listing by phone number or name.
3. Select your record from the results and follow the on-screen prompts to submit a removal request (this typically includes a CAPTCHA and your email address).
4. Check your email for a confirmation message and click the verification link.
5. Because this site is powered by Intelius/PeopleConnect, also complete the opt-out at `https://www.intelius.com/optout` for your name/state -- removing only the local listing here does not guarantee removal from the underlying network (TruthFinder, Instant Checkmate, etc.), and data can resurface within 48-72 hours if the upstream record isn't also suppressed.
