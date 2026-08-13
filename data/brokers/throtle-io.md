---
id: throtle-io
name: Throtle
domain: throtle.io
category: adtech_identity_resolution
people_search: false
tier: guided
priority: standard
method: email
opt_out_url: "https://optout.thrtle.com/optout"
opt_out_email: "privacy@throtle.io"
phone: "+1-866-672-5235"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "Throtle is a B2B identity-resolution/adtech company (cross-device identity graph linking PII to ad IDs for marketers), not a consumer-facing people-search site -- priority set to standard rather than crucial. WebFetch on throtle.io/privacy/ rendered live and quoted, verbatim, a CCPA opt-out section listing: a cookie opt-out link at https://optout.thrtle.com/optout (note: 'thrtle.com', not 'throtle.io' -- this looked like a possible model hallucination, so I independently confirmed via DNS that optout.thrtle.com resolves and WebFetch on it renders 'You have opted out of the Throtle DMP', confirming it is a real, live Throtle-branded short domain, not fabricated); a Data Subject Access Request webform hosted at privacyportal.privacypillar.com (a third-party OneTrust-style DSAR portal) which rendered only a bare 'Privacy Portal' heading and could not be independently confirmed to be Throtle-specific beyond the URL context on the privacy policy page; a toll-free number (866) 672-5235; a mailing address (Throtle, Inc., 141 West Front Street, Suite 312, Red Bank, NJ 07701, ATTN: Privacy Officer); and an email, privacy@throtle.io. Also confirmed throtle.io/texas-data-broker-notice is live and states the entity is a registered Texas data broker under 1 TAC 106.5(1), corroborating Throtle is a genuine data broker. Because tier:auto requires a plain email opt-out and the site's primary documented mechanism is a cookie tool plus a third-party DSAR webform (not a bare email-only flow), classified as guided rather than auto, but opt_out_email is populated since Throtle's own policy explicitly offers email as an equally valid channel ('Or, you may email us at privacy@throtle.io'). Method set to email to reflect that this is the most reliable/user-controllable channel found; the cookie tool only clears the current browser/device per Throtle's own stated limitation ('you must opt-out separately for each browser and device'). last_verified left null since none of this was independently re-rendered by me beyond the WebFetch summarization pass -- treat opt_out_url/opt_out_email as WebFetch-sourced from a live page but not human-eyeballed."
---

1. Email privacy@throtle.io from an address you control, stating your full name and that you are submitting a CCPA/CPRA "Do Not Sell or Share My Personal Information" and deletion request covering any data Throtle holds or has shared through its Consumer Graph / identity-resolution products.
2. Separately, visit https://optout.thrtle.com/optout in every browser and on every device you use; this sets a browser-level opt-out cookie for Throtle's data management platform (DMP) and must be repeated per browser/device, since it does not work if third-party cookies are blocked.
3. If you want a documented Data Subject Access Request instead of (or in addition to) the email, look for the "Data Subject Access Requests" link on throtle.io/privacy/ (routes to a third-party privacypillar.com DSAR form) and fill it out with your contact details.
4. You can also call Throtle's toll-free privacy line at (866) 672-5235, or mail a written request to: ATTN: Privacy Officer, Throtle, Inc., 141 West Front Street, Suite 312, Red Bank, NJ 07701.
5. Throtle states it will complete processing of opt-out requests within 15 days of receipt.
6. Because Throtle is an identity-resolution vendor that links your PII to ad-tracking IDs on behalf of other marketers (not a site where you have a visible profile), there is no listing URL to reference -- your request should simply assert your CCPA/CPRA rights and ask Throtle to confirm removal from its Consumer Graph / Tag / Crosswalks products.
