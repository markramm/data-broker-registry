---
id: leadiq-com
name: LeadIQ, Inc
domain: leadiq.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: standard
method: portal
opt_out_url: "https://leadiq.com/request-removal"
opt_out_email: "privacy@leadiq.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on leadiq.com's privacy policy confirmed: B2B sales-prospecting data broker maintaining a 'Directory Database' of professional contact info for sales and recruiting use. Policy directs removal requests to a dedicated Privacy Center at privacy.leadiq.com or via email to privacy@leadiq.com, and the footer carries a 'Do Not Sell or Share My Personal Information' link. Attempting to fetch privacy.leadiq.com itself returned only the marketing homepage content in this session (not the actual portal form), so the portal's exact fields/CAPTCHA status is inferred from the privacy policy's general language ('we may ask you to verify your identity') rather than directly observed -- no CAPTCHA or ID upload is mentioned anywhere, so kept at assisted rather than guided. B2B professional-contact data, not consumer people-search; priority standard. last_verified left null since the portal page itself wasn't directly rendered. Update 2026-11-14 (daily maintainer, refs page-monitor #225): privacy.leadiq.com still serves only the marketing homepage (title 'LeadIQ | The Smart B2B Prospecting Platform', no request form); that homepage's 'Privacy Center' and 'Do Not Sell or Share My Personal Information' links both go to leadiq.com/privacy-center, a hub offering 'Claim my profile', 'Request access' and 'Request removal' (/request-removal). Fetched leadiq.com/request-removal ('LeadIQ | Request Removal'): it embeds a Typeform titled 'LeadIQ Privacy Portal' whose first step is 'Let's start by verifying your email address' -- no CAPTCHA seen on that first step. Later Typeform steps were not walked (nothing was submitted). opt_out_url moved to /request-removal. Privacy Center also lists phone 1-888-653-2347 and says opting out of ad sharing is done via the site cookie manager. last_verified left null."
---

1. Go to https://leadiq.com/request-removal (reachable from LeadIQ's Privacy Center at https://leadiq.com/privacy-center via "Request removal").
2. The page embeds LeadIQ's Privacy Portal form. It starts by verifying your email address -- use the work email LeadIQ is likely to have on file for you.
3. Follow the remaining steps to request removal of your professional contact record from LeadIQ's database.
4. If the form doesn't work or you prefer email, write to privacy@leadiq.com with "Privacy Request" in the subject line, your name, and the details of the record (e.g. company, job title) you want removed.
5. Watch for a confirmation email once the removal is processed. To also stop ad-related sharing on LeadIQ's own site, turn off "Marketing cookies" in its cookie manager.
