---
id: i-360-com
name: "i360, LLC"
domain: i-360.com
category: political_voter_data_broker
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.i-360.com/ccpa/"
opt_out_email: null
phone: "1-844-611-2737"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: identity_check
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on i-360.com/privacy-policy/ confirmed the site's own text: 'The entity maintaining this website is a data broker under Texas law.' i360 is a large political/voter and consumer data broker (donor and voter file, modeling, analytics for conservative political and commercial clients) -- high personal-safety and civic-privacy stakes given the sensitivity of voter/political profiling, so marked crucial and people_search true (it resells individual-level voter/consumer records, not just aggregate models). WebFetch on i-360.com/ccpa/ confirmed the opt-out path: a 'Do Not Sell or Share My Personal Information' link and Global Privacy Control support, routing to a OneTrust webform (https://privacyportal.onetrust.com/webform/94afa614-d9cb-419b-99f1-20c87afaca7f/50cf2c4e-695f-4acc-b64f-7f62bb32d92d). Used the i-360.com/ccpa/ landing page as opt_out_url rather than the OneTrust URL directly since that is the broker's own canonical page and the OneTrust form is JS-rendered (could not confirm its exact fields/CAPTCHA via fetch). Page text states no CAPTCHA/ID verification is required specifically for opt-out requests (unlike other CCPA request types), so id_required/captcha left false, but tier kept guided given the third-party portal hop and the sensitivity of the data category. A phone alternative (1-844-611-2737) is listed on the same page."
---

1. Go to the [i360 CCPA notice](https://www.i-360.com/ccpa/).
2. Click the "Do Not Sell or Share My Personal Information" link (or enable Global Privacy Control in your browser beforehand, which i360 says it will honor automatically).
3. You'll be routed to i360's OneTrust privacy request form; enter your name and email address as prompted and submit.
4. If you prefer not to use the web form, you can instead call i360's privacy line at 1-844-611-2737 and request the same opt-out.
5. Note that this opt-out is tied to the browser/device you submit it from -- if you clear cookies or switch devices/browsers, i360 states you may need to resubmit the request.
6. Repeat periodically, since voter/consumer files like i360's are re-compiled from new source data on an ongoing basis.
