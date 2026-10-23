---
id: privatereports-com
name: "PrivateReports"
domain: privatereports.com
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://www.privatereports.com/api/helper/optOutLight/search"
opt_out_email: null
phone: "(833) 783-0920"
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
notes: "Authored 2026-10-22 by the daily maintainer from California's data broker registry (Infomatics LLC; registry contact support@privatereports.com; the registry also lists mugshotlook.com and publicsearcher.com for the same company, which were not fetched). The site is a JavaScript app, so plain fetches return an empty shell; it was loaded in a headless browser instead. The homepage is a name search selling background reports (criminal records, address, phone, property, civil judgments), so people_search is true and priority is crucial. Its footer 'Do Not Sell My Info' and 'Limit The Use of My Sensitive Personal Info' links both go to https://www.privatereports.com/api/helper/optOutLight/search, a page offering two separate requests. 'Your Privacy Choices' takes only an email or a phone number and stops sale/sharing; the page says it does not remove a listing. 'Remove My Information' asks for the listed person's first and last name, date of birth, city, ZIP and state, plus an email for a confirmation link, and says nothing is removed until that link is clicked. It promises acknowledgement within 10 business days and completion within 45 days, and offers (833) 783-0920 as a phone alternative. No CAPTCHA was visible on either form. required_fields lists address because city, ZIP and state are required (a street address is not). Nothing was submitted; last_verified is null."
---

1. Go to https://www.privatereports.com/api/helper/optOutLight/search (the "Do Not Sell My Info" link in the site footer).
2. Choose "Remove My Information". The other option, "Your Privacy Choices", only stops the sale and sharing of your data and leaves your listing on the site.
3. Enter the listed person's first and last name (no suffix such as Jr.), date of birth, city, ZIP code and state.
4. Enter an email address for the confirmation link and submit the removal request.
5. Open the email from PrivateReports and click the confirmation link. Nothing is removed until you do.
6. Optionally, go back to the same page, choose "Your Privacy Choices", and enter your email or phone number to stop the sale and sharing of your information as well.
7. Removal should be finished within 45 days. If the confirmation email never arrives, call (833) 783-0920 and they will do the request with you. The same company also runs mugshotlook.com and publicsearcher.com, so check those sites for your listing too.
