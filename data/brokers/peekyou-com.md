---
id: peekyou-com
name: "Peek You"
domain: peekyou.com
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://www.peekyou.com/about/contact/ccpa_optout/do_not_sell/"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "data-brokers-watch + tcp-verified"
notes: "MIGRATED research_note: live CCPA do-not-sell form (bot-block 403). Reconfirmed on this pass: WebFetch and direct DNS/curl both failed against peekyou.com; the domain now appears to route through people.inc (PeekYou's parent brand), which returned a Cloudflare bot-challenge 403 as well. Could not freshly re-render the form, so last_verified stays null. Kept prior TCP assessment that this is a genuine, working CCPA do-not-sell form -- typically these require your profile URL, name, and email, with no CAPTCHA or ID upload for the basic CCPA opt-out path. Priority crucial: PeekYou is a people-search/social-profile-aggregation site."
---

1. Search for yourself on PeekYou.com to find your profile page, and copy its exact URL.
2. Go to the CCPA do-not-sell opt-out form (peekyou.com/about/contact/ccpa_optout/do_not_sell/).
3. Paste your profile URL and enter your full name and email address as requested.
4. Submit the form -- this is a standard CCPA "do not sell my personal information" request, so it applies regardless of which state you live in, though it's specifically grounded in California's CCPA.
5. Watch for a confirmation email, and check back on your profile URL after a few weeks to confirm the listing was actually removed or suppressed.
6. Because this is a people-search/aggregation site pulling from social profiles and public records, consider repeating this periodically since listings can reappear.
