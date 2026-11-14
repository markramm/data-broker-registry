---
id: seekout-com
name: "SeekOut (ZipStorm, Inc.)"
domain: seekout.com
category: recruiting_data
people_search: true
tier: guided
priority: high
method: form
opt_out_url: "https://www.seekout.com/privacy/choices"
opt_out_email: "legal@seekout.com"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [full_name, email, listing_url]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Added 2026-11-14 by the daily maintainer from the California data broker registry (ZipStorm, Inc. dba SeekOut; registry email legal@seekout.com, rights URL seekout.com/privacy/choices). SeekOut is a recruiting/talent-sourcing platform; its site advertises searching '1B+ profiles', and its Candidate Privacy Policy says it collects names, contact info, work and education history and skills from public professional networking sites, personal websites and employer customers. Separately it runs a 'SeekOut Candidate Database' covered by its main privacy policy. SeekOut is also named as an upstream data vendor in our fetcher-ai entry. The 'Privacy Choices Portal' at /privacy/choices embeds a HubSpot form. Rendered headless (nothing submitted), it shows: individual / authorized-representative choice, first name*, last name*, email*, LinkedIn profile URL*, country*, state/region code*, and checkboxes for delete, copy, correction, Do Not Sell or Share, and limit sensitive PI, plus a reCAPTCHA. The page warns 'all requests for deletion are permanent'. CAPTCHA -> guided. Profiles of individuals searchable by recruiters -> people_search true; professional rather than home-address data, so high rather than crucial. The registry email was not seen on SeekOut's own pages. last_verified left null."
---

1. Copy the URL of your LinkedIn profile -- SeekOut's form requires it to find your record.
2. Go to https://www.seekout.com/privacy/choices (SeekOut's "Privacy Choices Portal").
3. Choose "I am the individual" and enter your first and last name, email, LinkedIn profile URL, country and state.
4. Tick "Delete My Personal Information" and "Do Not Sell or Share My Information". SeekOut warns that deletion is permanent.
5. Complete the CAPTCHA and submit, then watch for any follow-up email asking you to confirm.
6. If the form doesn't work, email legal@seekout.com (the address in SeekOut's California registry filing) with the same details.
