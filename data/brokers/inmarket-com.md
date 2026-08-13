---
id: inmarket-com
name: "InMarket Media LLC"
domain: inmarket.com
category: location_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://preferences.inmarket.com/form/opt_out"
opt_out_email: "privacy@inmarket.com"
phone: "1-877-782-0530"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on inmarket.com/privacy/ confirms InMarket is a location-data and advertising broker: it collects 'precise geolocation information' and discloses personal information to third-party advertisers/agencies; certain state laws (CCPA/CPRA) classify this targeted-advertising sharing as a 'sale.' Footer link-scrape of inmarket.com found the exact opt-out URL: https://preferences.inmarket.com/form/opt_out ('Do Not Sell or Share My Personal Information' and 'Limit the Use of My Sensitive Personal Information' both point to this same form). WebFetch on that URL only returned a bare page title ('Privacy Request Center | DataGrail') -- it's a JS-rendered DataGrail-hosted privacy-request form, so exact fields/CAPTCHA could not be confirmed; DataGrail forms are typically email-based with no CAPTCHA but this was not independently verified for this instance, so tier is guided (uncertain gating) rather than assisted. Phone (1-877-782-0530) and Global Privacy Control support are also offered as alternatives per the privacy policy. people_search is false -- this is a location/ad-tech data broker, not a consumer-facing name lookup site -- priority set to high (real location-tracking privacy stakes, working documented opt-out) per instructions rather than crucial. last_verified left null since the actual form page could not be rendered."
---

1. Go to InMarket's privacy request form at https://preferences.inmarket.com/form/opt_out (also linked from the "Do Not Sell or Share My Personal Information" and "Limit the Use of My Sensitive Personal Information" links in the footer of inmarket.com).
2. Follow the form's prompts to submit a request to opt out of the sale/sharing of your personal information and to limit use of sensitive personal information (this is a hosted DataGrail privacy-request form).
3. If you'd rather not use the web form, email privacy@inmarket.com directly and state that you are exercising your CCPA right to opt out of the sale/sharing of your personal information (include your name and any relevant device/advertising identifiers if you have them).
4. Alternatively, call InMarket at 1-877-782-0530 to make the same request by phone.
5. If your browser or a browser extension supports Global Privacy Control (GPC), enabling it will automatically signal your opt-out preference to InMarket going forward.
6. Note that InMarket applies opt-outs per browser/device, so repeat this process on each device or browser you use if you want full coverage.
