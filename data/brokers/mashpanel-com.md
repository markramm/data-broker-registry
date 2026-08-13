---
id: mashpanel-com
name: MashPanel
domain: mashpanel.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.mashpanel.com/remove-listings/"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [listing_url]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Live curl confirms mashpanel.com is a real people-search directory built on the 'Listingpro' WordPress theme (copyright footer dated 2016), running an 'About Us' page that states verbatim: 'Mashpanel.com is a people search portal which displays publicly available information on individuals and companies... locate your profile on the web-site and click on the removal request link.' Its 'Remove listings' page (mashpanel.com/remove-listings/) explains every listing has a per-record 'Delete' button that removes it immediately -- there is no centralized bulk opt-out form, email, or CAPTCHA; the user must find their own listing first. Site also has a public 'Add listing' feature, consistent with a small/independent aggregator rather than a major broker. No email or phone contact for opt-out was found beyond the per-listing delete mechanism, so opt_out_email is null despite this being method:form. Classified crucial priority as a live people-search site with real personal-safety stakes; guided tier because the process requires locating the specific listing rather than a simple form submission."
---

1. Go to mashpanel.com and use the search bar to look up your own name (or the name of the person whose listing needs removing).
2. Open the specific profile/listing page that matches -- note its exact URL.
3. On that listing page, look for and click the "Delete" button described on the site's Remove Listings page (https://www.mashpanel.com/remove-listings/); per the site, this removes the record immediately.
4. If no Delete button is visible on the listing, use the site's Contact Us page (https://www.mashpanel.com/contact-us/) to request manual removal, including the exact listing URL.
5. Repeat for any additional profiles that match your name, since the site allows anyone to add new listings and old ones can resurface under slightly different details.
