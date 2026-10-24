---
id: assurance-com
name: "Assurance IQ"
domain: assurance.com
category: marketing_data_broker
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "https://www.prudential.com/links/privacy-center/data-requests.html"
opt_out_email: "Global.Privacy@prudential.com"
phone: "1-844-778-3727"
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, phone, dob, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Assurance IQ (a Prudential-owned insurance-lead marketing company) publishes a CCPA disclosure at assurance.com/ccpa-disclosure describing sale of personal information and a dedicated opt-out page at assurance.com/ccpa-opt-out (Data Request Form) plus a phone alternative at 1-844-311-6099, per its own disclosure page and corroborated by Privacy Rights Clearinghouse. Note: direct WebFetch to both assurance.com/ccpa-disclosure and assurance.com/ccpa-opt-out failed with 'certificate has expired' -- independently confirmed via curl -sv that assurance.com's TLS certificate is genuinely expired as of this research date, not a fetch-tool artifact. Could not verify exact form fields/CAPTCHA on the live page as a result; required_fields inferred conservatively from generic CCPA data-request-form norms. The CCPA disclosure notes exemptions for GLBA/HIPAA-covered financial/health data (Assurance sells life/health insurance leads), so some requests may be declined in part. last_verified left null; flagging the expired certificate as a real, currently observable problem with the broker's own site. Update 2026-10-24 (daily maintainer, page-monitor #121): https://assurance.com/ccpa-opt-out and /ccpa-disclosure now both return HTTP 404 (curl, with and without www). The assurance.com homepage loads (HTTP 200), and its footer's only privacy link, 'Privacy center', goes to Prudential's privacy center (https://www.prudential.com/links/privacy-center). Prudential owns Assurance IQ. That center's 'Request data' page (https://www.prudential.com/links/privacy-center/data-requests.html) links a OneTrust 'Data Request Form' and gives 1-844-PRU-DSAR (1-844-778-3727) and Global.Privacy@prudential.com for requests the form doesn't cover. Loaded in a headless browser, the form requires country of residence, self or on-behalf-of, first and last name, email (twice), year of birth, ZIP code, phone number and a truthfulness certification, and shows a visible reCAPTCHA checkbox, so captcha is true and the tier is guided. The request types weren't visible until a country is chosen, and the FAQ says to use 'Other Request Type' for anything not listed, so whether 'opt out of sale/sharing' is its own option is unconfirmed. The old Assurance phone line (1-844-311-6099) was not re-checked and was replaced with the Prudential DSAR line the page gives. Nothing was submitted; last_verified stays null."
---

1. Go to Prudential's privacy request page at https://www.prudential.com/links/privacy-center/data-requests.html (Assurance's own site links its privacy questions to Prudential's privacy center; the old assurance.com opt-out page is gone).
2. Click "Submit a request" to open the Data Request Form.
3. Choose your country of residence and "Self", then enter your first and last name, email (twice), year of birth, ZIP code and phone number.
4. Choose the request you want: deletion, or opt-out of sale/sharing if it's offered. If it isn't, pick "Other Request Type" and write that you want Assurance IQ to stop selling or sharing your personal information under the CCPA.
5. Tick the certification, solve the CAPTCHA and submit.
6. Alternatively, call 1-844-PRU-DSAR (1-844-778-3727) or email Global.Privacy@prudential.com, and name Assurance IQ in your request.
7. Some information tied to insurance you actually bought (covered by GLBA or HIPAA) may be exempt from the opt-out.
