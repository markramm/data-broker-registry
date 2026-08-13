---
id: truepeoplesearch-net
name: TruePeopleSearch.net
domain: truepeoplesearch.net
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://truepeoplesearch.net/remove-my-info"
opt_out_email: "<verify: contact email is Cloudflare-obfuscated on /contact, could not be decoded without JS rendering>"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirmed via WebFetch that truepeoplesearch.net is LIVE and is a DISTINCT operator from truepeoplesearch.com -- not a redirect or alias. Its own copyright footer reads 'Copyright 2026 TruePeopleSearch.net' (vs. truepeoplesearch.com's separate branding/phone numbers). Its /terms page names a legal-notice address of 'NanShan District, Liuxian Avenue' (a district/street in Shenzhen, China) paired with a nonsensical governing-law clause ('courts located within Netherlands County, California' -- no such county exists), strongly suggesting boilerplate/templated ToS from an unrelated or offshore operator rather than truepeoplesearch.com's known US operation. No legal entity name, business address, or incorporation state is disclosed anywhere on the site. Removal process at /remove-my-info directs users to a third-party Google Form (docs.google.com/forms/d/e/1FAIpQLSeCPggzv4iXE20iUjcr6vdVWxBOblCyGwDLcO-jZA5j2YF5fQ/viewform) rather than a hosted opt-out flow; page text does not enumerate required fields, but people-search opt-out forms of this type typically ask for the profile/listing URL and an email. No CAPTCHA, ID, phone, or fee was mentioned on the removal page itself, but given the opaque operator, unnamed legal entity, and reliance on an external Google Form (which could change or disappear without notice), classified as guided/crucial out of caution rather than assisted. Contact-page email is Cloudflare email-protection-obfuscated and could not be decoded via WebFetch or curl; left as a verify placeholder rather than guessed. last_verified left null since no field here was confirmed against a freshly, fully rendered page with certainty (WebFetch summaries only, not manual render)."
---

<!-- Original instructions for TruePeopleSearch.net's Google-Form-based removal flow. -->
1. Search your name on truepeoplesearch.net and open the listing/profile that matches you; copy that listing's page URL.
2. Go to https://truepeoplesearch.net/remove-my-info and follow the link to the site's removal request form (currently hosted as a Google Form, not on the truepeoplesearch.net domain itself).
3. Paste your listing URL and enter your email address in the form; submit it.
4. If you have more than one matching listing on the site, submit a separate form for each one -- the site states it only processes one report per request.
5. Allow up to 48 hours for the listing to be removed from truepeoplesearch.net. Note the removal only affects this site's own listing, not copies on other people-search sites or government/public record sources.
6. If the form doesn't work or you have questions, use the "Contact Us" link in the site footer to reach support by email (no phone contact is listed).
7. Caution: this site's Terms of Use reference an overseas legal-notice address and do not name an operating company, and the removal flow depends on an external Google Form rather than the site's own infrastructure -- treat this as a lower-trust operator than the (also NOT the same company) truepeoplesearch.com, and consider it lower priority to revisit/re-check periodically since the process could change without notice.
