---
id: corelogic-com
name: CoreLogic (now Cotality)
domain: corelogic.com
category: real_estate_data
people_search: true
tier: guided
priority: high
method: portal
opt_out_url: "<verify: exact Cotality 'Online Privacy Portal' opt-out URL -- corelogic.com/privacy.aspx redirects to cotality.com/privacy.aspx, whose CCPA notice references an 'Online Privacy Portal' link that renders as a bare placeholder (#) in the fetched text>"
opt_out_email: null
phone: "866-221-9291"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: id_upload
required_fields: [full_name, address, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Legacy CSV listed corelogic.com twice (once under Teletrack LLC / Marketing Data Broker, once as a bare Credit Bureaus listing) -- authored as ONE entry per instructions. corelogic.com/privacy.aspx 301-redirects to cotality.com/privacy.aspx: CoreLogic rebranded to Cotality in 2024/2025. Confirmed via WebFetch + WebSearch this is a large property/real-estate data aggregator (mortgage, property records, tenant/renter screening inputs, valuation data) covering individual homeowners and renters -- genuine large-scale personal-data aggregator, so people_search true and priority high per instructions. Cotality's CCPA notice offers opt-out of sale/sharing via an 'Online Privacy Portal' (link rendered only as a placeholder anchor in the fetched HTML, so the concrete URL could not be confirmed -- left as a <verify:> placeholder, and last_verified is null as required whenever opt_out_url is a placeholder) or by phone at 1-866-221-9291; a separate email, datasubjectrequests@cotality.com, appeared in search-result summaries for broader data-subject requests but was not independently confirmed on a rendered page, so opt_out_email is left null rather than promoted to auto tier. Cotality's own policy states it asks requesters to 'verify data points based on information we have in our records,' which is a form of identity verification -- id_required set true on that basis. Cotality also states some CoreLogic/Cotality data (public records, GLBA/FCRA-covered data) may be exempt from CCPA deletion/opt-out rights, so full removal is not guaranteed even after a successful request."
---

1. Go to cotality.com (CoreLogic's current name) and look for "Do Not Sell or Share My Personal Information" in the site footer, which should lead to their CCPA "Online Privacy Portal."
2. If you cannot locate the portal link directly, call Cotality's California-resident privacy line at 1-866-221-9291 to submit your opt-out/deletion request by phone instead.
3. Be ready to verify your identity -- Cotality states it will ask you to confirm data points it already holds about you before processing the request.
4. Provide your full name, current and/or prior mailing address, and an email address so Cotality can match your record across its property and mortgage databases.
5. Note that Cotality states some data (public property records, and data covered by the Gramm-Leach-Bliley Act or Fair Credit Reporting Act, such as mortgage/credit-related records) may be exempt from CCPA opt-out and deletion rights -- full removal is not guaranteed even after a successful request.
6. If you manage rental applications and are trying to address tenant-screening data specifically, Cotality/CoreLogic's consumer-report disputes may need to go through their separate FCRA dispute process rather than the general CCPA portal.
