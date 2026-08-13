---
id: dobsearch-com
name: DOBsearch
domain: dobsearch.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "<verify: dobsearch.com's people-finder opt-out/manage-listings flow -- both /people-finder/search-name.php and /people-finder/block-record-request.php now 301-redirect to a generic article page (how-to-find-information-someone-online), so the current working entry point could not be confirmed>"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: true
charges_fee: false
required_fields: [listing_url, full_name, email, phone]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "DOBsearch.com is an active people-search site (confirmed via WebFetch on its live homepage: name/phone/address/DOB lookups, background checks, 1M+ users claimed) -- this is a genuine people-search broker, not noise. Its own privacy policy (dobsearch.com/privacy-policy/) states it collects and uses personal data and offers a CCPA verifiable-request email, but the address is Cloudflare email-obfuscated and did not resolve to plain text via WebFetch or curl. Multiple 2026 third-party opt-out guides (DeleteMe, Optery) independently describe the same process: search your name (CAPTCHA-gated), select your listing, click 'Manage My Listings', type 'I Agree', then supply email and phone for verification via a confirmation code -- phone verification required, ~1 week to process. I directly tested both URLs those guides cite (people-finder/search-name.php and people-finder/block-record-request.php) and both now 301-redirect to a generic 'how to find information online' article, suggesting the site has restructured and the documented opt-out entry point may have moved -- left opt_out_url as a verify placeholder rather than publish a dead link. DeleteMe also notes opting out of BeenVerified auto-opts-out DobSearch, suggesting shared backend with a larger people-search network."
---

1. Go to dobsearch.com and use the People Search tool to search your own name; you will need to solve a CAPTCHA.
2. Locate the listing(s) that match you, check the box next to each one, and click "Manage My Listings."
3. Follow the on-screen prompts to request removal -- this typically requires typing "I Agree" to confirm, then entering your name, email address, and phone number.
4. DOBsearch will send a verification/confirmation code to your phone or email; enter it to complete the request.
5. Expect removal to take up to about a week. If the flow above has moved, use the site's contact page (dobsearch.com/contact/) or the CCPA request instructions in dobsearch.com/privacy-policy/ instead, and confirm the current URL before relying on it.
6. Because DOBsearch may share a backend with BeenVerified, also check whether opting out of BeenVerified separately removes your DOBsearch listing.
