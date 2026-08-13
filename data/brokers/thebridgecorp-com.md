---
id: thebridgecorp-com
name: BRIDGE
domain: thebridgecorp.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://thebridgecorp.com/opt-out/"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, other]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "BRIDGE (thebridgecorp.com) is a people-based marketing/audience-matching data broker; its own site footer states it is 'a registered data broker in California, Oregon, Texas, and Vermont' and describes a database of '250 million verified humans' matched across offline and digital identifiers -- a real, high-impact broker, though not a public-facing individual people-search/lookup tool. WebFetch on https://thebridgecorp.com/opt-out/ rendered a real 'Do Not Sell or Share My Personal Information' form: fields are state of residency (CA resident / non-CA resident dropdown), email address, advertising ID (appears optional), request type (Request Information / Delete My Record / Opt Out), an attestation checkbox, and full name -- no CAPTCHA and no physical address required. Company also states it honors Global Privacy Control signals. Classified assisted tier given the confirmed no-CAPTCHA/no-ID form; high priority given the scale of the identity-matching database, though not people_search since it isn't a consumer-facing lookup product. last_verified left null since this was model-summarized page content, not a rendering I visually confirmed myself."
---

1. Go to BRIDGE's opt-out form at https://thebridgecorp.com/opt-out/.
2. Select your state of residency (California resident or non-California resident).
3. Enter your email address. If you know your mobile advertising ID (IDFA/AAID), you can optionally include it to help match your record.
4. Choose "Opt Out" as the request type (you can also select "Delete My Record" for a fuller deletion request).
5. Check the attestation box confirming the information you submitted is true and correct, and enter your full name.
6. Submit the form. BRIDGE also states it honors Global Privacy Control (GPC) browser signals, which may suppress sale/sharing automatically if you have GPC enabled.
