---
id: clearview-ai
name: "Clearview AI"
domain: clearview.ai
category: facial_recognition
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.clearview.ai/privacy-and-requests"
opt_out_email: "privacy-requests@clearview.ai"
phone: "1-866-637-0257"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [email, other]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-10-24 by the daily maintainer from California's data broker registry (Clearview AI, Inc.; registry rights URL https://www.clearview.ai/privacy-and-requests, email privacy-requests@clearview.ai). Clearview runs a facial-recognition search engine built from publicly posted photos and sells it to investigators and law enforcement. Because the public can't search it, people_search is false, but a face search that returns a person's photos and the pages they appear on carries real personal-safety stakes, so the priority is high. https://www.clearview.ai/privacy-and-requests, loaded in a headless browser (HTTP 200), lists per-state request links (California: Access, Delete, Do Not Sell/Share, Correct, Limit Use of Sensitive Info), all of which open the same OneTrust webform for California. Separate forms exist for Colorado, Connecticut, Delaware, Iowa and other states, plus an Illinois opt-out from search results. The California form, also loaded headless, asks whether you're a California resident, which right you're exercising, an email address, and requires an uploaded photo of your face (a redacted ID only for access requests); it shows a visible reCAPTCHA checkbox and gives 1 (866) 637-0257 as a phone alternative. The form says the photo is deleted after processing, except that for opt-out/deletion requests Clearview keeps an encrypted copy of the image, unlinked from other identifying information, to stop the face being collected again. A face photo upload and a CAPTCHA mean guided tier; 'other' in required_fields is the face photo. Nothing was submitted; last_verified is null."
---

1. Go to https://www.clearview.ai/privacy-and-requests and, under your state, click the request you want. For California, "Do Not Sell/Share" and "Delete" both open the same request form; other states have their own links.
2. Confirm that you're a resident of that state and pick the right you want to exercise: "Delete My Information" and "Do Not Sell/Share My Information". Submit a separate request for each one.
3. Enter an email address where Clearview can confirm your request.
4. Upload a clear photo of your face. Clearview can only find you by image, not by name or email. Only access requests need a redacted ID instead.
5. Tick the acknowledgment, solve the CAPTCHA and submit.
6. Watch for an email asking you to validate the request, and confirm it.
7. Alternatively, California residents can call 1 (866) 637-0257, and anyone can email privacy-requests@clearview.ai. Clearview says it keeps an encrypted copy of your photo after an opt-out or deletion, used only to stop your face being collected again.
