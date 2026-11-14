---
id: usa-people-search-com
name: usa-people-search.com
domain: usa-people-search.com
category: personal_information
people_search: false
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.usa-people-search.com/manage"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: ["full_name", "email", "other"]
readd_days: null
legal_basis: []
last_verified: null
source: data-brokers-watch
notes: "Updated 2026-10-30 by the daily maintainer after page-monitor #150. Fetched https://www.usa-people-search.com/manage (WebFetch, HTTP 200; the monitor snapshot shows the same text). The opt-out is now a two-stage email-link flow, not the old search -> View Details -> Remove Record flow: the first page ('USA People Search Opt-Out Form') asks whether you are the subject or an authorized agent, then first name, optional middle name, last name and email, and says to 'complete the captcha below' before 'Begin Removal Process'. USA People Search then emails a link to the opt-out form (it expires after 24 hours); that form asks for details matching the record and leads to a confirmation page and email, with up to 3 days to process. The second-stage form sits behind the emailed link and was not seen, so its exact fields are recorded as 'other'. The CAPTCHA widget itself did not appear in the fetched text, but the page instructs users to solve one, so captcha stays true and tier guided. Earlier history: the original opt_out_url (help.aspx#p3) 403'd and was replaced with /manage on third-party removal-guide consensus. Treated as crucial (people-search/address reseller) despite the migrated people_search:false flag. Nothing was submitted; last_verified null."
---

1. Go to https://www.usa-people-search.com/manage.
2. Choose whether you are the person in the record or an authorized agent, then enter your first and last name (middle name optional) and your email address.
3. Solve the CAPTCHA and click "Begin Removal Process".
4. Open the email USA People Search sends and click its link within 24 hours. If you wait longer, request a new link.
5. On the opt-out form the link opens, enter your details exactly as they appear on the record you want removed. Leaving fields out or getting them wrong can stop the record being matched.
6. You'll get a confirmation page and a confirmation email. Allow up to 3 days for the record to be removed.
