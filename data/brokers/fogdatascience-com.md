---
id: fogdatascience-com
name: "Fog Data Science LLC"
domain: fogdatascience.com
category: location_data_broker
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://www.fogdatascience.com/opt-out"
opt_out_email: "privacy@fogdatascience.com"
phone: "+1 (888) 834-3202"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [other]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-10-31 by the daily maintainer from California's data broker registry (Fog Data Science LLC; rights URL https://www.fogdatascience.com/opt-out). Fog sells commercially available device location data; its 'Your Privacy Choices' page (curl and WebFetch, HTTP 200; rendered in headless Chromium) says its Data Services are 'organized by Mobile Advertising ID (MAID), not by consumer name, home address', and that names, addresses, phone numbers or dates of birth will not let it find a MAID-indexed record. The page has two Squarespace forms: 'Opt-Out My Device', whose only field is the device identifier, and a 'California Privacy Request' form requiring first and last name, email, a California-residency yes/no, a message, the MAID and the right requested (know / access / delete / opt-out / limit). Both forms load reCAPTCHA Enterprise in invisible mode (size=invisible), so captcha: false; a challenge could still appear on submit, which was not tested. The page says the MAID is used to 'prevent associated data from being included in applicable future data updates' and does not say data already held is deleted, so the steps add the delete request. Contacts on the page: privacy@fogdatascience.com and +1 (888) 834-3202. It also points California residents to the CPPA's DROP platform. Priority high: precise location data tied to a device. Nothing was submitted; last_verified null."
---

1. Find your phone's mobile advertising ID (MAID). On Android it is under Settings > Google > Ads; iPhone settings don't display it, so use the "suggested links" on Fog's form for how to find it. Fog's records are indexed only by this ID, so your name or address won't find them.
2. Go to https://www.fogdatascience.com/opt-out and open "Opt-Out My Device".
3. Paste your advertising ID into the Identifier field and submit. Repeat for each phone or tablet you use.
4. To also have data already held deleted, California residents can use "Submit a California Privacy Request" on the same page: enter your name, email, confirm residency, paste the advertising ID, choose "Right to Delete" (and "Right to Opt-out"), and add a short message.
5. If the forms don't work, email privacy@fogdatascience.com or call +1 (888) 834-3202 with your advertising ID and the request.
