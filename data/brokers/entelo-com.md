---
id: entelo-com
name: "Entelo, Inc. (now Rival)"
domain: entelo.com
category: hr_talent_data
people_search: false
tier: assisted
priority: standard
method: email
opt_out_url: "<verify: entelo.com now redirects to rival-hr.com/entelo-recruit/ -- confirm current CCPA opt-out page/form, since privacy@rival-hr.com is a general privacy contact, not a dedicated opt-out form URL>"
opt_out_email: "privacy@rival-hr.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "entelo.com redirects (301) to https://rival-hr.com/entelo-recruit/, which confirms 'Entelo and ConveyIQ are now part of Rival' -- Entelo was acquired and folded into Rival, an HR/recruiting-orchestration SaaS company (sourcing, candidate engagement, employee journeys). This is a B2B recruiting/talent-sourcing data aggregator (aggregates candidate profiles from public professional sources), not a consumer people-search site, so people_search is false and category is hr_talent_data (matching this repo's existing convention). Fetched rival-hr.com/privacy-policy/ directly: it discloses CCPA applicability but does NOT provide a dedicated 'Do Not Sell My Personal Information' web form or opt-out-specific email -- instead it gives a general privacy contact: privacy@rival-hr.com (and a mailing address: Rival Technology, C/O Security Department, 311 W. Monroe Street, Suite 402, Chicago, IL 60606). Marketing-email opt-out is separately available via unsubscribe links in Rival's own marketing emails, but that's a different, narrower mechanism than a CCPA data-sale opt-out. Because opt_out_email is a real, live, non-placeholder address, method is set to email/tier auto-eligible per the schema rule, but I'm holding tier at assisted and flagging the URL as needing verification: it's unclear whether Rival has a dedicated CCPA request portal elsewhere on rival-hr.com that a general fetch didn't surface, so opt_out_url is a <verify:> placeholder and last_verified is null. priority standard: legitimate opt-out channel exists but this is a B2B recruiting tool with lower direct personal-safety stakes than a people-search site."
---

1. Entelo has been folded into Rival (rival-hr.com); entelo.com now redirects to https://rival-hr.com/entelo-recruit/, so opt-out requests should go through Rival's privacy channel rather than a legacy Entelo page.
2. Email privacy@rival-hr.com with a clear subject line such as "CCPA Opt-Out / Do Not Sell My Personal Information," and include your full name and any identifying details (e.g., professional profile URL) that will help Rival locate your candidate record.
3. If you'd rather send a written request by mail, address it to: Rival Technology, C/O: Security Department, 311 W. Monroe Street, Suite 402, Chicago, IL 60606, USA.
4. If you only want to stop marketing emails specifically (a narrower request than a full data-sale opt-out), you can instead use the "Unsubscribe" or "opt out" link included in any marketing email Rival/Entelo sends you.
5. Before relying on this entry, check Rival's current privacy policy at rival-hr.com/privacy-policy/ for a possibly more specific CCPA request form -- none was found during this research pass, but Rival's site structure may have a dedicated portal not surfaced by a general fetch.
