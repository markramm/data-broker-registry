---
id: reonomy-com
name: "Reonomy"
domain: reonomy.com
category: commercial_real_estate_data
people_search: false
tier: auto
priority: standard
method: email
opt_out_url: "<verify: Reonomy's Location-Based Rights Notice / CCPA opt-out page, referenced from reonomy.com/legal/privacy-policy/ but not directly located>"
opt_out_email: "support@reonomy.com"
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
notes: "Fetched reonomy.com and reonomy.com/legal/privacy-policy/. Reonomy is a commercial real-estate data platform (property ownership records, LLC/holding-company structures, business decision-maker contacts) for CRE professionals, not a consumer people-search site. Its own privacy policy's CCPA disclosure table marks 'identifiers,' 'commercial information,' and 'professional data' as having been sold in the past 12 months, and directs consumers to a separate 'Location-Based Rights Notice' for the actual opt-out mechanism -- that notice page was not located at a stable URL during this session (searches for /legal/privacy-policy/ and /privacy-policy/ returned inconsistent results), so opt_out_url is a verify-placeholder and last_verified is null. The policy does give a working contact address (support@reonomy.com) for rights requests, which is what this entry uses as the actionable channel meanwhile. Standard priority: B2B commercial-property data, not personal address/identity resale to the public, despite the technical 'sale of identifiers' disclosure."
---

1. Email support@reonomy.com and request a CCPA data-subject rights action (access, deletion, or opt-out of sale) for your personal information.
2. Include your full name and the email address(es)/contact details you believe Reonomy holds (e.g., as a property owner, LLC member, or business contact surfaced in their commercial real estate data).
3. Reonomy's privacy policy references a separate "Location-Based Rights Notice" with more specific opt-out instructions for California and other state residents; look for a link to this notice from the privacy policy page at reonomy.com/legal/privacy-policy/ and follow its process if found, since it may supersede the email-only path above.
4. Note that Reonomy's data is primarily about commercial properties and the business entities/decision-makers tied to them, not general consumer address/phone lookups -- expect a slower, human-processed response rather than a self-serve form.
5. Follow up if you do not receive a response within a reasonable time, since no fixed response SLA was found in the fetched policy text.
