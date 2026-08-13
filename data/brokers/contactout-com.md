---
id: contactout-com
name: ContactOut
domain: contactout.com
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://www.contactout.com/optout"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch/WebSearch confirmed ContactOut indexes and resells personal email addresses and phone numbers scraped from websites and social media (LinkedIn etc.) for sales/recruiting use -- a genuine people-search/contact-data reseller, so people_search true and priority crucial (personal contact info including phone numbers). Their dedicated opt-out page at contactout.com/optout is a two-step process: submit identifying info, then click an emailed verification link, after which they commit to deleting the profile within 24 hours. No CAPTCHA or ID upload was observed in the page description, so classified assisted rather than guided. Note ContactOut states removed profiles can reappear if the source page still exists, so periodic re-checking is warranted."
---

1. Go to https://www.contactout.com/optout.
2. Enter your full name and the email address you want removed (or that is associated with your listing).
3. Click "Send verification link" and check your inbox for ContactOut's confirmation email.
4. Click the link in that email to confirm the opt-out request.
5. ContactOut states it will delete the matching profile within 24 hours of verification.
6. Because ContactOut re-scrapes public sources, re-check periodically -- if your information is still publicly available elsewhere (e.g., a public LinkedIn profile), it may be re-indexed and require opting out again.
