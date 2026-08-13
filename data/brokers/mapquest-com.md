---
id: mapquest-com
name: MapQuest (System1)
domain: mapquest.com
category: maps_local_search
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://privacyportal.onetrust.com/webform/f7e3f6db-ed65-4759-a3f5-3b5c8b7e9bff/draft/9949a1a8-aa69-4848-a93f-d093d877a981"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: email_confirm
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "Legacy CSV listed a Verizon privacy URL (verizon.com/about/privacy/mapquest) that now 404s. Live curl of mapquest.com's own footer privacy link (hello.mapquest.com/privacy) returns a meta-refresh to system1.com/terms/privacy-policy, whose HTML comment literally says it used to point at the dead Verizon page -- MapQuest is no longer Verizon-operated; it is now run by System1 OpCo, LLC (an ad-tech/lead-gen company). System1's privacy policy (fetched directly) documents full CCPA/CPRA sale/sharing disclosures and a 'Do Not Sell' link that resolves to a OneTrust webform (privacyportal.onetrust.com/webform/f7e3f6db-...). MapQuest itself is a maps/directions tool, not a people-search/address-reseller product, so priority is high rather than crucial. The OneTrust form's exact fields/CAPTCHA were not directly rendered (JS-heavy privacy-inquiries page did not return body content) -- guided tier and last_verified left null."
---

1. Go to the System1 privacy request portal: https://privacyportal.onetrust.com/webform/f7e3f6db-ed65-4759-a3f5-3b5c8b7e9bff/draft/9949a1a8-aa69-4848-a93f-d093d877a981 (linked as "Do Not Sell" from System1's privacy policy, which now governs MapQuest).
2. Select the request type for "Do Not Sell or Share My Personal Information" (or "Right to Opt Out" if the form uses different labeling).
3. Provide your name and an email address so System1 can locate and confirm your request.
4. Submit the form and watch for a confirmation email; click any verification link it contains.
5. If the webform is unavailable, use the general contact page at https://system1.com/contact-us to request escalation of a CCPA/CPRA opt-out for MapQuest specifically.
6. Allow up to 45 days for confirmation, per CCPA timelines.
