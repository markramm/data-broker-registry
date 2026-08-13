---
id: infopay-com
name: "InfoPay"
domain: infopay.com
category: people_search
people_search: true
tier: auto
priority: crucial
method: email
opt_out_url: "https://www.infopay.com/privacy"
opt_out_email: "privacy@infopay.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "The legacy CSV's privacy_policy URL (infopay.com/privacy.php) 302-redirects to infopay.com/privacy, which was fetched. That page describes InfoPay as a payment-adjacent-sounding name but the homepage (WebFetch on infopay.com/) makes clear InfoPay is actually a public-records/people-search data aggregator: 'connects billions of records from thousands of sources, including vehicle, property, court, and business entity records' and lets users 'instantly search for people, property records, public records, vehicles and more,' plus skip-tracing resources -- so people_search is true and priority is crucial (personal-safety relevance of a people-search/skip-trace product), not standard as the payment-sounding name might suggest. No dedicated listing-removal/opt-out form was found (checked infopay.com/optout -> 404; homepage only links to /privacy). The privacy page states InfoPay does not sell/share personal info for cross-context behavioral advertising and honors Global Privacy Control signals, and provides privacy@infopay.com for privacy requests generally -- used here as the CCPA opt-out/deletion contact since no dedicated form exists. method:email with a plain email contact and no login/CAPTCHA -> tier auto. last_verified left null since the opt-out mechanism itself (whether this email actually results in people-search listing removal, vs. just ad-tracking opt-out) was not independently confirmed beyond the privacy page's general language."
---

1. Email privacy@infopay.com and state that you are exercising your CCPA right to opt out of the sale/sharing of your personal information, and request deletion of any record associating you with InfoPay's people-search, skip-tracing, property, or vehicle report products.
2. Include your full name and any email address(es), phone numbers, or past/current addresses InfoPay may have on file, so they can locate and remove your record(s).
3. If you know the specific report/profile URL that shows your information, include that link in your email to speed up removal.
4. InfoPay states it honors the Global Privacy Control (GPC) browser signal -- if your browser or an extension supports GPC, enabling it will stop InfoPay sharing your data with third parties for personalized ads going forward, though this does not by itself remove an existing people-search listing.
5. Keep a copy of your email; if you do not receive a response or confirmation within a reasonable time, follow up by replying to the same thread.
