---
id: cuebiq-com
name: "Cuebiq Group, LLC"
domain: cuebiq.com
category: location_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://cuebiq.com/privacy-request/"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [email, other]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-11-05 by the daily maintainer from California's data broker registry (Cuebiq Group, LLC, listing legal@cuebiq.com and https://cuebiq.com/privacy-request/). Cuebiq sells device location data (footfall measurement, location-based audiences) keyed to mobile advertising IDs, so it is a location-data broker: people_search false, priority high. I fetched the privacy request page (HTTP 200) and rendered it in a headless browser without submitting anything. It is a Gravity Forms form with: a request-type radio (opt-out/do not sell or share, access, or delete), email (required), Type of ID (IDFA or GAID, required), the Mobile Advertising ID itself, and an authorized-agent yes/no with a file upload for the agent designation form. The page says Cuebiq must validate both the requester and their ownership of the MAID. Its only CAPTCHA is an invisible reCAPTCHA v3 badge (ginput_recaptchav3) with no visible challenge, so captcha is false. Tier is guided rather than assisted because the user has to find their device's advertising ID first, and on iOS the page itself says that takes a third-party app. The privacy policy (updated 10/22/26, fetched) names the same form as the opt-out path and gives privacy@cuebiq.com for questions and correction requests only, so opt_out_email is null. verification: email_confirm is inferred from the page saying the email is used to process the request; I didn't observe the confirmation step. The second form on the page (work email, title, company) is a sales-demo form, not part of the opt-out. last_verified null."
---

Cuebiq collects location data from phones and ties it to the phone's mobile advertising ID. That ID, not your name, is what you opt out.

1. Find your phone's advertising ID. On Android, go to Settings > Privacy > Ads (or Settings > Google > Ads); the ID is listed at the bottom. iPhones don't show the IDFA in Settings; Cuebiq suggests a third-party app from the App Store that can display it.
2. Go to https://cuebiq.com/privacy-request/.
3. Under "I wish to", choose "opt-out/do not sell or share my personal information". You can also choose access or delete.
4. Enter your email address, choose your ID type (IDFA for iPhone, GAID for Android), and paste your advertising ID.
5. Answer "No" to the authorized-agent question if you are submitting for yourself, then submit. Ignore the separate "Unlock Location Intelligence" sales form lower on the page.
6. Watch your inbox for any follow-up from Cuebiq asking you to confirm the request.
7. Repeat for each phone you use. If you reset your advertising ID later, the new ID won't be covered, so submit again. You can also turn off ad tracking on the device itself (Android: "Delete advertising ID"; iPhone: Settings > Privacy & Security > Tracking).
