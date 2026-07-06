---
id: addresses-com
name: Addresses.Com
domain: addresses.com
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://www.addresses.com/optout.php"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: ["listing_url", "full_name", "email"]
readd_days: null
legal_basis: []
last_verified: null
source: "data-brokers-watch + tcp-verified"
notes: "MIGRATED research_note: own opt-out form; bot-block 403, live. WebFetch returned HTTP 403 (bot-blocked) both in this session and per prior TCP research -- could not freshly confirm, so last_verified stays null. Addresses.com is part of the same family of simple own-hosted people-search opt-out forms as its sibling sites (name + listing URL + email, no CAPTCHA/ID); treated as assisted based on that pattern and third-party removal guides. People-search site with address/phone lookups, so priority crucial."
---

1. Search your own name on [Addresses.com](https://www.addresses.com) to find your listing.
2. Copy the full URL of your listing from the address bar.
3. Go to the [Addresses.com opt-out form](https://www.addresses.com/optout.php).
4. Paste in your listing URL, and enter your full name and an email address you can access.
5. Submit the form and watch for an on-screen confirmation that the request was received.
6. Check back after a few days to confirm the listing is gone -- it can reappear if the underlying public-record source is re-scraped.
