---
id: peoplesearcher-com
name: "PeopleSearcher"
domain: peoplesearcher.com
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://www.peoplesearcher.com/api/helper/optOutLight/search"
opt_out_email: "support@peoplesearcher.com"
phone: "1-833-634-0750"
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
notes: "Authored 2026-10-17 by the daily maintainer from California's data broker registry (The People Searchers LLC, support@peoplesearcher.com; the registry's rights_url is a typo, 'peopesearcher.cm', and also lists secretinfo.org, which was not fetched). The site is a JavaScript app (a plain fetch returns an empty shell), so pages were rendered in a headless browser. The footer link 'Limit The Use of My Sensitive Personal Info' leads to https://www.peoplesearcher.com/api/helper/optOutLight/search ('Privacy Requests', HTTP 200), which offers two separate requests. 'Your Privacy Choices' only stops sale/sharing, takes an email or phone, and explicitly does not remove a listing. 'Remove My Information' (?type=removal) requires first and last name, birth month/day/year, city, ZIP, state and an email for a confirmation link; nothing is removed until the link is clicked. The page says requests are acknowledged within 10 business days and completed within 45 calendar days, removal also covers reports members already hold and future matching records, agents must attach signed permission, and GPC is honoured for sale/sharing. No CAPTCHA widget was present on either form when rendered, so assisted; one may still appear on submit, which was not tested. People-search site -> people_search true, priority crucial. Nothing was submitted; last_verified null."
---

1. Go to https://www.peoplesearcher.com/api/helper/optOutLight/search (also reachable from the "Limit The Use of My Sensitive Personal Info" link in the site footer).
2. Choose "Remove My Information". The other option, "Your Privacy Choices", only stops sale/sharing and does not take your listing off the site.
3. Enter the first and last name, birth date (month, day, year), city, ZIP code and state of the person in the listing.
4. Enter an email address for the confirmation link, then click "Submit removal request".
5. Open the confirmation email and click the link. Nothing is removed until you do.
6. PeopleSearcher says it acknowledges requests within 10 business days and completes them within 45 days. Search the site again after that to check.
7. If the link never arrives or you'd rather not use the form, call (833) 634-0750.
