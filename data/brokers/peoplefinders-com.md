---
id: peoplefinders-com
name: Peoplefinders.com
domain: peoplefinders.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.peoplefinders.com/do-not-sell"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: data-brokers-watch
notes: "Direct fetch of the migrated privacy.aspx URL returned only a bare footer link with no form content; corrected opt_out_url to PeopleFinders' actual 'Do Not Sell My Personal Information' page (found via WebSearch) and corrected category/people_search -- this is a people-search site, not a generic personal_information broker. Process is two-step: an initial name+email+CAPTCHA request form, followed by an emailed verification link that opens a second form for full record details. CAPTCHA at multiple steps -> guided. last_verified left null (not freshly fetched from the corrected URL)."
---

1. Go to peoplefinders.com and scroll to the footer, or go directly to peoplefinders.com/do-not-sell.
2. Enter your full name and a valid email address, select "The subject of the request" from the dropdown, and check the agreement box.
3. Complete the CAPTCHA and click "Send Request."
4. Check your email for a verification message from PeopleFinders and click "Click here to fill out the form."
5. Complete the follow-up form with your personal details, confirm the information is correct, complete the CAPTCHA again, and click "Submit."
6. Processing typically takes about 3 days; this suppresses the listing from search results (PeopleFinders states it does not delete the underlying record).
