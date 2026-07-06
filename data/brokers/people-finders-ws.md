---
id: people-finders-ws
name: people-finders.ws
domain: people-finders.ws
category: data_brokers
people_search: false
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.peoplefinders.com/opt-out"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, full_name, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: data-brokers-watch
notes: "people-finders.ws (note the .ws TLD) redirects -- confirmed live via curl -- to www.peoplefinders.com/privacy.aspx, which itself redirects to the peoplefinders.com root, meaning the original .aspx path is stale. peoplefinders.com is a well-known people-search broker and returned a Cloudflare bot-challenge 403 on direct fetch, so the exact current opt-out page content couldn't be rendered; last_verified stays null. Updated opt_out_url to PeopleFinders' known dedicated opt-out page (peoplefinders.com/opt-out) since the old people-finders.ws privacy.aspx path no longer resolves to anything specific. NOTE: category/people_search were left as migrated (data_brokers / false) per instructions not to break existing classification fields, but this is functionally a people-search site (PeopleFinders.com) and priority is set to crucial accordingly -- a human should consider correcting category/people_search to people_search/true in a follow-up pass, since the migrated categorization looks wrong here."
---

1. Search for your own name on PeopleFinders.com to locate your listing, and copy its exact profile URL.
2. Go to the PeopleFinders opt-out page (peoplefinders.com/opt-out).
3. Enter your full name and address as prompted, and paste in the listing URL you found.
4. Complete the CAPTCHA challenge if presented.
5. Submit the removal request and watch for a confirmation email.
6. Because PeopleFinders shares infrastructure/data with sister people-search brands, check whether your listing also appears on related sites (some are owned by the same parent company) and repeat the opt-out there if so.
