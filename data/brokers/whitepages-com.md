---
id: whitepages-com
name: Whitepages
domain: whitepages.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.whitepages.com/suppression-requests"
opt_out_email: null
phone: "(800) 991-3077"
captcha: true
id_required: false
phone_required: true
charges_fee: false
required_fields: ["listing_url", "phone"]
readd_days: null
legal_basis: []
last_verified: null
source: "data-brokers-watch + tcp-verified"
notes: "Direct fetch of whitepages.com blocked for fetch tooling in this session (same bot-block as noted on the related 411.com entry, which is powered by the same Whitepages suppression flow). Assessed from third-party removal-guide consensus (Incogni, DeleteMe, Security.org, CyberInsider). The suppression-requests flow requires a live automated phone-verification call -- a robocall reads back a 4-digit code you re-enter on screen -- plus a CAPTCHA, so despite method:form this is phone_required and guided, not assisted."
---

1. Search whitepages.com for your own listing and copy its URL.
2. Go to whitepages.com/suppression-requests and paste in the listing URL.
3. Enter the phone number associated with the listing and complete the CAPTCHA.
4. Whitepages places an automated call to that phone number that reads back a 4-digit verification code.
5. Enter the code on the suppression-request page when prompted to confirm you control that number.
6. Submit the request; allow several days for the listing to be suppressed, and repeat for any other listings under different addresses.
