---
id: outbrain-com
name: "Outbrain Inc."
domain: outbrain.com
category: adtech_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://dsr.outbrain.com/recommendations-settings/home"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [email]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "Outbrain is a large content-recommendation/native-advertising network ('interest-based ads' widgets across publisher sites) -- a genuine ad-tech data broker at meaningful scale, priority high. WebFetch on www.outbrain.com's homepage confirmed a footer link labeled 'Interest-Based Ads (Opt Out)' pointing to https://dsr.outbrain.com/recommendations-settings/home; that URL loads (title/branding 'Outbrain' returned) but is a client-rendered single-page app whose actual form fields/CAPTCHA could not be read via static fetch, so captcha:true and tier:guided are conservative assumptions pending a human render, not confirmed facts. Direct attempts to fetch www.outbrain.com/legal/privacy and www.outbrain.com/privacy hit a redirect loop (>10 redirects) both via WebFetch and are not reflected in the notes below as confirmed content. The legacy CSV's legal@outbrain.com was NOT corroborated on any page actually fetched (a related /legal page surfaced only info@teads.com for French content-provider inquiries), so opt_out_email is left null rather than asserted -- rely on the DSR settings URL as the primary channel. last_verified left null."
---

1. Go to https://dsr.outbrain.com/recommendations-settings/home (also reachable via the "Interest-Based Ads (Opt Out)" link in the footer of outbrain.com).
2. Follow the on-page steps to opt out of interest-based/personalized recommendations and ad targeting; you may need to enter an email address to identify your preferences.
3. Look for a CCPA "Do Not Sell or Share My Personal Information" option on the same settings page, since Outbrain processes data as an ad-tech/data broker subject to CCPA.
4. If you cannot locate a direct opt-out option, use Outbrain's general privacy policy page (outbrain.com/privacy) to find current contact details for a manual CCPA request.
5. Because this page loads dynamically and may include identity or CAPTCHA verification, complete the process in a standard browser rather than relying on a scripted request.
6. Re-check periodically, since ad-tech opt-out preferences are often browser/cookie-based and can reset if cookies are cleared.
