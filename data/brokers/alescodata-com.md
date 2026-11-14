---
id: alescodata-com
name: "The Alesco Group LLC"
domain: alescodata.com
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://unsubscribe.stirista.com/"
opt_out_email: "privacy@stirista.com"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: ["ccpa"]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on alescodata.com/opt-out-request/ confirmed a self-serve form asking for name, address, email, and phone, with a confirmation checkbox and no CAPTCHA visible; page states Alesco may contact the requester to confirm identity before processing. Email opt-out via privacy@alescodata.com also confirmed (legacy CSV email michael@alescodata.com was not confirmed as current and is not used). Alesco Data builds mailing-list and audience databases from public records/assessor files -- a marketing data aggregator, not people-search, hence priority high not crucial. Did not verify against a freshly rendered page beyond this fetch, so last_verified left null. Updated 2026-11-03 by the daily maintainer after page-monitor #171: alescodata.com/opt-out-request/ now redirects to /privacy-center/, which no longer shows a form and says Alesco Data is now a Stirista company, that privacy preferences and data subject access requests are now handled through stirista.com, that Stirista will honor requests made to Alesco before 7/1/2026, and then redirects to stirista.com. The footer reads 'Alesco Data, A Stirista Solution'. Routing therefore moved to Stirista's portal at unsubscribe.stirista.com (rendered headless, HTTP 200). It has an email-only removal section, a postal section (first name, last name, address, city, region, country, postal code), a mobile-ID section and a sale/sharing inquiry section, all behind a visible reCAPTCHA v2 checkbox (captcha true, tier guided). The old Alesco phone line (877) 652-5002 was not re-confirmed, so phone is now null; privacy@stirista.com is listed on the portal. Nothing was submitted."
---

1. Alesco Data is now part of Stirista, and its old opt-out form is gone. Its privacy page says requests now go through Stirista, so use [Stirista's opt-out portal](https://unsubscribe.stirista.com/).
2. In the first section ("Do you wish to remove your data profile from our consumer records?"), enter your email address, complete the CAPTCHA and submit.
3. Alesco's records are mostly postal, so also fill in the "No email? No problem!" section with your first and last name, mailing address, city, region/country and postal code, and submit that too. Submit once for each address you have lived at.
4. Stirista says a deletion and an opt-out have the same effect: it deletes the matching records from its active databases and adds you to its suppression list.
5. Or email privacy@stirista.com and ask Stirista, as the owner of Alesco Data, to delete your data and stop selling or sharing it. Requests already sent to Alesco before 7/1/2026 will still be honored, according to the notice on Alesco's site.
