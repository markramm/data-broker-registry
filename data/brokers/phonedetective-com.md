---
id: phonedetective-com
name: "Phone Detective"
domain: phonedetective.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.beenverified.com/app/optout/search"
opt_out_email: "ccpa@numberguru.com"
phone: 1-866-673-9048
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, listing_url]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: data-brokers-watch
notes: "WebFetch of the migrated PD.aspx?_act=OptOut URL 301-redirected to numberguru.com, confirmed by WebSearch: phonedetective.com is now folded into NumberGuru, which is owned by BeenVerified. Corrected opt_out_url to numberguru.com and category/people_search (reverse-phone lookup is a people-search variant). Flow is: NumberGuru's 'Do Not Sell My Personal Information' footer link -> BeenVerified opt-out portal -> name+state search -> CAPTCHA -> email verification link. BeenVerified's opt-out form does not support removing multiple profiles at once; for that, contact privacy@beenverified.com or use the numberguru.com CCPA request path (ccpa@numberguru.com / 1-866-673-9048). CAPTCHA -> guided. last_verified left null (redirect target confirmed via WebSearch, not independently re-fetched). 2026-11-21 maintainer update (refs #255, #250): opt_out_url moved from the numberguru.com homepage to the page its footer link points to. A fetch today showed phonedetective.com still 301-redirects to https://www.numberguru.com/, and that homepage's footer link 'Do Not Sell My Personal Information' goes to https://www.beenverified.com/app/optout/search, the same URL the numberguru-com and beenverified-com entries use. That page answered a plain fetch with a Cloudflare challenge, so its form was not re-checked. The homepage URL made the page monitor flag a change every day, because the homepage carries a feed of user comments. Routing unchanged otherwise; last_verified stays null."
---

1. Note that phonedetective.com now redirects to numberguru.com, which is owned by BeenVerified.
2. Open the BeenVerified opt-out page at https://www.beenverified.com/app/optout/search. This is where the "Do Not Sell My Personal Information" link in numberguru.com's footer goes.
3. Click "Do Not Sell My Info," then enter your first and last name and select your state, and click "Search."
4. Locate your matching record, complete the CAPTCHA, and submit the removal request.
5. Check your inbox for a message from support@email.beenverified.com and click "Verify Opt-Out."
6. If you have multiple listings and BeenVerified's form won't remove them all at once, email privacy@beenverified.com, or use NumberGuru's direct CCPA request path at ccpa@numberguru.com / 1-866-673-9048.
