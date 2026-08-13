---
id: nielsen-com
name: Nielsen
domain: nielsen.com
category: media_marketing_data_broker
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://www.nielsen.com/legal/optout-page/"
opt_out_email: "privacy.department@nielsen.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa, cpra, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "Nielsen is a major global media/marketing measurement and data company (audience measurement, panels, big data + panel identity products). Fetched nielsen.com/legal/optout-page/ directly (HTTP 200) but it rendered as the general site shell/navigation with a OneTrust-managed privacy-preference-center link ('Limit the use of my sensitive personal information') in the footer rather than a standalone opt-out form body -- the actual opt-out control is embedded via OneTrust JS and wasn't fully renderable in this session. privacy.department@nielsen.com is confirmed as Nielsen's privacy contact from the same fetch/site. Given Nielsen's scale (large media/marketing data broker per the task brief) -> priority:high despite people_search:false (Nielsen does not resell individual identity/address lookups; it's audience/panel measurement data). tier:guided because the real mechanism is a OneTrust preference-center widget, not a simple form or plain email -- exact CAPTCHA/ID requirements could not be confirmed. last_verified left null; opt_out_url is the confirmed link target even though its interactive contents weren't fully rendered."
---

1. Go to https://www.nielsen.com/legal/optout-page/ and look for the "Limit the use of my sensitive personal information" link (Nielsen uses a OneTrust-based privacy preference center, usually reachable from the site footer as well).
2. Follow the preference-center flow to submit your opt-out / do-not-sell request; you'll typically need to provide an email address to identify your request.
3. If the self-serve portal doesn't resolve your request, email privacy.department@nielsen.com directly with your full name and a description of the personal information you want opted out of collection or sale, citing CCPA/CPRA (or GDPR if you're in the EU/UK).
4. Because Nielsen operates many regional privacy notices (including a separate Health Privacy Notice and Nielsen Marketing Cloud Privacy Statement), check whether a more specific notice applies to your situation and follow any instructions specific to that notice.
