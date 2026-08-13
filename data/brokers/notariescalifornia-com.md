---
id: notariescalifornia-com
name: "California Notaries (licensedata.org network)"
domain: notariescalifornia.com
category: professional_license_registry
people_search: false
tier: auto
priority: high
method: email
opt_out_url: null
opt_out_email: "removals@licensedata.org"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, email, full_name]
readd_days: null
legal_basis: [none]
last_verified: null
source: "dbw+tcp-research"
notes: "notariescalifornia.com is part of the same unofficial licensedata.org network already documented at californiabrokers.org, firearmscalifornia.org, californianursing.org, etc: an independent directory (here 'Search 209,729 notaries licensed in California') that republishes California notary-license records with a search UI and reviews, and cross-links companion sites (nursing, dentistry, security, pharmacists, brokers, firearms) in its footer. Confirmed via direct curl fetch of notariescalifornia.com/about (HTTP 200) and decoded the two Cloudflare cdn-cgi/l/email-protection obfuscated addresses directly (XOR against the leading key byte): removals@licensedata.org (for removal requests, referencing a per-record ID shown on each license listing) and contact@licensedata.org (general inquiries). Same operator/backend as the rest of the confirmed licensedata.org family. Direct email opt-out, no CAPTCHA/ID gate described -> tier:auto, method:email. people_search left false (professional-license registry, not general identity/address lookup) but priority:high since it publishes named individuals' license records publicly with reviews behind an easy-to-miss removal path. opt_out_url left null -- removal requires locating your own listing's record ID first; there is no fixed opt-out landing page."
---

1. Go to https://www.notariescalifornia.com/ and search for your own name to find your notary license listing.
2. Open your listing and note the record ID shown on the bottom-right corner of the license-details block -- you'll need this for the removal request.
3. Email removals@licensedata.org with the record ID and your full name as it appears on the listing, asking that your record be removed from notariescalifornia.com.
4. Because this site is part of a shared network run by the same operator (California Nursing, California Pharmacists, California Licensing, California Security, California Brokers, California Firearms, and others linked in the footer), you may need to repeat this request separately for each related site where you have a listing.
5. Your official notary commission status remains verifiable through the California Secretary of State regardless of whether this unofficial listing is removed.
