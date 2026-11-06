---
id: stirista-com
name: Stirista
domain: stirista.com
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://unsubscribe.stirista.com/"
opt_out_email: "privacy@stirista.com"
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "Stirista, LLC is a consumer marketing-data broker; andrewswharton.com (already in this dataset) is a sibling brand under the same company and its privacy policy redirects entirely to Stirista's. WebFetch of stirista.com/privacy-policy/ confirmed the opt-out mechanism: a self-serve portal at https://unsubscribe.stirista.com/, requesting current address, email address, and any prior home/email addresses so records can be matched and suppressed; alternatively email privacy@stirista.com (a California-specific address, privacyinfo@stirista.com, is also mentioned). The policy states identity verification is performed 'in part by requesting certain information' before processing. No CAPTCHA mentioned. Legal basis spans CCPA and other US state privacy laws plus GDPR/UK/Swiss frameworks (recorded here as ccpa+gdpr as representative). Priority set to high (not crucial) because Stirista is a marketing/audience-data broker (not a people-search/address-lookup service) but has a real, working self-serve opt-out mechanism. last_verified left null since the page was summarized via fetch tool rather than independently re-rendered. Updated 2026-11-03 by the daily maintainer (found while checking Alesco Data, now a Stirista company; Refs #171): unsubscribe.stirista.com rendered headless (HTTP 200) shows a visible reCAPTCHA v2 checkbox (google.com/recaptcha/api2/anchor iframe, 256x60), so captcha false -> true and tier assisted -> guided. The portal has four separate sections: email-only removal; postal removal (first name, last name, address, city, region, country, postal code required); mobile opt-out (MAID and phone); and a sale/sharing inquiry (email plus description). Email alone is enough for the first section, so required_fields is now [email]. The portal lists the Privacy Officer at Stirista, Inc., 777 E. Sonterra Blvd., Suite 225, San Antonio, TX 78258, privacy@stirista.com, and says a deletion and an opt-out have the same practical effect (deletion from active databases plus suppression). Nothing was submitted."
---

1. Go to Stirista's unsubscribe/privacy portal at https://unsubscribe.stirista.com/.
2. In the first section, enter your email address, complete the CAPTCHA and submit.
3. Also fill in the "No email? No problem!" section with your name and mailing address and submit it. Repeat the relevant section for every email address and home address you have used, because each request covers only the address you enter.
4. Alternatively, email privacy@stirista.com (or privacyinfo@stirista.com if you are a California resident) directly, stating you want to opt out of the sale/sharing of your personal information under the CCPA (or GDPR, if applicable).
5. Stirista may contact you to verify your identity before completing the request; allow roughly 10 business days for processing per their stated policy.
6. Because Stirista also operates under sibling brand names (e.g. Andrews Wharton Inc.), a single opt-out here should cover data controlled by those affiliated brands as well.
