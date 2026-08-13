---
id: stirista-com
name: Stirista
domain: stirista.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: high
method: portal
opt_out_url: "https://unsubscribe.stirista.com/"
opt_out_email: "privacy@stirista.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, address]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "Stirista, LLC is a consumer marketing-data broker; andrewswharton.com (already in this dataset) is a sibling brand under the same company and its privacy policy redirects entirely to Stirista's. WebFetch of stirista.com/privacy-policy/ confirmed the opt-out mechanism: a self-serve portal at https://unsubscribe.stirista.com/, requesting current address, email address, and any prior home/email addresses so records can be matched and suppressed; alternatively email privacy@stirista.com (a California-specific address, privacyinfo@stirista.com, is also mentioned). The policy states identity verification is performed 'in part by requesting certain information' before processing. No CAPTCHA mentioned. Legal basis spans CCPA and other US state privacy laws plus GDPR/UK/Swiss frameworks (recorded here as ccpa+gdpr as representative). Priority set to high (not crucial) because Stirista is a marketing/audience-data broker (not a people-search/address-lookup service) but has a real, working self-serve opt-out mechanism. last_verified left null since the page was summarized via fetch tool rather than independently re-rendered."
---

1. Go to Stirista's unsubscribe/privacy portal at https://unsubscribe.stirista.com/.
2. Provide your current mailing address and email address, plus any prior home or email addresses you've used, so Stirista can match and suppress all associated records.
3. Submit the request through the portal.
4. Alternatively, email privacy@stirista.com (or privacyinfo@stirista.com if you are a California resident) directly, stating you want to opt out of the sale/sharing of your personal information under the CCPA (or GDPR, if applicable).
5. Stirista may contact you to verify your identity before completing the request; allow roughly 10 business days for processing per their stated policy.
6. Because Stirista also operates under sibling brand names (e.g. Andrews Wharton Inc.), a single opt-out here should cover data controlled by those affiliated brands as well.
