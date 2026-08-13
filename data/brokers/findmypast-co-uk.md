---
id: findmypast-co-uk
name: Findmypast
domain: findmypast.co.uk
category: genealogy_records
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "<verify: locate the current CCPA/privacy-rights request page under findmypast.com or findmypast.co.uk -- WebFetch of findmypast.co.uk/content/privacy-policy and findmypast.com/content/privacy-policy both returned HTTP 403, and the plain curl fetch only returned a client-rendered SPA shell with no policy text or contact email visible>"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "Findmypast is a well-established UK/US genealogy and family-history records company (historical census, birth/marriage/death, military and immigration records), which publishes records that can include personal information about living relatives found in more recent record sets -- genealogy sites of this kind are commonly included in data-broker/opt-out registries alongside Ancestry.com. However, I was not able to independently confirm the live opt-out mechanism: WebFetch of both the .co.uk and .com privacy-policy URLs returned HTTP 403 (bot-blocked), and a direct curl fetch only retrieved the client-side-rendered app shell (a 'titan' SPA) with no privacy-policy text, CCPA section, or contact email present in the initial HTML. The legacy CSV supplied support@findmypast.com as a contact email, but I could not verify this is the correct address for a privacy/opt-out request specifically (vs. general customer support) and am not using an unconfirmed email for an auto-tier entry. Classified as method:form/tier:guided conservatively pending human verification of the actual request path; opt_out_url is a verify-placeholder and last_verified is null accordingly. people_search left false -- this is a genealogy records archive, not a general identity/address lookup service, though it does publish personal information about named individuals."
---

1. Findmypast is a genealogy/family-history records service; it publishes historical records (census, vital records, military records) that can include information about relatives, some of whom may still be living.
2. This entry could not be independently verified: attempts to fetch findmypast's live privacy policy pages returned bot-blocked (403) or client-rendered content with no visible text.
3. To pursue a removal or opt-out request, look for a "Privacy Policy" or "Your Privacy Choices" link in the footer of findmypast.co.uk or findmypast.com, which should describe how to contact their privacy/support team.
4. If you find a specific record about yourself (rather than a historical relative) that you want removed, most genealogy sites handle this as a "living person" record-suppression request rather than a full account opt-out -- look for a "report this record" or similar link on the record page itself.
5. Given the uncertainty here, consider contacting Findmypast's general customer support channel and asking them to route your request to their privacy/data-protection team; confirm any email address independently before sending personal information.
