---
id: firearmscalifornia-org
name: Firearms California (licensedata.org network)
domain: firearmscalifornia.org
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
required_fields: [listing_url, email]
readd_days: null
legal_basis: [none]
last_verified: null
source: "dbw+tcp-research"
notes: "firearmscalifornia.org is part of the same unofficial licensedata.org network already documented at californiabrokers.org: an independent directory (here 'Search 199,780 firearms permit holders licensed in California') that republishes California firearms-permit records with reviews, and cross-links companion sites (California Notaries, California Pharmacists, California Licensing, California Security, California Brokers) in its footer. Confirmed via curl of firearmscalifornia.org/about and /contact: both pages carry Cloudflare cdn-cgi/l/email-protection obfuscated addresses. Decoded the hex payloads directly (XOR against the leading key byte, same technique used for californiabrokers.org) and both pages resolve to the same two addresses used across the network: removals@licensedata.org (removal-specific) and contact@licensedata.org (general). Direct email opt-out, no CAPTCHA/ID gate described -> tier:auto, method:email. people_search left false (professional/permit license registry, not general identity/address lookup) but priority:high since it publishes named individuals' permit records publicly with reviews behind an easy-to-miss removal path. opt_out_url left null -- removal requires locating your own listing's record ID first, there is no fixed opt-out landing page."
---

1. Go to https://www.firearmscalifornia.org/ and search for your own name to find your permit listing.
2. Open your listing and note the record ID shown on the license-details page -- you'll need this for the removal request.
3. Email removals@licensedata.org with the record ID and your full name as it appears on the listing, asking that your record be removed from firearmscalifornia.org.
4. Because this site is part of a shared network run by the same operator (California Notaries, California Pharmacists, California Licensing, California Security, California Brokers, and others linked in the footer), you may need to repeat this request separately for each related site where you have a listing.
5. Your official permit status remains verifiable through the actual California issuing authority regardless of whether this unofficial listing is removed.
