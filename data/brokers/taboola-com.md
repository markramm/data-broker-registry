---
id: taboola-com
name: Taboola
domain: taboola.com
category: adtech_content_recommendation
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://ccparequest.taboola.com/"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: []
readd_days: null
legal_basis: [ccpa, cpra, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "Taboola is a major adtech/content-recommendation network (the 'around the web' widget boxes on news sites), not a people-search broker -- it profiles browsing behavior for ad targeting rather than reselling identity/address data. policies.taboola.com/privacy-policy/ section 5.2.1 points to the U.S. State Consumer Rights Portal at https://ccparequest.taboola.com/ for CCPA/CPRA opt-out of sale/share and cross-context behavioral advertising; accessrequest.taboola.com/access handles access/deletion. Updated 2026-10-17 by the daily maintainer after page-monitor #75: the portal now renders as a static page (fetched directly, HTTP 200, 'US State Privacy Rights'). It says Taboola holds only pseudonymized identifiers (cookie IDs, IP addresses, mobile ad IDs, sometimes a hashed email), and the opt-out is a single button ('I'd like to opt out from Taboola's disclosures, sharing and sales of my personal information') behind a visible reCAPTCHA (div.g-recaptcha) that sets a 'Do Not Sell' cookie in that browser. It asks for no name or email, so required_fields is now empty; it must be repeated on every browser and device, and does not work if cookies are blocked (Safari users must turn off cross-site tracking prevention first). Nothing was submitted; last_verified null."
---

1. Open https://ccparequest.taboola.com/ in the browser you want to opt out. The opt-out is stored as a cookie, so do not use a private window and do not block cookies for taboola.com.
2. On Safari (iOS/macOS), first turn off "Prevent Cross-Site Tracking" and "Block All Cookies" in Privacy settings, then reload the page. Clearing your cookies later also clears the opt-out.
3. Complete the reCAPTCHA, then click "I'd like to opt out from Taboola's disclosures, sharing and sales of my personal information." No name or email is asked for.
4. Check that "My Status" no longer says "Not Opted Out".
5. Repeat on every browser and device you use.
6. For an access or deletion request (rather than an opt-out of sharing), use Taboola's separate Data Subject Access Request portal at https://accessrequest.taboola.com/access.
