---
id: atriks-com
name: "Atriks, LLC"
domain: atriks.com
category: marketing_data_broker
people_search: false
tier: auto
priority: standard
method: email
opt_out_url: null
opt_out_email: "ccpa@atriks.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirmed via the California AG's data-broker registry (oag.ca.gov/data-broker/registration/191427) that Atriks LLC is a registered CA data broker whose registration lists ccpa@atriks.com as the CCPA opt-out/deletion contact and directs consumers to atriks.com/privacy.html for detailed instructions. Direct WebFetch to atriks.com/privacy.html returned HTTP 503 (twice, with a Retry-After header suggesting temporary rate-limiting/bot-blocking rather than the domain being dead) and a plain curl to the http:// version returned a redirect to the https version, confirming the domain is live and routes correctly, just not fetchable by this tool right now. Given the AG registration is itself an authoritative primary source for the opt-out contact, treating email as the confirmed auto-tier mechanism despite not rendering the privacy page directly. last_verified left null since the actual page content (any additional required fields) wasn't directly observed."
---

1. Send an email to ccpa@atriks.com requesting that Atriks, LLC opt you out of the sale/sharing of your personal information and/or delete the personal information it holds about you, per its California data-broker registration.
2. Include your full name and any other identifying details (such as a former address or email you may have provided to a company that shares data with Atriks) so they can locate your record.
3. For the complete, current opt-out process and any additional forms, check atriks.com/privacy.html directly, since Atriks may also offer a web form there.
4. Keep a copy of your email as proof of the request; Atriks does not appear to offer a self-serve confirmation page.
