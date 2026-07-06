---
id: path2response-com
name: Path2Response
domain: path2response.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://privacyportal-cdn.onetrust.com/dsarwebform/2de26f06-de6f-45a7-8e1d-7d1148a3f301/draft/7a5dc7d1-cc7e-43a8-9f24-702807deb65b.html"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, address]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: data-brokers-watch
notes: "Page loads but is a JS-rendered OneTrust DSAR webform (Salesforce/OneTrust privacy-portal framework) -- WebFetch only returned the static HTML shell with no visible field labels, and the form's actual fields are populated client-side, so the exact field list couldn't be confirmed by fetch alone. last_verified left null. Assessed tier/required_fields from OneTrust DSAR webform conventions: these forms typically present a privacy-request-type selector (access/delete/opt-out/do-not-sell) plus name, email, and mailing address fields, generally without CAPTCHA or ID upload for a basic opt-out/do-not-sell request. Path2Response is a direct-mail/marketing list co-op data broker (B2B-facing), so priority is standard (spam/marketing harm, not physical-safety harm)."
---

1. Open the Path2Response privacy request form (the OneTrust-hosted DSAR webform linked in opt_out_url).
2. When the form's request-type selector loads, choose the option for "opt-out of sale/sharing" or "do not sell my personal information" (California/CPRA-style requests) -- or "delete my data" if you want full deletion rather than just an opt-out.
3. Enter your full name, email address, and mailing address as prompted.
4. Submit the form and watch for a confirmation email, which some OneTrust portals send to verify your email address before processing the request.
5. If the form doesn't load or errors out, note that Path2Response is a data co-op/marketing aggregator serving many direct-mail clients -- removal here won't necessarily affect other brokers you're independently listed with.
