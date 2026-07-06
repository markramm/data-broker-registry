---
id: peoplesearchpro-com
name: "People Search"
domain: peoplesearchpro.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "http://www.peoplesearchpro.com/PSP.aspx?_act=optout"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, full_name]
readd_days: null
legal_basis: []
last_verified: null
source: data-brokers-watch
notes: "Direct fetch returned 403; WebSearch did not surface peoplesearchpro.com-specific opt-out guides (only similarly-named sites like PeopleSearch.com/Whitepages). Corrected category/people_search to reflect this is in fact a people-search site (domain and page title 'People Search' make this unambiguous, despite the earlier data_brokers/false migration tag). The PSP.aspx?_act=optout URL pattern matches the same legacy Intelius-family template used by phonedetective.com's PD.aspx?_act=OptOut, which per other research typically requires locating your own listing and a CAPTCHA-gated submission. Assessed conservatively as guided/captcha:true by analogy to that shared template; NOT independently confirmed for this exact domain. last_verified left null -- flagging this entry for a follow-up manual check."
---

1. Go to peoplesearchpro.com and search for your own name to locate your listing.
2. Copy the listing URL or note identifying details (name, age, city/state) from the record.
3. Go to the opt-out page at peoplesearchpro.com/PSP.aspx?_act=optout.
4. Enter the requested identifying details for the listing you want removed.
5. Complete the CAPTCHA if one is presented and submit the request.
6. This entry is based on the shared template this site appears to run (same as other Intelius-family lookup sites) rather than a fresh direct confirmation -- if the form differs from these steps, treat that as the authoritative version and let the maintainers know.
