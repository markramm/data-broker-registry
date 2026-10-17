---
id: uplead-com
name: UpLead
domain: uplead.com
category: b2b_contact_data
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "https://www.uplead.com/opt-out/"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa, vcdpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on uplead.com and uplead.com/opt-out/ succeeded directly. UpLead is a B2B contact-data / sales-intelligence platform ('Real-time verified B2B emails, mobile numbers and intent data', '200M+ leads') -- a business-contact broker, not a people-search site (people_search:false, priority:standard per the B2B-only guidance). The opt-out page is a web form (not email) requiring a contact email, the email address the request concerns, a jurisdiction dropdown (CCPA, VCDPA, OCPA, TDPSA, GDPR, Other), a request-type dropdown ('Request my Information' / 'Delete my Information'), an optional phone number for SMS validation, and checkboxes agreeing to the Privacy Policy/Terms. No CAPTCHA was mentioned in the fetched content. Classified tier:assisted (plain form, no CAPTCHA/ID) rather than guided. legal_basis includes ccpa, vcdpa, and gdpr since the form's own jurisdiction dropdown names those alongside others (OCPA/TDPSA aren't in this schema's enum so were omitted). last_verified left null since this was a single WebFetch pass, not a rendered confirmation of live form submission. 2026-10-16 maintainer run (Fixes #46): re-fetched https://www.uplead.com/opt-out/ (HTTP 200). The opt-out form (id dataremoval) now has a visible reCAPTCHA v2 checkbox (elementor-g-recaptcha, data-type=v2_checkbox, data-size=normal), so captcha: true and tier assisted -> guided. The form also marks Full Name as required (along with contact email, jurisdiction and request type), so full_name was added to required_fields. The jurisdiction options now read CCPA, VDPA, OCPA, TDPSA, GDPR, Other. Nothing was submitted; last_verified stays null."
---

1. Go to https://www.uplead.com/opt-out/.
2. Enter your full name and a contact email address.
3. Enter the email address that UpLead's data concerns (this may be the same address).
4. From the "Data Privacy Jurisdiction" dropdown, select the law that applies to you (e.g. CCPA).
5. From the "Request Type" dropdown, select "Delete my Information" to request removal rather than just a data-access report.
6. Optionally provide a phone number if you want SMS confirmation, and check the boxes agreeing to UpLead's Privacy Policy and Terms.
7. Tick the reCAPTCHA checkbox, submit the form and watch for a confirmation email.
