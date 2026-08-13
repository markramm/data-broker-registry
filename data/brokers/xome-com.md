---
id: xome-com
name: "Xome Inc."
domain: xome.com
category: real_estate_data
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "https://www.xome.com/pages/privacy-policy"
opt_out_email: "info@xome.com"
phone: "800-758-8052"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [full_name, address, email]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on xome.com/pages/privacy-policy succeeded and rendered CCPA section text. Xome is a real-estate/property-data and auction marketplace (foreclosure/title/valuation listings), operating alongside affiliated licensed-brokerage entities (Xome Realty Services LLC, Xome CT LLC, Xome PR LLC, Xome OH LLC per the site's terms of use). Not classified people_search -- it publishes property/listing data rather than operating as a person-lookup engine, though property records can include owner names. The privacy policy lists three opt-out routes: the 'Do Not Sell or Share My Personal Information' footer link, email, and a toll-free phone line (800-758-8052), plus honoring Global Privacy Control signals; email confirmed via direct fetch as info@xome.com (a raw curl of the page also surfaced only info@xome.com -- no other opt-out address appeared). The legacy repo CSV (data/legacy/data-brokers-watch-source.csv) lists a different address, licensing@xome.com, tied to both 'xome.com' and a related row for 'eleadz.com' / 'Xome Leads LLC' at the same Lewisville, TX address -- that entry appears to be an older/lead-generation-specific contact and was NOT found anywhere in the current live privacy policy, so it is not used here. eleadz.com is a separate domain not in this batch and was not authored. No CAPTCHA or ID requirement found in the policy text for the email/phone opt-out routes, but the actual footer form itself was not directly rendered (JS-heavy page), so tier is left at guided rather than assisted out of caution. last_verified left null."
---

1. Go to https://www.xome.com and scroll to the site footer, then click "Do Not Sell or Share My Personal Information."
2. If the on-site form doesn't load or you prefer not to use it, email info@xome.com and state that you are exercising your CCPA/CPRA right to opt out of the sale or sharing of your personal information, or to request deletion.
3. Include your full name and the address or property listing you believe Xome has associated with you, since Xome's policy notes it may ask current customers for full name and address to process deletion requests.
4. Alternatively, call Xome's privacy line at 800-758-8052 to submit the request by phone.
5. If your browser sends a Global Privacy Control (GPC) signal, Xome states it will honor that as an opt-out-of-sale request automatically for that browser/device.
6. You can also open the cookie-preference icon in the bottom-left corner of xome.com or valueyourhome.com to manage tracking-cookie consent separately from the sale/sharing opt-out.
