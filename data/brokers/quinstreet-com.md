---
id: quinstreet-com
name: QuinStreet, Inc.
domain: quinstreet.com
category: lead_generation
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "<verify: exact URL of QuinStreet's 'Do Not Sell or Share My Personal Information' portal link -- confirmed to exist in the site footer/privacy notice but the direct link target was not captured>"
opt_out_email: "legalq@quinstreet.com"
phone: "8889451080"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirmed via WebFetch on quinstreet.com/privacy-policy/ that QuinStreet is a lead-generation/customer-acquisition data broker across insurance, loans, credit cards, banking, and home-services verticals, matching the legacy CSV description. Confirmed multiple real opt-out channels described in the fetched policy text: a 'Do Not Sell or Share My Personal Information' portal link in the site footer, phone (888)-945-1080, SMS 'STOP' reply, and legalq@quinstreet.com for appeals/Nevada opt-outs. The policy states GPC signals are honored and opt-outs process within 1 day with no account required. I did not capture the exact portal URL (only that it exists in-footer per the fetched summary), so opt_out_url is left as a verify-placeholder; method is set to portal since that's the primary described channel, with the confirmed email as a documented fallback."
---

1. Go to https://www.quinstreet.com/privacy-policy/ (or quinstreet.com generally) and look for the "Do Not Sell or Share My Personal Information" link in the site footer.
2. Follow that link and complete the opt-out request as prompted; QuinStreet states these requests are processed within about one day and do not require creating an account.
3. If your browser sends a Global Privacy Control (GPC) signal, QuinStreet says it will honor that automatically -- check your browser/extension settings if you'd rather not do the manual opt-out.
4. Alternatively, call QuinStreet's privacy line at (888) 945-1080, or reply "STOP" to any text message you've received from a QuinStreet-affiliated service.
5. For an appeal, a Nevada-specific opt-out request, or if the portal doesn't resolve your situation, email legalq@quinstreet.com directly with your name and the request you're making.
6. Because QuinStreet operates across many different lead-gen brands and verticals (insurance, loans, credit cards, home services), your data may have entered through more than one QuinStreet-affiliated site -- the central opt-out is intended to cover all of them, but consider re-checking periodically.
