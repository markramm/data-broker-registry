---
id: weinform-org
name: "WeInform"
domain: weinform.org
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://www.weinform.org/api/helper/optOutLight/search"
opt_out_email: null
phone: "(855) 879-0159"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [full_name, dob, address, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-10-22 by the daily maintainer from California's data broker registry (We Inform LLC; registry contact support@weinform.org; the registry also lists truthrecord.org for the same company). The site is a JavaScript app, so plain fetches return an empty shell; it was loaded in a headless browser instead. The homepage is a public-records name search ('over 12 billion public records') selling reports with contact details, criminal and court records, so people_search is true and priority is crucial. Its footer 'Remove My Information' link goes to https://www.weinform.org/api/helper/optOutLight/search?type=removal, and 'Do Not Sell My Info' to the same page without the query string. That page offers two separate requests: 'Your Privacy Choices' (email or phone only; stops sale/sharing, does not remove a listing) and 'Remove My Information' (first and last name, date of birth, city, ZIP and state, plus an email for a confirmation link; nothing is removed until the link is clicked). It promises acknowledgement within 10 business days and completion within 45 days, with (855) 879-0159 as a phone alternative. No CAPTCHA was visible. truthrecord.org was also loaded: same site design, with its own copy of the same request page at https://www.truthrecord.org/api/helper/optOutLight/search; whether one removal covers both sites isn't stated. required_fields lists address because city, ZIP and state are required (a street address is not). Nothing was submitted; last_verified is null."
---

1. Go to https://www.weinform.org/api/helper/optOutLight/search (the "Remove My Information" link in the site footer).
2. Choose "Remove My Information". The other option, "Your Privacy Choices", only stops the sale and sharing of your data and leaves your listing on the site.
3. Enter the listed person's first and last name (no suffix such as Jr.), date of birth, city, ZIP code and state.
4. Enter an email address for the confirmation link and submit the removal request.
5. Open the email from WeInform and click the confirmation link. Nothing is removed until you do.
6. Optionally, go back to the same page, choose "Your Privacy Choices", and enter your email or phone number to stop the sale and sharing of your information as well.
7. The same company runs TruthRecord. It isn't clear that one request covers both sites, so repeat steps 2 to 5 at https://www.truthrecord.org/api/helper/optOutLight/search.
8. Removal should be finished within 45 days. If the confirmation email never arrives, call (855) 879-0159 and they will do the request with you.
