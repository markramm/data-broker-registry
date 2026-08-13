---
id: anywho-com
name: AnyWho
domain: anywho.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.spokeo.com/optout"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Direct WebFetch of anywho.com and www.anywho.com both failed to connect, so this entry is reconstructed from WebSearch of third-party opt-out guides (Incogni and others), consistent across independent sources: AnyWho is a legacy reverse-phone/white-pages people-search site (historically AT&T/YellowPages-affiliated) still live and drawing meaningful US traffic in 2026, but it no longer maintains its own opt-out form -- its privacy policy now directs all data-removal requests to Spokeo's opt-out tool at spokeo.com/optout, requiring the AnyWho/Spokeo profile URL, an email address, a reCAPTCHA, and a confirmation-link click within 72 hours. Free, no ID or phone required. Not independently verified against a rendered anywho.com page -- last_verified left null. Caution: unrelated copycat/scam domains like 'anywho-com.com' exist and are not this broker."
---

1. Search your name or phone number on anywho.com and locate the listing that matches you.
2. Note the listing's URL, then go to https://www.spokeo.com/optout -- AnyWho's own privacy policy redirects all removal requests to Spokeo's opt-out tool rather than handling them itself.
3. Paste the listing URL into Spokeo's opt-out form along with a valid email address, and solve the CAPTCHA.
4. Submit the form, then check your email for a confirmation link and click it within 72 hours -- the opt-out isn't final until confirmed.
5. Repeat for each distinct matching listing, since AnyWho/Spokeo may hold multiple records under different addresses or phone numbers.
