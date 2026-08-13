---
id: sync-me
name: Sync.ME
domain: sync.me
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://sync.me/do-not-sell/"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, phone]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch confirmed Sync.ME is a caller-ID and reverse-phone-lookup app/service: it provides real-time Caller ID, lets users 'find out who owns a phone number,' blocks spam calls, and syncs contacts with social profiles -- i.e. it builds and serves a people-search-style database keyed on phone numbers, so people_search is true and priority is crucial despite the opt-out mechanism itself being simple. Its footer links a dedicated 'Do Not Sell My Info' page at https://sync.me/do-not-sell/, confirmed via a second WebFetch to be a plain web form (no CAPTCHA, no ID requirement) requiring name, email, and phone number (with country-code selector); the form notes the request is submitted partly under New Jersey's Daniel's Law, which protects contact info of judicial/law-enforcement personnel specifically but the general form appears usable by any requester. Because it's a simple form with no CAPTCHA/ID gate, tier is assisted rather than guided. Separate privacy policy, unsubscribe, and cookies-policy pages also exist at sync.me/privacy/, sync.me/unsubscribe/, and sync.me/cookies-policy/. last_verified left null since pages were summarized via fetch tool rather than independently re-rendered."
---

1. Go to Sync.ME's opt-out form at https://sync.me/do-not-sell/.
2. Enter your full name, email address, and phone number (select the correct country code).
3. Submit the form to request that Sync.ME not sell or share your personal information, and to remove your number/caller-ID entry from its database.
4. If you have multiple phone numbers associated with you, submit a separate request for each number.
5. For general account or listing removal beyond the do-not-sell request, also check https://sync.me/privacy/ and https://sync.me/unsubscribe/ for additional controls.
