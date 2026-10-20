---
id: persopo-com
name: Persopo
domain: persopo.com
category: people_search
people_search: true
tier: auto
priority: crucial
method: email
opt_out_url: "https://persopo.com/opt-out.html"
opt_out_email: support@persopo.com
phone: 1-800-481-9168
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, full_name]
readd_days: null
legal_basis: []
last_verified: 2026-07-03
source: "data-brokers-watch + tcp-verified"
notes: "MIGRATED research_note: own opt-out page live. Confirmed via direct WebFetch of opt-out.html: no online form -- process is to copy your listing as plain text (name, age, location, relatives shown) and email it to support@persopo.com (subject 'Opt Out' or 'Attention: Opt Out Dept.'), or mail it to their Las Vegas address. No CAPTCHA, ID, or fee. Because the channel is email, tier set to auto per schema. Removal takes 10-20 business days; Persopo also adds your info to a suppression list shared with its data providers to reduce future re-listing. 2026-10-19 (maintainer, Refs tester report #5 by @matthew-product): a tester who emailed the opt-out was told Persopo 'no longer has any public records', holds data only on paying customers, and that results reached from persopo.com come from TruthFinder, which must be asked separately. Fetched 2026-10-19: persopo.com and opt-out.html both load (HTTP 200); opt-out.html still describes the copy-your-listing email process unchanged, and the homepage's search links out to a tracking.truthfinder.com affiliate URL, consistent with the reply. Added a TruthFinder step; email route and last_verified unchanged (not re-walked)."
---

1. Search for yourself on persopo.com and find your listing.
2. Copy the entire listing as plain text (name, age, location, relatives) -- do not send a screenshot or just a link.
3. Email the copied listing to support@persopo.com with a subject like "Opt Out" or "Attention: Opt Out Dept."
4. Alternatively, mail the same information to: Persopo.com, Attention: Opt Out Dept., 848 N. Rainbow Blvd., Suite 20, Las Vegas, NV 89107.
5. Allow 10-20 business days for removal. Persopo says it shares a suppression list with its data providers, but new records with different identifiers can still appear later.
6. Persopo's search sends you to TruthFinder, and Persopo has told at least one requester it keeps no public-record data itself and that TruthFinder results must be removed with TruthFinder. Also complete the TruthFinder opt-out (see the truthfinder-com entry).
