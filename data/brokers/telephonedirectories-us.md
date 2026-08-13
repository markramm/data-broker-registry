---
id: telephonedirectories-us
name: Telephone Directories
domain: telephonedirectories.us
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.telephonedirectories.us/Edit_Records"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirmed genuine people-search site: WebFetch on the homepage described 'easy tools to find people by name, phone number, address or email' claiming 500M+ records, sourced from public records, with an explicit FCRA disclaimer (not a consumer reporting agency). A curl fetch of https://www.telephonedirectories.us/Edit_Records returned a real page (title 'Edit records from our database | Telephone Directories'), confirming the removal page exists, but it's a JS-rendered single-page app -- raw HTML didn't expose the actual form fields or confirm CAPTCHA presence. Footer/homepage also references a 'Do Not Sell My Info' link. Given real personal-safety stakes (address/phone lookup) and unconfirmed CAPTCHA, classified people_search:true, crucial priority, guided tier with captcha assumed true out of caution. last_verified left null since the form itself wasn't rendered."
---

1. Search your name or phone number on telephonedirectories.us and open any profile that matches you; copy that profile's URL.
2. Go to the removal page at https://www.telephonedirectories.us/Edit_Records.
3. Paste in the profile URL (or the identifying details the form requests) and provide an email address for confirmation.
4. Complete any CAPTCHA the page presents and submit the removal request.
5. Check your email for a confirmation message and confirm if a link is provided.
6. Repeat for each distinct matching listing, since the site may hold multiple profiles per person; re-check periodically in case listings reappear after a future scrape.
