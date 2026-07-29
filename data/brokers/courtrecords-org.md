---
id: courtrecords-org
name: "CourtRecords.org"
domain: courtrecords.org
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.courtrecords.org/lp_optout.php"
opt_out_email: null
phone: "800-309-9351"
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: ["full_name", "listing_url"]
readd_days: null
legal_basis: []
last_verified: null
source: "data-brokers-watch + tcp-research"
notes: "Confirmed a real, serious security problem directly: the TLS certificate for members.courtrecords.org (the opt-out subdomain referenced by third-party guides, same members.<domain>/customer/opt-out URL pattern as criminalpages.com) is CN=*.courtrecords.org but EXPIRED 2022-09-25 -- almost four years ago -- verified via curl/openssl handshake ('certificate has expired'). The public-facing apex/www opt-out flow at courtrecords.org/lp_optout.php is documented consistently across multiple independent 2025-2026 guides (brandyourself, optery, deletemyinfo): search your name, copy the 'Buy Full Report' link for your listing (this becomes the listing_url/Record ID), go to the opt-out page, paste it in with your name, solve a CAPTCHA, and submit; processing takes 2-15 business days. WebFetch attempts to load the opt-out page directly hit connection resets, so last_verified is left null despite the corroborating guides and the confirmed cert problem on the members subdomain. Same InfoTracer-family URL pattern as criminalpages.com (members.*.org/customer/opt-out, PO Box 990142 Boston MA fax number reused across the family) -- likely shares infrastructure/ownership. People-search site with real personal-safety impact -> crucial priority despite the trust problem."
---

1. Go to [courtrecords.org](https://www.courtrecords.org/) and search your name to find your listing.
2. Copy the link address behind that listing's "Buy Full Report" button -- this is the Record ID/listing URL you'll need for the opt-out form.
3. Go to the opt-out form at [courtrecords.org/lp_optout.php](https://www.courtrecords.org/lp_optout.php), paste in the listing URL, fill in your name, solve the CAPTCHA, and submit.
4. Caution: a related subdomain used by this same operator (members.courtrecords.org) is currently presenting an SSL certificate that expired in September 2022 -- if your browser shows a certificate-expired warning anywhere in this flow, do not enter personal information past that warning; stick to the courtrecords.org/lp_optout.php path described above instead.
5. If you're a judge, prosecutor, law enforcement officer, or immediate family member covered by the Daniel Anderl Judicial Security and Privacy Act, you can instead email privacy@courtrecords.us for expedited removal.
6. Expect removal within 2-15 business days; you can also call 800-309-9351 with questions, though this number is shared with other sites in the same operator family (InfoTracer-linked, per Criminal Pages' listing) so confirm you're speaking about CourtRecords.org specifically.
