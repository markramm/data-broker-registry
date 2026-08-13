---
id: nativo-com
name: "Life360 Ads (formerly Nativo, Inc.)"
domain: nativo.com
category: adtech
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://ads.life360.com/privacy-policy"
opt_out_email: "privacy-nativo@life360.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, other]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "Nativo, Inc. (the native-advertising platform) was acquired by Life360 -- nativo.com/privacy-policy now 301-redirects to ads.life360.com/privacy-policy, titled 'Life360 Ads Featuring Nativo Website Privacy Policy.' This is an adtech/programmatic-advertising company, not a people-search or identity-reseller service, so people_search is false and priority is standard (ad-targeting opt-out only, no direct personal-safety exposure). WebFetch of the redirected policy confirmed a CCPA sale/share/targeted-advertising opt-out: the stated primary path is the 'Your Privacy Choices' link in the site footer (a preference-management toggle, consistent with method:form/assisted rather than a plain email), with rights requests (including deletion/access) also acceptable via email at privacy-nativo@life360.com, and a TrustArc-hosted rights-request portal linked in the policy (submit-irm.trustarc.com/...). Because a real email path exists and is explicitly offered for rights requests including opt-out of sale, opt_out_email is populated with that address; tier is kept at assisted rather than auto because the primary documented mechanism is the footer preference toggle/portal, not a bare mailto flow. last_verified left null since this was a single WebFetch render, not human-confirmed."
---

1. Note that Nativo, Inc. has been acquired by Life360 and now operates as 'Life360 Ads featuring Nativo' -- its privacy policy lives at https://ads.life360.com/privacy-policy.
2. To opt out of the sale/sharing of your personal information for targeted advertising, look for the 'Your Privacy Choices' link in the footer of the ads.life360.com site and follow the preference-management flow it opens.
3. Alternatively, submit a rights request (including opt-out, access, or deletion) through the linked TrustArc request portal referenced in the privacy policy.
4. If you prefer email, send your request to privacy-nativo@life360.com, describing what you want (opt-out of sale/share, access, or deletion) and including enough information to identify your data (e.g. the email or device identifiers associated with your ad activity).
5. Because this is a programmatic-advertising/adtech company, the practical effect of this opt-out is limited to ad-targeting based on your browsing/app activity -- it will not remove you from unrelated data-broker or people-search listings.
