---
id: people-search-org
name: "People-Search.org"
domain: people-search.org
category: people_search
people_search: true
tier: guided
priority: crucial
method: portal
opt_out_url: "<verify: exact per-record removal-request mechanism -- confirm whether a global search/opt-out form also exists beyond the per-listing widget button>"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, full_name]
readd_days: null
legal_basis: [none]
last_verified: null
source: "dbw+tcp-research"
notes: "curl-fetched people-search.org's homepage and privacy-policy page directly (both HTTP 200, static HTML). It is a live, active people-search aggregator: 'People-Search.org gives you instant access to billions of public records collected from government agencies, courthouses, and official registries across all 50 states,' returning aliases, age, address history, phone numbers, and family members for a searched name -- real personal-safety-relevant exposure, so priority crucial. The privacy policy states removal is handled per-record: 'If you wish to have your information removed from our database, please press the removal request removal button on the record widget' -- i.e. you must first find your own listing via a name search, open your specific record, and click a removal button embedded in that record's display, rather than submit a name/email to a single global opt-out form or email address. This session could not locate or render an actual search-result record (would require searching a real name) to confirm the exact removal-button URL/flow, so opt_out_url is left as an unconfirmed placeholder and last_verified is null per instructions -- do not treat the domain homepage as the opt-out page. Also note the site's own FCRA disclaimer states it is not a consumer reporting agency and its data 'may not be 100% accurate.' No legal basis (CCPA etc.) is cited on the page itself, hence legal_basis: [none]."
---

1. Go to https://www.people-search.org and search your own full name (add city/state if you know it, to narrow results).
2. Open the search result record that matches you and look for a "removal request" (or similarly labeled) button embedded directly in that record's display -- this is the mechanism the site's own privacy policy describes; there does not appear to be a separate, standalone opt-out form or email address.
3. Follow whatever prompts that removal button presents (this may vary by record; confirm what it asks for before submitting personal information).
4. Repeat separately for any other matching listings under name variants, past addresses, or family-member cross-references, since aggregator sites like this often generate multiple separate records for the same person.
5. Because the removal path could not be independently confirmed end-to-end in this research pass, treat this as a starting point: if the "removal request" button doesn't appear or doesn't work, check the site's Privacy Policy or Terms & Conditions page for an updated process, and consider using a formal written CCPA/state-law request by mail if you're a resident of a state with an applicable data-broker law.
