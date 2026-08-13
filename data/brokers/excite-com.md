---
id: excite-com
name: Excite
domain: excite.com
category: search_engine
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://www.excite.com/privacy"
opt_out_email: "privacy@ask.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: []
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "The legacy CSV's privacy_policy URL (eula.mindspark.com/excite/privacypolicy) no longer resolves (DNS failure). WebFetch on the live excite.com/privacy page shows Excite is now operated by Ask Media Group LLC, not Mindspark, and the policy is a shared interest-based-advertising opt-out: an on-page 'Opt Out' toggle button tied to a per-browser cookie ID, plus a contact email of privacy@ask.com and a note that one ad partner (LiveRamp) requires its own separate opt-out at optout.liveramp.com. Because the primary mechanism is a no-login, no-CAPTCHA browser toggle (not a data-deletion form per se), classified assisted rather than guided; still a search-portal/adtech opt-out rather than a people-search removal, so priority standard. Not independently re-verified with a live render beyond the single WebFetch pass; last_verified left null."
---

1. Go to https://www.excite.com/privacy in the same browser you normally use to visit Excite (the opt-out is tied to your browser's cookie, so it only affects that browser/device).
2. Find the interest-based-advertising section and click the "Opt Out" toggle/button described there to stop Excite's advertising partners from using your browsing data for personalized ads.
3. If you use multiple browsers or devices, repeat the toggle opt-out on each one separately.
4. For a broader privacy request (data access or deletion, not just ad-targeting), email privacy@ask.com directly and describe what you're requesting.
5. Note that one of Excite's ad-data partners, LiveRamp, maintains its own separate opt-out; visit https://optout.liveramp.com/opt_out if you want to also stop LiveRamp's use of your data.
