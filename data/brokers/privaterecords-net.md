---
id: privaterecords-net
name: "PrivateRecords"
domain: privaterecords.net
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://www.privaterecords.net/api/helper/optOutLight/search"
opt_out_email: "support@privaterecords.net"
phone: "1-888-270-9304"
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
notes: "Authored 2026-10-20 by the daily maintainer from California's data broker registry (Private Records LLC, support@privaterecords.net). The registry also lists peoplesearch123.com, backgroundcheckers.net and personsearchers.com; none of these were fetched. The homepage (redirects to /name/landing, HTTP 200) is a public-records and people search ('search over 12 billion public records'), so people_search is true and priority is crucial. Pages were rendered in a headless browser. The footer links 'Do Not Sell Or Share My Personal Info' and 'Limit The Use of My Sensitive Personal Info' both go to https://www.privaterecords.net/api/helper/optOutLight/search ('Privacy Requests', HTTP 200). This is the same request page used by peoplesearcher.com and checksecrets.com. It offers two requests. 'Your Privacy Choices' only stops sale/sharing, accepts an email or a phone number, and states that it does not remove a listing. 'Remove My Information' (?type=removal) requires first and last name, birth month/day/year, city, ZIP, state, and an email address that receives a confirmation link. The page says nothing is removed until that link is clicked. Requests are acknowledged within 10 business days and completed within 45 calendar days. Phone requests go to (888) 270-9304. No CAPTCHA widget or script was present on either form when rendered, so the tier is assisted. A CAPTCHA could still appear on submit; that was not tested. Nothing was submitted; last_verified is null."
---

1. Go to https://www.privaterecords.net/api/helper/optOutLight/search. The site footer also links to it as "Do Not Sell Or Share My Personal Info".
2. Choose "Remove My Information". "Your Privacy Choices" only stops sale and sharing, and your listing stays up.
3. Enter the first and last name, birth date (month, day and year), city, ZIP code and state of the person in the listing.
4. Enter an email address for the confirmation link, then click "Submit removal request".
5. Open the confirmation email and click the link. Nothing is removed until you do.
6. PrivateRecords says it acknowledges requests within 10 business days and completes them within 45 days. Search the site again after that to check.
7. If the link never arrives, or you'd rather not use the form, call (888) 270-9304.
