---
id: ididata-com
name: "Interactive Data, LLC"
domain: ididata.com
category: identity_intelligence_data_broker
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.ididata.com/do-not-sell-my-personal-information/"
opt_out_email: "statebasedprivacy@ididata.com"
phone: "888-376-6659"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [full_name, email, address]
readd_days: null
legal_basis: [ccpa, cpra, vcdpa, cdpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on ididata.com/idis-privacy-statement/ confirmed IDI (Interactive Data) compiles identity-intelligence products (idiCORE, coreIDENTITY, idiVERIFIED) pulling from 'credit bureaus, government and public record repositories... data aggregators, brokers, compilers, marketing companies, third-party resellers' and sells access to investigators, law enforcement, financial services, and real estate -- a genuine people-search/identity-lookup broker on individuals, so people_search true and priority crucial. Confirmed separate dedicated pages for do-not-sell (https://www.ididata.com/do-not-sell-my-personal-information/), deletion, correction, and personal-information-request, plus a dedicated privacy email (statebasedprivacy@ididata.com) and phone (888-376-6659) covering CA, VA, CO, CT, UT, OR, TX, MT, IA, DE, NE, NH, NJ, TN, MN, MD, IN, KY, and RI residents. Could not confirm exact form fields/CAPTCHA on the do-not-sell page itself via fetch (only the privacy-statement page rendered), so listed plausible required fields based on the industry-standard identity-verification pattern for opt-out requests and left tier assisted rather than guided since no ID/CAPTCHA was reported; note this is a lower-confidence field guess and should be double-checked against the live form. 2026-10-14 maintainer: fetched https://www.ididata.com/do-not-sell-my-personal-information/ (HTTP 200); the form carries a visible reCAPTCHA v2 widget (div.g-recaptcha with a site key, no invisible size), confirming the page monitor's flag. captcha set true and tier moved assisted -> guided per CONTRIBUTING (CAPTCHA-gated). The email and phone routes in the steps are unaffected. last_verified unchanged."
---

1. Go to the [IDI do-not-sell page](https://www.ididata.com/do-not-sell-my-personal-information/) and follow the opt-out request form.
2. Provide your full name, email address, and mailing address as prompted so IDI can locate your record.
3. Submit the request; alternatively, email statebasedprivacy@ididata.com directly and state you are requesting IDI stop selling/sharing your personal information under applicable state privacy law (CCPA/CPRA or your state's equivalent).
4. You can also call 888-376-6659 to make the same request by phone.
5. If you also want your existing record corrected or deleted, use IDI's separate correction request (https://www.ididata.com/correction-request/) or deletion request (https://www.ididata.com/deletion-request/) pages.
6. Watch for a confirmation email and follow any verification link IDI sends before the request is finalized.
