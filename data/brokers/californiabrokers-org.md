---
id: californiabrokers-org
name: California Brokers (licensedata.org network)
domain: californiabrokers.org
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
notes: "californiabrokers.org is NOT a state licensing board -- it is an independent, unofficial directory that republishes California real estate broker license records (name, license status/number, renewal dates) with a search/browse UI and user reviews. It is one of a confirmed family of near-identical sites (californiabrokers.org, californiaengineering.org, californialicensing.org, californianursing.org, californiapharmacists.org, plus others referenced in their shared footer such as 'California Contractors' and 'California Dentists') that cross-link each other and share the exact same removal/contact infrastructure. Confirmed via WebFetch of each site's /contact page: all use Cloudflare email-obfuscation resolving to removals@licensedata.org and contact@licensedata.org (decoded the cloudflare cdn-cgi/l/email-protection hex payloads directly), establishing a single common operator running under the licensedata.org backend. The site explicitly discourages delisting ('doing so will prevent others from verifying your license') but does process removal-by-email requests, identified by a per-record ID shown on each license listing. Since it publishes business/professional license info (not home addresses) with a working, direct-email opt-out and no CAPTCHA/ID gate described -> tier:auto, method:email. people_search left false (this is a professional-license registry, not a general identity/address lookup), but priority:high given it publishes named individuals' license records publicly with reviews and only a narrow, easy-to-miss removal path. opt_out_url left null because the removal flow requires locating your own listing's page (which contains a per-record ID) rather than a fixed opt-out landing page."
---

1. Go to https://www.californiabrokers.org/ and search for your own name to find your license listing.
2. Open your listing and note the record ID shown in the bottom-right corner of the license-details block -- you'll need this for the removal request.
3. Email removals@licensedata.org and include the record ID plus your full name as it appears on the listing, asking that your record be removed from californiabrokers.org.
4. Note that the site explicitly warns that removing your listing may make it harder for others to verify your license through this particular (unofficial) site -- your official license status remains verifiable through the California Department of Real Estate regardless.
5. Because this site is part of a shared network (californiaengineering.org, californialicensing.org, californianursing.org, californiapharmacists.org, and others) run by the same operator, a removal request to removals@licensedata.org may need to be repeated separately for each site where your license type has its own listing -- check the related sites linked in the footer if you hold multiple licenses.
