---
id: freepeopledirectory-com
name: Free People Directory
domain: freepeopledirectory.com
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://www.freepeopledirectory.com/optout"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url]
verification: none
readd_days: null
legal_basis: [none]
last_verified: null
source: "dbw+tcp-research"
notes: "Not in the source CSV, discovered/confirmed independently. FreePeopleDirectory is a live people-search site (name/phone/address lookup) that aggregates public-records data; page source (window.Spokeo object, GTM container, schema.org markup) confirms it is a Spokeo-family/white-label property. Site's own /optout page was fetched directly and contains a real, simple form: a single 'url' text input labeled 'Enter the profile URL you wish to remove' plus a submit button -- no CAPTCHA markup found in the static HTML (JS-rendered CAPTCHA can't be ruled out, so treated cautiously). The privacy policy page (/privacy) does not mention CCPA 'do not sell' language directly but links out to Spokeo's own privacy control page (spokeo.com/privacy/control/) as a secondary/broader removal path. Because the site's own opt-out is a single-field form with no login, CAPTCHA, or ID gate detected, this is classified assisted rather than guided. legal_basis set to none because no explicit statutory basis was found in the fetched text (site is federal-public-records-based, FCRA-exempt disclaimer present)."
---

1. Search your name on freepeopledirectory.com and open the profile listing that matches you; copy that profile's full URL.
2. Go to https://www.freepeopledirectory.com/optout.
3. Paste the profile URL into the "Enter the profile URL you wish to remove" field and click Submit.
4. Repeat separately for each distinct matching profile, since removing one listing does not remove others.
5. Note that FreePeopleDirectory aggregates from third-party public-record sources -- removing the listing here will not remove the underlying data from its original source, so it may reappear elsewhere or resurface after a data refresh.
6. As a broader option, this site appears to be part of the Spokeo family; you can also submit a removal through Spokeo's own privacy control page at https://www.spokeo.com/privacy/control/, which may cover related properties.
7. Re-check periodically, since public-records aggregators commonly re-add listings on their normal refresh cycle.
