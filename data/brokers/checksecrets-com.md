---
id: checksecrets-com
name: "CheckSecrets"
domain: checksecrets.com
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://www.checksecrets.com/api/helper/optOutLight/search"
opt_out_email: "support@checksecrets.com"
phone: "1-855-754-7951"
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
notes: "Authored 2026-10-20 by the daily maintainer from California's data broker registry (Truth Now LLC, support@checksecrets.com; the registry also lists peoplesearchUSA.org, inmatesearcher.com and sealedrecords.net, none of which were fetched). The homepage (redirects to /name/landing, HTTP 200) sells person, phone and inmate searches, so people_search true and priority crucial. Pages were rendered in a headless browser. The footer links 'Do Not Sell Or Share My Personal Info' and 'Limit The Use of My Sensitive Personal Info' both lead to https://www.checksecrets.com/api/helper/optOutLight/search ('Privacy Requests', HTTP 200). This is the same request page used by peoplesearcher.com. It offers two requests. 'Your Privacy Choices' only stops sale and sharing, takes an email or phone number, and says it does not remove a listing. 'Remove My Information' (?type=removal) requires first and last name, birth month/day/year, city, ZIP code, state, and an email address for a confirmation link. The page says nothing is removed until that link is clicked, requests are acknowledged within 10 business days and completed within 45 calendar days, and phone requests go to (855) 754-7951. No CAPTCHA widget or CAPTCHA script was present on either form when rendered, so the entry is marked assisted. A CAPTCHA could still appear on submit, which was not tested. Nothing was submitted, and last_verified is null."
---

1. Go to https://www.checksecrets.com/api/helper/optOutLight/search. It is also linked as "Do Not Sell Or Share My Personal Info" in the site footer.
2. Choose "Remove My Information". The other option, "Your Privacy Choices", only stops sale/sharing and leaves your listing on the site.
3. Fill in the details of the person in the listing: first and last name, full birth date, city, ZIP code and state.
4. Enter an email address for the confirmation link, then click "Submit removal request".
5. Open the confirmation email and click the link. Nothing is removed until you do.
6. CheckSecrets says it acknowledges requests within 10 business days and completes them within 45 days. After that, search the site again to check.
7. If the link never arrives, or you'd rather not use the form, call (855) 754-7951.
