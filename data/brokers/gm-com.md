---
id: gm-com
name: General Motors
domain: gm.com
category: connected_vehicle_data
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.gm.com/consumer-privacy"
opt_out_email: null
phone: "1-866-697-7482"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [full_name, email, address, phone]
readd_days: null
legal_basis: [ccpa, cpra, vcdpa, cdpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Registered California data broker (CA registry row: General Motors LLC, gm.com, privacy@gm.com, rights URL https://www.gm.com/consumer-privacy). GM collects driving-behavior, geolocation and vehicle data from connected cars (OnStar, the brand mobile apps), so the stakes for drivers are real. On 2026-11-07, fetched https://www.gm.com/privacy-statement with curl (HTTP 200). Its 'Your privacy rights' section says requests go through the U.S. Consumer Privacy Request Form or the phone line 1-866-MYPRIVACY (1-866-697-7482), and that GM does not accept privacy requests by email. Rights listed: access/portable copy, correct, delete, and, depending on state, opt out of targeted advertising ('Do Not Share'), opt out of sale, and a list of third parties. The statement also says GM honors Global Privacy Control, that marketing preferences are at gmcontactpreferences.com, and that you can unenroll from OnStar on 1-888-466-7827 or with the blue button. https://consumerprivacy.gm.com redirects to https://www.gm.com/consumer-privacy. That page loaded by curl but is only a shell that embeds the form from https://privacy.gm.com (an Angular app). privacy.gm.com returned 403 to a headless browser, so the rendered form was never seen. The form's JavaScript bundle (fetched by curl) shows fields for name, address, phone, email, optional date of birth, OnStar account number, GM Rewards number and VIN. It marks first name, last name, email, address and phone as required, and adds a step where a 6-digit verification code is sent to your email (or phone). No CAPTCHA code was found in the bundle, but because the rendered form wasn't observed, tier is guided out of caution. Nothing was submitted; last_verified left null."
---

1. Go to GM's U.S. Consumer Privacy Request Form at https://www.gm.com/consumer-privacy (or call 1-866-697-7482). GM does not take privacy requests by email.
2. Choose the requests you want: delete my personal information, opt out of selling, and opt out of sharing for targeted advertising ("Do Not Share").
3. Enter your name, address, phone number and email. Optionally add your VIN, OnStar account number or GM Rewards number; these help GM find the vehicle data it holds about you.
4. Request the verification code, then enter the 6-digit code GM sends to your email (or phone) to confirm the request.
5. Answer any follow-up identity check. GM says it can take up to 45 days to respond.
6. Optional: to stop new data being collected from a connected vehicle, unenroll from OnStar on 1-888-466-7827 (or with the blue OnStar button), and check the privacy settings in the car's infotainment system. Turning on Global Privacy Control in your browser opts you out of sale on GM's websites.
