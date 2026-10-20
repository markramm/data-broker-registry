---
id: socialcatfish-com
name: Social Catfish
domain: socialcatfish.com
category: people_search
people_search: true
tier: guided
priority: high
method: form
opt_out_url: "https://socialcatfish.com/opt-out/"
opt_out_email: null
phone: "(844) 422-8347"
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, other]
readd_days: null
legal_basis: [ccpa]
last_verified: "2026-07-29"
source: badbool
notes: "Replaces a thin legacy stub (source data-brokers-watch, phone-only, opt_out_url null) migrated from data/legacy/data-brokers-watch-source.csv -- this entry supersedes it with a real, verified web opt-out flow. Fetched live 2026-07-29: socialcatfish.com/opt-out/ renders a form with a required state-of-residence dropdown plus first/last name and email as the only mandatory fields; middle initial, age range, extra emails/phones, up to 8 photos, other states lived in, and a direct profile link are all optional but said to speed up matching. A checkbox asks whether you're submitting on your own behalf or as an authorized agent. No CAPTCHA was present in the fetched content and no fee is mentioned. Social Catfish states it will ensure your info isn't for sale within 15 days. They note they may request identity verification if fraud is suspected, and list (844) 422-8347 as a support line. Reverse-image/identity-verification-oriented people-search site -- tier assisted since no CAPTCHA/ID gating was observed, though optional photo upload is a notable data-sharing consideration worth flagging to users. 2026-10-15 maintainer re-check (Refs page-monitor #29): fetched /opt-out/ (HTTP 200, lands on /opt-out/?id=request_optout). The opt-out form (request_optout_form) now contains a Cloudflare Turnstile widget (div.cf-turnstile with a sitekey), so captcha -> true and tier assisted -> guided. The human-verified routing (URL, fields) was not changed, so last_verified is untouched. Nothing was submitted."
---

1. Go to the [Social Catfish opt-out form](https://socialcatfish.com/opt-out/) and select your current state of residence from the dropdown.
2. Fill in the required fields: first name, last name, and email address.
3. Optionally add details that help them find and remove the right profile faster -- middle initial, age range, other emails/phones, direct link to your Social Catfish profile, or photos -- but you can skip these if you'd rather not share more than necessary.
4. Confirm whether you're submitting for yourself or as an authorized agent, complete the CAPTCHA, then submit the form.
5. Social Catfish states it will stop offering your info for sale within 15 days of the request; if you don't see results, call (844) 422-8347.
6. Be aware the form may ask for identity verification if they suspect a fraudulent request -- that's a Social Catfish anti-abuse step, not something you need to preemptively provide.
