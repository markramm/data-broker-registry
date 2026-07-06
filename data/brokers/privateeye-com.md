---
id: privateeye-com
name: privateeye.com
domain: privateeye.com
category: data_brokers
people_search: false
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.privateeye.com/removal"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, address, dob]
readd_days: null
legal_basis: []
last_verified: null
source: data-brokers-watch
notes: "WebFetch on the old query-string help URL returned empty content; the working removal path per multiple third-party opt-out guides is privateeye.com/removal, a separate two-step form (initial name+email, then an emailed link -- expires in 24h -- to a second form asking DOB/address, gated by CAPTCHA). Updated opt_out_url to the real removal path since the legacy Help-page anchor is stale/unreliable. Not freshly fetched successfully, so last_verified left null; people-search site, so priority is crucial regardless of category field inherited from migration."
---

1. Go to `https://www.privateeye.com/removal` and enter your first name, last name, and email address, then submit.
2. Check your inbox (and spam folder) for an email from PrivateEye with an opt-out link. Click it within 24 hours -- the link expires after that and you'll need to resubmit step 1.
3. On the linked removal form, fill in your date of birth, street address, city, and state to match your listing.
4. Complete the CAPTCHA challenge and click "Opt Out."
5. Removal typically completes within about 3 days. If you have lived in multiple states or used different name variants, repeat this process for each separate listing/profile.
