---
id: viantinc-com
name: "Viant Technology"
domain: viantinc.com
category: adtech
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://privacyportal.onetrust.com/webform/18c06089-a9ec-473c-a6d8-23d20fea46af/43201dea-88d7-44cd-9142-e5b4f485e428"
opt_out_email: "privacy@viantinc.com"
phone: "1-888-655-1873"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: ["full_name", "email"]
readd_days: null
legal_basis: ["ccpa", "cpra"]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on viantinc.com's privacy policy identified a standard OneTrust consumer-rights-request webform (access/deletion/opt-out) and a separate cookie/device-level opt-out at my.ipredictive.com (Adelphic, Viant's ad platform). Viant is a programmatic advertising / identity-graph company (adtech), not a people-search site. OneTrust webforms are typically simple and not CAPTCHA-gated, so assisted tier; downgraded from crucial to high since this is ad-targeting data rather than a public-facing people-search profile. The OneTrust webform link was confirmed reachable via direct HTTP check (200) in this session; page contents themselves were not rendered by this agent, so last_verified left null."
---

1. Go to Viant's [Consumer Rights Request Portal](https://privacyportal.onetrust.com/webform/18c06089-a9ec-473c-a6d8-23d20fea46af/43201dea-88d7-44cd-9142-e5b4f485e428) and submit an opt-out or deletion request with your name and email address.
2. If you want to stop cookie-based ad targeting specifically, also visit the [Viant/Adelphic cookie opt-out](https://my.ipredictive.com/optout/mobile-web?deviceId=MobileWeb) from each browser and device you use (this opt-out is not account-wide).
3. Alternatively, email privacy@viantinc.com or call 1-888-655-1873 with your request.
4. If your browser sends a Global Privacy Control (GPC) signal, Viant states it will honor that as an opt-out automatically -- no form needed in that case.
