---
id: peoplefindersdaas-com
name: PeoplefindersDaaS
domain: peoplefindersdaas.com
category: people_search
people_search: true
tier: auto
priority: crucial
method: email
opt_out_url: "https://peoplefindersdaas.com/personal-information/"
opt_out_email: "privacy@peoplefindersdaas.com"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, phone, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "PeoplefindersDaaS (\"Data as a Service\") is the bulk/API data-supply arm of PeopleFinders -- it sells consumer identity, address, and contact records to B2B customers (marketing, verification, people-search resellers) rather than running its own consumer-facing search UI, but it is still a genuine people-search-adjacent data broker with real personal-safety stakes since the underlying records are the same individual profiles. 2026-09-15: fetched https://peoplefindersdaas.com/personal-information/ directly (HTTP 200) and read the rendered form, replacing instructions that previously only said to 'follow the instructions there' -- a step a tester cannot check the tool against. The page is a real request form, not a policy page: it collects Name (First/Last), Email, Phone, Address Line 1/2, City, State, Zip, and offers four separate opt-out checkboxes (do not sell/share; no targeted/cross-contextual advertising; no profiling/automated decision-making; no sensitive-data targeting) plus a distinct 'Please delete my personal information' option. The page states that a delete request causes them to create an archival record of the request, and directs anyone wanting to stay out of the database in future to email privacy@peoplefindersdaas.com. required_fields widened from [full_name, email] to include phone and address, since the form asks for both. tier stays auto: the email route is a complete opt-out path on its own with no login, CAPTCHA, or ID gating, which is what auto means in this repo -- the form is an additional convenience, not a barrier. The privacy policy discloses PeoplefindersDaaS's own 2025 CCPA transparency stats: of 15,678 California removal requests received, only 77 were completed, the vast majority denied for 'insufficient information or bot detection' -- a real but friction-heavy process, and a number worth telling the reader so a denial does not read as the end of the road. last_verified stays null: fetching and reading the form is not the same as a human submitting a request and confirming their record came down. This is a distinct entity from consumer-facing peoplefinders.com (cataloged separately) -- separate opt-out infrastructure, so kept as its own entry rather than merged. 2026-10-14 maintainer: fetched https://peoplefindersdaas.com/personal-information/ (HTTP 200); the WPForms request form now embeds a Cloudflare Turnstile challenge (div.wpforms-turnstile with a site key), confirming the page monitor's flag, so captcha is set true for the form. tier stays auto: the privacy@ email route is still a complete opt-out with no CAPTCHA. last_verified unchanged."
---

1. Go to https://peoplefindersdaas.com/personal-information/ -- this is a real request form, not a policy page, so the whole request can be made here.
2. Fill in your name and email (both required), plus your phone and address. The address fields matter: this broker sells address and contact records, so identifying yourself completely makes it likelier they find your record.
3. Tick the boxes for what you want stopped. They are separate choices and ticking one leaves the others running: do not sell/share my personal information; do not use my personal data for targeted or cross-contextual advertising; do not use my personal data for profiling or automated decision-making; do not use my sensitive personal data for targeting. For a full opt-out, tick all four.
4. There is a separate "Please delete my personal information" option. Tick it if you want deletion rather than suppression -- but note the page says that when they receive a delete request they create an archival record of it, so this does not mean every trace is gone.
5. Submit the form. If you would rather use email, or you want to ask them to keep you out of the database in future rather than only remove you today, email privacy@peoplefindersdaas.com with the same details, stating that you are exercising your CCPA (or your state's equivalent) right to opt out and delete.
6. Expect a response within 45 days; their own disclosures note this may be extended to 90 for complex requests.
7. Be persistent. PeoplefindersDaaS's own 2025 CCPA transparency report says it received 15,678 California removal requests and completed 77, denying most for "insufficient information or bot detection." If you are denied, resend with fuller identifying details rather than assuming the opt-out is closed to you.
8. Because this is the data-supply arm behind other people-search sites, submit the separate opt-out for peoplefinders.com too -- the two do not share a single suppression list.
