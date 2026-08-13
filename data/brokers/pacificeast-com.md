---
id: pacificeast-com
name: "PacificEast Research Inc."
domain: pacificeast.com
category: data_enrichment_verification
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.pacificeast.com/contact-us-privacy/"
opt_out_email: "privacy@pacificeast.com"
phone: "800-665-8400"
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, address, phone]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "curl-fetched pacificeast.com/contact-us-privacy/ directly (HTTP 200, full static HTML, no JS rendering needed) and confirmed the page content verbatim: it is titled 'Do Not Sell or Share My Personal Information' and states PacificEast provides BrandDelivery (caller-ID branding), Data Enrichment, and Data Verification services to healthcare, nonprofit, financial, and retail clients -- a B2B contact-data broker, not a consumer-facing people-search site. The page states PacificEast 'does not maintain or store consumer information' on an ongoing basis but offers an opt-out form (or email to privacy@pacificeast.com) for consumers whose info 'passes through' its systems. Form fields confirmed from the raw HTML: First Name, Last Name, Phone Number, Email Address, Address, City, State, Zip, an identity/authorization confirmation checkbox, an anti-automation confirmation checkbox, and a CAPTCHA. Also lists hello@pacificeast.com as a general contact and 800-665-8400 as a phone number (used here as the general company phone, distinct from the privacy email). CAPTCHA-gated multi-field form -> tier guided. Not independently re-verified beyond this session's fetch; last_verified left null per instructions."
---

1. Go to PacificEast's opt-out page at https://www.pacificeast.com/contact-us-privacy/ ("Do Not Sell or Share My Personal Information").
2. Fill in the form with your first name, last name, phone number, email address, and full mailing address (street, city, state, zip) -- PacificEast requires complete, accurate information to verify and process the request; incomplete submissions are rejected.
3. Check the box confirming you are the person identified in the request (or are legally authorized to submit it on their behalf), and the box confirming the submission is not from an automated third-party service.
4. Complete the CAPTCHA and click "Submit Opt-Out Request."
5. Watch the email address you provided for follow-up correspondence -- PacificEast communicates about the request status by email and may ask for additional verification.
6. Alternatively, skip the form and email privacy@pacificeast.com directly with the same information (name, phone, email, address) to request an opt-out.
