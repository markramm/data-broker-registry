---
id: dexknows-com
name: "DexKnows (Thryv)"
domain: dexknows.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://www.dexknows.com/info/ccpa"
opt_out_email: "privacy@thryv.com"
phone: "1-877-243-8339"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: ["other"]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "dexknows.com is a business directory operated by Thryv (formerly Dex Media); direct WebFetch of dexknows.com and dexknows.com/info/ccpa both returned HTTP 403 (bot-blocked), so I could not render the live page myself. Per WebSearch results (the dexknows.com/info/ccpa page text as indexed, plus third-party opt-out guides from Optery, GuaranteedRemovals, EraseMe, NetReputation, and OneRep, which are independently consistent), Thryv/DexKnows participates in ad networks that constitute a 'sale/share' of personal info under CCPA/VCDPA/etc., and offers a 'Do Not Sell or Share My Personal Information' cookie-based button on the site, plus email to privacy@thryv.com and Thryv's own data-brokers opt-out form at thryv.com/privacy-ccpa/ (confirmed live via WebFetch: a simple one-click cookie-based opt-out button, no CAPTCHA, no form fields, scoped to thryv.com though the dexknows.com-specific /info/ccpa page presumably mirrors this). The legacy CSV's green.dexknows.com/DexGreen subdomain no longer resolves (DNS failure), confirming that mechanism is deprecated. Older guides also mention a phone option, 1-877-243-8339. Not independently re-verified against a live dexknows.com render due to bot-blocking -- assisted tier given the underlying mechanism (cookie button / simple form) has no CAPTCHA or ID gating in any source consulted."
---

1. Go to https://www.dexknows.com/info/ccpa (DexKnows' dedicated CCPA rights page).
2. Click the "Do Not Sell or Share My Personal Information" button described on that page -- this sets an opt-out cookie in your browser for cross-contextual/behavioral advertising sharing tied to dexknows.com.
3. Note that this opt-out is cookie-based: if you clear your browser cookies or switch browsers/devices later, you'll need to repeat this step.
4. If you'd prefer a direct request instead of (or in addition to) the cookie button, email privacy@thryv.com and ask to opt out of sale/sharing of your personal information collected via dexknows.com, or call 1-877-243-8339.
5. For listing-specific concerns (e.g. an inaccurate business/personal listing on DexKnows itself), use the same CCPA page's request options, since Thryv/DexKnows consolidated its opt-out handling under its parent Thryv privacy program.
