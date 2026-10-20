---
id: usdatacorporation-com
name: "US Data Corporation"
domain: usdatacorporation.com
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.usdatacorporation.com/opt-out"
opt_out_email: "privacy@usdatacorporation.com"
phone: "888-578-3282"
captcha: true
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [email, other]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch confirms US Data Corporation is a direct-marketing list/data-append provider that self-identifies on its own site as a data broker: 'The entity maintaining this website is a data broker under Texas law.' It offers targeted marketing lists (email, direct mail, telemarketing) across 303M+ consumers. Footer/nav link to a dedicated 'Do Not Sell My Info' page at /do-not-sell-my-info/, which in turn points to an online form at /opt-out, email privacy@usdatacorportion.com (note: this misspelling 'corportion' appears in the fetched privacy-policy text itself -- flagging as likely a typo on the broker's own site; used the correctly-spelled privacy@usdatacorporation.com in this entry pending manual confirmation of which actually delivers), and phone (888) 578-3282. The privacy policy states the /opt-out form only collects information 'to review and comply with the request' but does not enumerate exact fields; a WebFetch directly on /opt-out saw a generic 'provide the information requested below so that we may locate your record in our database' prompt but the specific field list did not render. No CAPTCHA was mentioned anywhere. Deep-linkable form with no CAPTCHA/ID gate -> assisted tier. Marketing list aggregator (not consumer-facing people search) -> people_search false, priority high. last_verified left null; the opt_out_email spelling should be double-checked against the live page before use. 2026-10-15 maintainer re-check (Refs page-monitor #64): fetched /opt-out (HTTP 200). The form is an iframe served by a third-party privacy-request vendor (forgetmenaut.com/rtbf/unjVFFNnmFvsZ17Fnk3Tap6U). Its markup has a visible reCAPTCHA v2 widget (div.g-recaptcha with a sitekey, not invisible), so captcha -> true and tier assisted -> guided. Required fields are email, a jurisdiction selector (CCPA, VCDPA, etc.) and a request category (deletion, opt_out, ...); name, phone, date of birth, address, MAID and VIN are optional. required_fields -> [email, other]. The 'Email' field the monitor saw on the parent page is a newsletter box, not the opt-out form. Nothing was submitted."
---

1. Go to the US Data Corporation opt-out form at [usdatacorporation.com/opt-out](https://www.usdatacorporation.com/opt-out).
2. The request form is embedded on that page (it is run by a third-party privacy-request service). Enter your email address, pick your jurisdiction (e.g. CCPA), and choose the request category: "opt_out" or "deletion".
3. Name, phone, date of birth, address and other identifiers are optional. Add only what they need to find your marketing record, such as your name and mailing address.
4. Complete the CAPTCHA and submit the form.
5. If the form does not work or you prefer email, contact privacy@usdatacorporation.com (verify the exact spelling shown on the live privacy-policy page, as the fetched text rendered it inconsistently) and state you are requesting a CCPA "Do Not Sell My Info" opt-out.
6. You can also call (888) 578-3282 to make the same request by phone.
7. Alternatively, mail a written request to: US Data Corporation, Attn: Privacy Administrator, 5115 Clareton Drive Ste. 210, Agoura Hills, CA 91301.
