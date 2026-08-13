---
id: reunion-com
name: "Reunion.com (MyLife)"
domain: reunion.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.mylife.com/ccpa/personal-information-removal-request"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, listing_url]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "reunion.com (a former classmate/reunion-finder brand, matching the domain-name hint) 301-redirects to mylife.com -- Reunion.com has been absorbed into MyLife, a well-known people-search/reputation-profile broker. Direct fetch of mylife.com/ccpa/personal-information-removal-request returned HTTP 403 with a Cloudflare 'Attention Required' interstitial (bot-blocked), consistent with MyLife's known aggressive bot protection. URL and general process (find your profile, request removal via CCPA form) reconstructed from the redirect target and MyLife's documented removal flow in third-party opt-out guides; not independently confirmed by rendering the page. CAPTCHA assumed true given the Cloudflare gate. Crucial priority: MyLife is a well-documented people-search/reputation-profile broker with real personal-safety stakes (name, age, address, relatives, background-check teasers)."
---

1. Note that reunion.com now redirects to mylife.com -- Reunion.com's former classmate/reunion-finder profiles are served by MyLife, and removal happens on MyLife, not on a separate reunion.com site.
2. Search your name on mylife.com and open the profile page that matches you; copy its exact URL.
3. Go to the [MyLife CCPA personal information removal request page](https://www.mylife.com/ccpa/personal-information-removal-request).
4. Paste in your profile URL and provide your full name as it appears on the profile.
5. Complete the CAPTCHA/bot-verification challenge (MyLife's site is behind Cloudflare bot protection and may require solving a challenge before the form loads).
6. Submit the removal request and watch for a confirmation email; click any confirmation link it contains.
7. Repeat for any additional distinct profiles that match you, and re-check periodically since MyLife profiles can reappear after new data pulls.
