---
id: liftengine-com
name: Blue Hill Marketing Solutions, inc
domain: liftengine.com
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.liftbasedata.com/your-privacy-choices/"
opt_out_email: "dataprivacy@liftbasedata.com"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, dob, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on liftengine.com's privacy policy confirmed: consumer data broker operating multiple named consumer databases (LiftBase, American Pre-Movers, American New Movers, American WeddingBase) that sell targeted consumer/household audience data to brands for marketing. This is consumer (not B2B) data at the household/individual level -- movers, newlyweds -- which is more sensitive than typical B2B contact brokering, so bumped to high priority (not crucial, since it's marketing-segment audience data rather than a people-search identity/address lookup tool). LiftEngine's own policy defers CCPA handling to its parent/affiliate LiftBase, pointing to https://www.liftbasedata.com/privacy-policy/ and a 'Do Not Sell My Personal Information' link at https://www.liftbasedata.com/request-to-know/, plus an email contact dataprivacy@liftbasedata.com. Legacy CSV's emailprivacy@liftbasedata.com was not corroborated by the fetched text, which surfaced dataprivacy@liftbasedata.com instead; used the corroborated address. No CAPTCHA/ID mentioned. last_verified left null since the request-to-know form itself wasn't independently rendered. 2026-10-15 maintainer re-check (Refs page-monitor #25): liftbasedata.com/request-to-know/ now redirects to /your-privacy-choices/ (HTTP 200), which hosts the consumer request form; opt_out_url updated. The form says it is protected by Cloudflare Turnstile and reCAPTCHA (a cf-turnstile widget plus invisible reCAPTCHA v3), so captcha -> true and tier assisted -> guided. Required fields: yes/no choices for delete / opt-out / correct / tell-me, first and last name, email (entered twice), date of birth (month/day/year), US residential address, and an 'I am the individual identified above' checkbox. A mail-in form to LiftEngine, Attn: LiftBase Data Privacy, P.O. Box 1110, Pearl River, NY 10965 is offered as the alternative. Nothing was submitted."
---

1. Go to https://www.liftbasedata.com/your-privacy-choices/ (LiftEngine's privacy request page, hosted on its LiftBase data site; the old /request-to-know/ link redirects here). The form needs JavaScript and an up-to-date browser.
2. Answer "No" to "Are you acting as an agency on behalf of a consumer?".
3. Choose "Yes" for the actions you want: Delete My Data and/or Opt-Out (Stop Selling or Sharing my Personal Information).
4. Enter your first and last name, your email address (twice), your date of birth, and your US residential address. LiftBase organizes its records by residential address, so use the address you want removed.
5. Tick the box confirming you are the person identified, complete the CAPTCHA if one is shown, and submit.
6. If the form doesn't work for you, print LiftBase's mail-in form from the same page and mail it to LiftEngine, Attn: LiftBase Data Privacy, P.O. Box 1110, Pearl River, NY 10965, or email dataprivacy@liftbasedata.com.
7. Watch for a confirmation once your request is processed. The request covers all of Blue Hill Marketing Solutions' brands, including LiftEngine and LaunchPad.
