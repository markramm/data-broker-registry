---
id: achcoop-com
name: "ACH, Address Clearing House"
domain: achcoop.com
category: postal_data
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.achcoop.com/do-not-sell-my-personal-info"
opt_out_email: "Privacy@achcoop.com"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [full_name, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-10-23 by the daily maintainer from California's data broker registry (ACH, Address Clearing House; registry rights URL https://www.achcoop.com/). The homepage (HTTP 200) is a small Wix site. It gives Privacy@achcoop.com for privacy questions and links a 'DNSMPI' opt-out page. The site doesn't describe the business beyond its name (the About link returned 404); the page says it 'only process[es] U.S. postal data', so it is classed as a postal/address data broker rather than a people-search site, at high priority. https://www.achcoop.com/do-not-sell-my-personal-info, loaded in a headless browser, adds a name and address to ACH's 'no sale' list. It requires first and last name, street address (Apt/Unit only if it applies), city, state and ZIP, and checkboxes for: Do Not Sell, Remove Me From Your Database, Access, Correct, Do Not Share, opt out of targeted advertising, and opt out of profiling. The page says a full address is required, one name/address per submission. A Wix CAPTCHA widget sits on the form, so captcha is true and the tier is guided. No confirmation step is described. Nothing was submitted; last_verified is null."
---

1. Go to https://www.achcoop.com/do-not-sell-my-personal-info (the "DNSMPI" link in the site menu).
2. Enter your first and last name and your full mailing address: street, Apt/Unit only if you have one, city, state and ZIP. Requests without a full address aren't processed.
3. Under "Select your request", tick "Do Not Sell My Personal Information", "Remove Me From Your Database" and "Do Not Share My Personal Information". Add the targeted-advertising and profiling opt-outs if you want them.
4. Complete the CAPTCHA and submit.
5. The form takes one name and address per submission, so submit again for every other address you've lived at or other household member.
6. No confirmation step is described. If you want one, or have questions, email Privacy@achcoop.com.
