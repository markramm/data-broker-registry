---
id: truedata-co
name: TrueData
domain: truedata.co
category: adtech_data_broker
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://info-prod.truedata.co/opt-out-request"
opt_out_email: "privacy@truedata.co"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "Not to be confused with the unrelated stock-market/financial-data-feed company also called 'TrueData' (truedata.in/.tv). This truedata.co is a Texas-registered data broker (site footer states 'the entity maintaining this website is a data broker under Texas law') doing offline/identity-resolution data for digital advertising; recently acquired by ID5. WebFetch on the homepage and on /opt-out-request rendered directly (not bot-blocked): the opt-out form only requires country/state/email, with name/address/phone/mobile-ad-ID as optional fields, no CAPTCHA and no ID upload mentioned. WebFetch on /privacy-policy/ (a rendered PDF) confirmed the same opt-out URL plus a separate access/delete-request form at https://info-prod.truedata.co/access-delete-request and a privacy@truedata.co contact address for verification follow-up. Not a people-search site (no per-person profile pages found) -- classified as an adtech/marketing data broker, standard priority. tier set to assisted rather than auto because the primary documented path is the web form, not a plain email opt-out, even though the email address is also usable."
---

1. Go to https://info-prod.truedata.co/opt-out-request (TrueData's CCPA/CPRA "Do Not Sell My Personal Information" form).
2. Select your country and state, and enter your email address -- these are the only required fields.
3. Optionally add your full name, mailing address, phone number, or mobile/CTV advertising identifiers to make the suppression match more precise (TrueData notes a separate submission is needed per email address or device identifier).
4. Click Submit. No CAPTCHA or government ID is required based on the rendered form.
5. If you'd rather use email, write to privacy@truedata.co and state you are requesting to opt out of the sale/sharing of your personal information under CCPA/CPRA; TrueData may follow up to verify the request.
6. To request a copy of, or deletion of, the data TrueData holds on you, use the separate form at https://info-prod.truedata.co/access-delete-request.
7. Because TrueData works from identifiers (email hashes, mobile ad IDs, connected-TV IDs) rather than name/address lookups alone, consider submitting the opt-out for each email address and device identifier you use.
