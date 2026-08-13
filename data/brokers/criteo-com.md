---
id: criteo-com
name: Criteo
domain: criteo.com
category: advertising_adtech
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.criteo.com/privacy/disable-criteo-services-on-internet-browsers/"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [other]
readd_days: null
legal_basis: [ccpa, cpra, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch confirmed criteo.com/privacy/ describes Criteo as a cross-context behavioral-advertising platform collecting cookie IDs, mobile ad IDs, hashed emails, IP addresses, browsing activity, and purchase/cart data, disclosed/sold to DSPs/SSPs/data platforms for retargeting -- a genuine adtech data broker. WebFetch on criteo.com/privacy/ccpa-privacy-policy/ found the CCPA opt-out mechanism is a 'Disable Criteo services' button linking to criteo.com/privacy/disable-criteo-services-on-internet-browsers/, which is a browser-based cookie/tracking opt-out rather than a personal-data-deletion form -- likely per-browser/per-device rather than a durable account-level opt-out, so classified guided rather than assisted. dpo@criteo.com is also available for GDPR/data-subject requests but not treated as the primary opt-out channel since the browser-disable flow is what CCPA users are directed to. Not independently re-rendered today -- last_verified left null."
---

1. Go to https://www.criteo.com/privacy/disable-criteo-services-on-internet-browsers/.
2. Follow the on-page instructions to disable Criteo's ad tracking in your current browser -- this typically sets an opt-out cookie or uses your browser/device's ad-ID reset mechanism.
3. Repeat this step separately in every browser and on every device you use, since the opt-out is tied to that specific browser/device rather than your identity as a whole.
4. If you clear cookies or use a different browser later, you will need to repeat the opt-out.
5. For a full CCPA/GDPR access, deletion, or "do not sell/share" request that goes beyond disabling tracking cookies, email Criteo's Data Protection Officer at dpo@criteo.com and describe the request; expect a response within the statutory window (typically 30-45 days).
