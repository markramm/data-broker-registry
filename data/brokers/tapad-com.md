---
id: tapad-com
name: Tapad
domain: tapad.com
category: adtech_identity_graph
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://crportal.tapad.com"
opt_out_email: null
phone: "855-927-0800"
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, other]
readd_days: null
legal_basis: [ccpa, cpra, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "Tapad (owned by Experian) operates a cross-device identity graph used for ad targeting/measurement -- it links a person's devices together rather than reselling names/addresses for lookup, so people_search is false but the identity-graph function still makes this a real, high-impact opt-out. WebFetch on tapad.com's privacy notice (redirects to www.tapad.com/global-privacy-notice) confirmed a 'Consumer Rights Request Portal' at https://crportal.tapad.com, reachable via 'Opt-out' or 'Do Not Sell My Personal Information' buttons that the notice says function identically; phone alternative 855-927-0800 is also listed for submitting requests. The portal itself is a JS-rendered form that WebFetch could not read field-by-field, so exact required fields/CAPTCHA presence on that page are not directly confirmed -- captcha marked true and tier kept guided out of caution. last_verified left null."
---

1. Go to Tapad's Consumer Rights Request Portal at https://crportal.tapad.com.
2. Choose either "Opt-out" or "Do Not Sell My Personal Information" -- Tapad states both function the same way and remove you from its device Graph.
3. Follow the portal's prompts, providing the identifying information it requests (typically an email address), and complete any CAPTCHA or verification step.
4. Submit the request and watch for a confirmation email.
5. If you'd rather not use the web portal, call 855-927-0800 to submit your opt-out request by phone.
