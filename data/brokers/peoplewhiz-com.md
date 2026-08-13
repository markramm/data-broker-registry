---
id: peoplewhiz-com
name: PeopleWhiz
domain: peoplewhiz.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "<verify: locate the actual opt-out/do-not-sell page path -- home page and all common paths were Cloudflare bot-challenge blocked in this session>"
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
notes: "peoplewhiz.com is a confirmed live people-search/background-check site: both WebFetch and curl (with a browser user-agent) hit a Cloudflare 'Attention Required' / bot-challenge page rather than a real 403-and-done block, and the Wayback Machine's availability API shows a successful (200) snapshot as recently as July 17, 2026 -- confirming this is currently active, not dead or parked. However every fetch attempt was blocked before reaching real page content, so I could not confirm the site's specific opt-out page path, privacy-policy text, or any opt-out email. opt_out_url is left as an explicit <verify:> placeholder per schema convention rather than guessed, and last_verified is null. tier:guided/captcha:true reflect the standard pattern for this class of people-search site seen consistently elsewhere in this repo (name/state lookup, listing selection, CAPTCHA, email verification), not a directly-confirmed process for this specific domain -- needs a human or a non-blocked fetch path to verify the exact URL/email before this entry is fully actionable."
---

1. Go to peoplewhiz.com and search your name and state to find your listing (you may need to pass a Cloudflare verification challenge to load the site).
2. Look for a "Do Not Sell My Info," "Opt Out," or "CCPA/Privacy" link, typically in the site footer or a linked privacy policy page.
3. Copy the URL of your specific profile/listing before starting the opt-out process, since most sites in this category require it.
4. Follow the opt-out form's prompts, which will likely include a CAPTCHA and an email-verification step to finalize the request.
5. Because this entry's exact opt-out page could not be confirmed in this research pass (see notes), verify the current opt-out path directly on the site or via an independent removal-guide source before relying on these steps, and update this entry once confirmed.
