---
id: ask-com
name: "Ask.com"
domain: ask.com
category: search_engine
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "<verify: exact Do Not Sell or Share My Personal Information page URL on ask.com>"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: []
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on ask.com/privacy.html confirmed Ask.com (Ask Media Group, an IAC brand) explicitly states it sells/shares identifiers, geolocation, and internet-activity data to third-party advertisers and lead-gen partners -- a real CCPA-covered ad-tech data seller, not a people-search broker. The policy directs users to a 'Do Not Sell or Share My Personal Information' link in the site footer (also honors Global Privacy Control signals) rather than a single stable URL, and lists privacy@ask.com for privacy requests. Could not confirm the exact footer-link destination URL via fetch, so opt_out_url is a placeholder and last_verified is null. Marked standard priority (ad-tech cookie-based opt-out, not personal-safety-critical) and guided tier since the only confirmed path is a footer click-through, not a direct deep link."
---

1. Go to [ask.com](https://www.ask.com) and scroll to the footer of any page.
2. Click the "Do Not Sell or Share My Personal Information" link in the footer.
3. Follow the on-page instructions to opt out of the sale/sharing of your data via cookies and other tracking technologies. If you use a browser or extension that sends a Global Privacy Control (GPC) signal, Ask.com states it will honor that signal automatically.
4. For other privacy requests (access, deletion) not covered by the footer opt-out, email privacy@ask.com with your request and identifying details sufficient for them to locate your data.
5. Keep a copy of any confirmation you receive; re-check periodically since ad-tech opt-outs are often cookie- or browser-scoped and can reset.
