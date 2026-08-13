---
id: ip2location-com
name: Hexasoft Development Sdn. Bhd. (IP2Location)
domain: ip2location.com
category: adtech_identity
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://www.ip2location.com/do-not-sell"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, full_name, other]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on ip2location.com/do-not-sell succeeded and rendered a live, detailed opt-out form description. IP2Location/Hexasoft sells B2B IP-geolocation and network-intelligence data (country/region/city, ISP, ASN) rather than reselling individual identity lookups, so people_search:false. The 'Do Not Sell My Info' form requires name, email, the IP address(es) associated with the requester's data, request type, and a scope preference (delete all data vs. retain only country-level info), plus an authorization confirmation if requesting on behalf of someone else -- no CAPTCHA or ID upload mentioned in the fetched content, and the company says it may request further verification by email for residency confirmation. Classified tier:assisted (simple form, no CAPTCHA/ID) rather than guided. required_fields includes 'other' for the IP-address field, which has no dedicated schema enum value."
---

1. Go to https://www.ip2location.com/do-not-sell.
2. Fill in your name, email address, and the IP address(es) you believe are associated with your data (check 'what is my IP' if unsure).
3. Select the request type -- e.g., "I want you to not sell my personal data" -- and choose whether you want all associated data deleted or only country-level information retained.
4. If you are submitting the request on someone else's behalf, complete the authorization confirmation section.
5. Submit the form. IP2Location may follow up by email to verify your residency (e.g., California, EU, UK) before completing the request.
