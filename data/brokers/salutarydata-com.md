---
id: salutarydata-com
name: "Salutary Data, LLC"
domain: salutarydata.com
category: b2b_contact_data
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://salutarydata.com/privacy-opt-out-and-disclosure-form/"
opt_out_email: null
phone: "617-917-4084"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, other]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "Salutary Data LLC describes itself as 'Highly Curated U.S. Business Contact & Company Data Intelligence' -- a B2B contact-data broker selling sourced/cleansed business-professional contact records via data feeds and API. curl fetch of salutarydata.com/privacy-opt-out-and-disclosure-form/ (HTTP 200, bypassing an earlier WebFetch 403 bot-block) confirmed a dedicated 'California Consumer Notice of Right to Opt-out of Sale/Sharing of Personal Information' form requiring name, work email address, current employer name, and employer address -- explicitly no SSN/DOB/residential address, consistent with a B2B-only contact database. States it will cease sale/sharing within 15 business days of request. required_fields uses 'other' for employer name/address since that field isn't in the schema enum. No CAPTCHA or ID upload required per the fetched page text. tier assisted (self-service form, no CAPTCHA/ID). priority standard (B2B-only). last_verified left null since the form was fetched via curl workaround, not a normal browser render, and submission itself wasn't tested."
---

1. Go to the Salutary Data opt-out and disclosure form at https://salutarydata.com/privacy-opt-out-and-disclosure-form/.
2. Provide your name, work email address, current employer name, and employer address -- Salutary Data uses these specifically because its database covers business professionals, not residential/personal data (it states it does not hold SSNs, dates of birth, or home addresses).
3. Submit the form to exercise your California right to opt out of the sale/sharing of your personal information.
4. Salutary Data states it will search its systems using the information you provided and exclude your data from future sale/sharing with third parties within 15 business days of receiving your request.
5. If you prefer to call instead, Salutary Data lists a phone number, 617-917-4084, on its site.
6. Note this stops future sale/sharing only -- any of your business-contact data already delivered to a customer via a prior data feed will not be recalled.
