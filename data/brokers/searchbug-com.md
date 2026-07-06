---
id: searchbug-com
name: "Search Bug"
domain: searchbug.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.searchbug.com/contact-us.aspx"
opt_out_email: null
phone: null
captcha: false
id_required: true
phone_required: false
charges_fee: false
required_fields: [full_name, email, phone, address, gov_id]
readd_days: null
legal_basis: [ccpa]
last_verified: 2026-07-03
source: "data-brokers-watch + tcp-verified"
notes: "MIGRATED research_note: own CCPA/Do-Not-Sell form, fetched 200. Re-fetched 2026-07-03: the actual request flow lives at /contact-us.aspx (the ccpa.aspx URL redirects/points here), which requires selecting 'CCPA Request' or 'Opt-Out Request', entering name/email/phone/address matching official ID, and uploading a photo of a driver's license or government ID. Updated opt_out_url to the working contact-form path, set id_required true (photo ID upload demanded), and flagged this as guided given the ID-upload requirement despite there being no CAPTCHA. Domestic-violence/stalking-victim and law-enforcement requesters have an alternate documentation path (court order instead of ID)."
---

1. Go to `https://www.searchbug.com/contact-us.aspx`.
2. Under reason for contact, select "CCPA Request" if you're a California resident, or "Opt-Out Request" otherwise.
3. For the subject line, enter "Do Not Sell" (or, if you're a protected individual such as a domestic violence/stalking victim, law enforcement officer, judge, or public figure, select the matching category instead).
4. Fill in your name, email, and phone number, and enter an address that matches your official ID/legal documents.
5. Upload a photo of your driver's license or other government-issued ID (protected-category requesters should upload a court order or equivalent documentation instead of an ID).
6. Submit the form. Searchbug states CCPA requests may take up to 45 days to process; for bulk or opt-out-service-provider requests, contact support@searchbug.zohodesk.com instead.
