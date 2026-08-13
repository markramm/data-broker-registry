---
id: vdx-tv
name: "VDX.TV (Tribal Fusion)"
domain: vdx.tv
category: adtech
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://vdx.tv/policies/privacy#opting-out"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: []
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch confirms VDX.TV is an omnichannel/programmatic video advertising company ('TV Magnify', 'Video Magnify') extending TV ad campaigns to household members' personal devices -- an ad-tech/audience-targeting business, not a people-search or identity-resale broker. Its privacy policy at vdx.tv/policies/privacy has a 'Your Rights' > 'Opting Out/Deletion/Do Not Sell' section describing a single-click, cookie-based opt-out: clicking the provided link overwrites the site's identifier cookie with a non-identifying 'ANON_ID=optout' cookie on the tribalfusion.com domain (VDX.TV's legacy corporate name), valid for 10 years. No form fields, email, CAPTCHA, or account are required -- it is a browser-cookie opt-out rather than a data-deletion request tied to identity. Because this is cookie/device-scoped rather than an identity-verified CCPA request, and per-browser/per-device re-opt-out is required, classified as assisted (a human still needs to follow a link per browser/device) rather than auto. Ad-tech targeting company rather than a people-search/address broker -> people_search false, priority standard. last_verified left null."
---

1. Go to the VDX.TV privacy policy at [vdx.tv/policies/privacy](https://vdx.tv/policies/privacy) and find the "Opting Out/Deletion/Do Not Sell" section under "Your Rights."
2. Click the "opt out" link provided there.
3. Your browser will receive a replacement cookie (ANON_ID=optout, on the tribalfusion.com domain, valid 10 years) marking you as opted out of VDX.TV's ad targeting and data sale.
4. Repeat this step in every browser and on every device you use, since the opt-out is stored per-browser/per-device via cookie rather than tied to your identity.
5. If you clear your cookies later, you will need to repeat the opt-out.
