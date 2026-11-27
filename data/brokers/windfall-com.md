---
id: windfall-com
name: "Windfall (Windfall Data, Inc.)"
domain: windfall.com
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.windfall.com/your-privacy-choices"
opt_out_email: "privacy@windfall.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [full_name, address, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-11-27 by the daily maintainer from California's data broker registry (Windfall Data, Inc.; registry rights_url https://www.windfall.com/your-privacy-choices; registry email privacy@windfall.com). Windfall sells wealth and net-worth intelligence about individual people (wealth screening, enrichment, propensity models) to nonprofits, retailers, financial services and others. It is not a public people-search site, so people_search is false and priority is high. Fetched the Your Privacy Choices page (HTTP 200, also rendered headless). It says Windfall's database is organized by name and address, so an opt-out of sale needs first and last name plus current address, and an email for status updates. It also says the opt-out covers only Windfall's own databases, not its customers' copies. It says the opt-out form is 'below', but no such form showed up in the static HTML or the headless render; only a blog-subscribe email box appeared. Access, correct, delete and authorized-agent requests go through an 'Exercise Privacy Rights' button linking to an Osano portal (my.datasubject.com). Loaded headless, that portal auto-detected the US as the location and said privacy rights were not supported there. It has a location picker at the top right, but choosing a state could not be scripted. The page says access requests need a phone number that matches Windfall's records. Its 2025 metrics show 202 opt-out and 751 deletion requests, all complied with, median about one day. A CAPTCHA could not be confirmed either way (the page HTML mentions a CAPTCHA library, but no widget rendered), so captcha stays false. Tier is guided because the form did not render and the portal needs a state chosen by hand. opt_out_email is the privacy contact from the CA registry filing, not shown on the fetched page. Nothing was submitted; last_verified is null."
---

1. Go to https://www.windfall.com/your-privacy-choices.
2. Use the opt-out-of-sale form on that page. Give your first and last name, your current address, and an email address. Windfall's records are matched by name and address, so both are needed.
3. If the form doesn't show up, click "Exercise Privacy Rights" at the bottom of the page. In the portal that opens, use the location selector at the top right to choose your state (for example, United States → California) before filling in the request.
4. To have your record deleted rather than only withheld from sale, choose a deletion request in that portal. Windfall may ask for a phone number that matches its records to verify you.
5. If neither works, email privacy@windfall.com. Ask to opt out of the sale of your personal information and to have it deleted, and include your full name and current address.
6. Windfall reports handling most opt-out and deletion requests within a day or two. The opt-out covers only Windfall's own databases, not copies its customers already hold.
