---
id: unitedstatesphonebook-com
name: United States Phone Book
domain: unitedstatesphonebook.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "<verify: locate the per-listing 'remove' button; no standalone opt-out form page was found>"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Fetched unitedstatesphonebook.com and its privacy policy directly (HTTP 200 via curl with a browser user-agent; Claude's built-in WebFetch got 403). Site is a reverse-phone/people-search engine going by multiple aliases (also branded OldPhoneBook.com and AmericaPhoneBook.com per its own privacy policy), copyright-dated 2016, page last-edited note dated 2020-06-09. Footer text reads 'We are not a Data Broker' but the privacy policy simultaneously describes sourcing from public phonebooks and third parties -- functionally a people-search aggregator regardless of self-label. The privacy policy explicitly instructs: 'We will remove your data from this site upon your request... DO NOT EMAIL FOR REMOVALS, PLEASE USE THE REMOVE BUTTON NEXT TO THE LISTING' -- i.e. removal happens via a button attached to each individual listing, not a standalone opt-out page (a guessed /opt-out URL 404'd). No dedicated opt-out URL could be located without first finding a live listing, so opt_out_url is left as a verify-placeholder and last_verified is null. Site is Cloudflare-challenge protected (same cf$cv$params script seen elsewhere), hence captcha:true. The privacy-policy page also references a removal email but obscures it behind an anti-scraping 'email protected' placeholder, so opt_out_email is left null rather than guessed."
---

1. Go to https://unitedstatesphonebook.com and search by first name, last name (required), city, and state to find any listing matching you.
2. Open the matching listing page.
3. Look for a "remove" button or link next to the listing itself -- the site's own privacy policy insists removals must go through this in-listing control, not email.
4. Follow the removal flow presented by that button, which may include a Cloudflare bot-check.
5. Because the operator also runs OldPhoneBook.com and AmericaPhoneBook.com off the same data, you may need to search and repeat this process on those related domains as well.
6. Re-check periodically, since phone-book aggregators re-scrape public records.
