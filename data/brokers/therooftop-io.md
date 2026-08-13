---
id: therooftop-io
name: "Rooftop Media"
domain: therooftop.io
category: marketing_data_broker
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://www.rooftopmedia.ai/data-privacy.html"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: "2026-08-13"
source: "dbw+tcp-research"
notes: "therooftop.io (and www.therooftop.io) 302-redirects to www.rooftopmedia.ai -- same operator, current brand name. Fetched and curled the live rooftopmedia.ai homepage and data-privacy.html directly: Rooftop Media is an AI-powered customer-acquisition/lead-gen platform describing '300M+ consumer profiles enriched with live signals' and '1.4B+ Data Signals' used to target consumers for insurance/mortgage/financial-services advertisers. Its own privacy-policy.html (curled directly) states in section 9 that it may receive 'affiliate fee, commission payment, lead delivery compensation, and monetization tied to audience matching' that 'may qualify as sales of personal data depending on jurisdiction,' lists categories sold/shared (identifiers, device data, commercial information, online activity, inferences), and references CCPA/CPRA rights including 'Do Not Sell My Personal Information.' In scope as a marketing data broker, not a people-search site. The data-privacy.html Consumer State Rights Request form was fetched raw (curl) and inspected directly: no CAPTCHA markup present, JS-submitted (fetch()), fields are requester_type (radio: Consumer/Agent), first_name, last_name, email, state (dropdown, all 50 states + DC + PR), and an action dropdown including 'Right to opt-out of sharing or sale of my personal information.' No ID, SSN, or phone required. Contact email privacy@rooftopmedia.ai confirmed present in the curled privacy-policy.html. Because the form has no CAPTCHA and only 4 simple fields, classified tier:assisted rather than guided. last_verified set to today because I directly curled and read the exact live page content (not just a search-engine-summarized writeup)."
---

<!-- Real instructions based on Rooftop Media's own Consumer State Rights Request form, fetched directly. -->
1. Go to https://www.rooftopmedia.ai/data-privacy.html (therooftop.io redirects here -- Rooftop Media is the current operating brand).
2. Select "Consumer" for requester type.
3. From the "Please select the action desired" dropdown, choose "Right to opt-out of sharing or sale of my personal information" (or "Right to delete my personal information" if you want full deletion instead).
4. Enter your first name, last name, email address, and select your state of residence.
5. Click "Submit Request."
6. If you prefer email, you can instead write to privacy@rooftopmedia.ai stating you are a California (or other applicable state) consumer requesting to opt out of the sale/sharing of your personal information under CCPA/CPRA.
7. Rooftop Media's privacy policy references standard state-law response windows (up to 45 days, extendable to 90) -- if you don't hear back within that window, follow up by email.
