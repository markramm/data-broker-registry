---
id: newenglandfacts-com
name: NewEnglandFacts.com
domain: newenglandfacts.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "<verify: site is fully Cloudflare bot-blocked (403 on / and every path tried, including /optout, /ng/optout, /control/privacy); exact opt-out URL not directly confirmed, only inferred from third-party removal-guide summaries>"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "newenglandfacts.com is a people-search site that aggregates public records (addresses, phone numbers, ages, family/relative connections) despite the regional-sounding name -- it indexes all 50 states and is described by multiple independent removal-guide sources (BrandYourself, PrivacyOn, OneRep, MyDataRemoval, YourDigitalRights.org) as part of the same operator network as Radaris (radaris.com, already in this dataset). Direct fetch was fully blocked: every path attempted (/, /optout, /ng/optout, /control/privacy) returned Cloudflare 403. Because it could not be independently confirmed and is inferred entirely from third-party guide summaries rather than a directly rendered page, opt_out_url is a placeholder pending verification -- last_verified left null per schema rules for placeholder URLs. Given the Radaris-network association, assumed captcha:true and a similar find-profile -> paste-URL -> submit -> email-confirm flow to radaris.com's documented process, but this specific site's process was not independently rendered. people_search:true and priority:crucial given real personal-safety stakes (addresses, phone numbers, family relationships published)."
---

1. Search your name on newenglandfacts.com and locate the profile page that matches you; copy that profile's URL. (Verify the exact opt-out page yourself -- the site blocked automated fetches during this research, so the URL below could not be independently confirmed.)
2. Third-party removal guides describe an opt-out flow similar to the related site Radaris: locate a "Remove My Information" or opt-out link (often in the footer or on the profile page itself), paste in your profile URL, and provide an email address.
3. Solve any CAPTCHA the form presents, and submit the request.
4. Check your email for a confirmation message and click the confirmation link -- the opt-out is typically not final until confirmed.
5. Because this site shares infrastructure/operator with Radaris and similar sites, budget up to an hour for the full process including the email wait, and re-check periodically since these sites re-ingest public records.
