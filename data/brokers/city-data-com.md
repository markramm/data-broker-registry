---
id: city-data-com
name: City-Data.com
domain: city-data.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.city-data.com/delrequest/form.php"
opt_out_email: null
phone: "(650) 204-0028"
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, email, full_name, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on city-data.com/delrequest/form.php rendered successfully: a removal form requiring first name, last name, email, state, county, city, and the specific page URL to be delisted (one request per link), plus an image CAPTCHA. City-Data is primarily a city-statistics/forum site but also republishes property-assessment records (34M+ properties) tied to individual names on per-property pages, which is the people-search-relevant surface here -- removal only hides the name from the assessment page, not the property/address data itself, and does not affect search-engine caches. Given the CAPTCHA and the property-record personal-safety angle, classified people_search:true, tier:guided, priority:crucial. last_verified left null (WebFetch render, not a live human session)."
---

1. Find the specific city-data.com page showing your name (typically a property/assessment page or forum post) and copy its exact URL.
2. Go to the [City-Data removal request form](https://www.city-data.com/delrequest/form.php).
3. Enter your first name, last name, email address, and the state, county, and city as listed on the page.
4. Paste the page URL into the address/link field, optionally note a reason for the request, and solve the image CAPTCHA.
5. Submit the form. City-Data states it will instruct partner sites not to display your profile in their results as well; allow 24-48 hours for the change to take effect.
6. Submit a separate request for each distinct page/link showing your name -- one request only covers one URL. Note that the underlying property/address data itself typically remains listed; only your name is suppressed from the page.
7. If you're a government or law-enforcement official needing expedited handling, the form has an optional checkbox for that which requires your work position and a verifiable phone number.
