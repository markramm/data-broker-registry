---
id: veeva-com
name: "Veeva Systems"
domain: veeva.com
category: b2b_saas_with_consumer_adtech
people_search: false
tier: guided
priority: standard
method: portal
opt_out_url: "https://www.veeva.com/privacy/do-not-sell-share/"
opt_out_email: null
phone: "1-877-807-3230"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: identity_confirmation
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch confirms Veeva Systems is fundamentally B2B enterprise software for the life-sciences/pharma industry (clinical trials, regulatory submissions, quality management, commercial CRM) -- matching the hint that it is likely not a consumer broker. However, its privacy notice discloses a secondary consumer-data business: 'healthcare marketing and analytic products' that source 'demographic and consumer information from third-party consumer data partners' to build ad-targeting audience segments, and it explicitly states 'Any U.S. resident may opt out of the sale or sharing of their personal information within our consumer-based advertising products.' The opt-out is via a dedicated page (veeva.com/privacy/do-not-sell-share/) that routes into a OneTrust privacy portal (privacyportal.onetrust.com) where the requester selects a relationship type ('Consumer' vs 'Healthcare Professional or Scientific Expert'), or by calling 1-877-807-3230. Exact form fields/CAPTCHA on the OneTrust portal itself were not directly observed (page summarized rather than fully rendered), and OneTrust portals commonly require email verification -- classified guided out of caution given the multi-step portal + relationship-type branching. Primarily B2B with only a secondary consumer-ad data flow -> priority standard. last_verified left null."
---

1. Go to Veeva's "Do Not Sell or Share My Personal Information" page at [veeva.com/privacy/do-not-sell-share](https://www.veeva.com/privacy/do-not-sell-share/).
2. Click through to the linked privacy-rights portal (hosted on OneTrust).
3. When prompted to select your relationship to Veeva, choose "Consumer" (not "Healthcare Professional or Scientific Expert").
4. Complete the portal's request form with your name and email address, and verify your identity/email if prompted.
5. Submit the request and watch for a confirmation email; follow any verification link it contains.
6. Alternatively, call Veeva toll-free at 1-877-807-3230 to request the same opt-out by phone.
