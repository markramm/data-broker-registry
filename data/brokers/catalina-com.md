---
id: catalina-com
name: Catalina Marketing
domain: catalina.com
category: retail_purchase_data
people_search: false
tier: guided
priority: high
method: email
opt_out_url: "<verify: catalina.com's full Privacy Notice is a OneTrust-hosted 'otnotice' widget loaded client-side by JS -- it did not appear in the static HTML of catalina.com/legal, so no direct CCPA 'Do Not Sell' webform URL could be confirmed>"
opt_out_email: "privacyteam@catalina.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirms the prior pass's finding that catalina.com is a JS-rendered site that resists straightforward fetching, but this pass got further. Catalina is a genuine data broker: it describes itself as decoding shopper behavior from 'one of the world's largest sources of deterministic purchase data' and selling 'custom or syndicated segments' of consumer purchase data to CPG brands, retailers, and pharma companies (confirmed via WebFetch of catalina.com homepage). The site's /legal page is built on a framework (Coldsnap) that server-renders some accordion content but loads the actual Privacy Notice via a OneTrust 'otnotice' div populated client-side -- so no fixed CCPA opt-out webform URL could be confirmed despite fetching the raw HTML directly with curl (bypassing the WebFetch tool's own JS-blindness). What WAS confirmed in the raw HTML: a Cookie Policy 'CONTACT US' section stating 'If you have any privacy concerns, please contact us by e-mail at privacyteam@catalina.com or dpo@catalina.com' (dpo@catalina.com is scoped to EU/UK inquiries per the same text), and a reference that 'For US privacy inquiries please refer to Your Privacy Rights' which links to a OneTrust portal (app.onetrust.com/#yourprivacyrights_sec_5) whose exact behavior/URL for this specific tenant could not be verified. Given the confirmed, non-EU-scoped privacyteam@catalina.com contact and CCPA legal basis (US company, sells purchase data, California consumers covered), used method:email with that address rather than leaving the entry entirely unresolved -- but tier is guided (not auto) because the process is not a documented plain email opt-out with known required fields, it's a general privacy-concerns inbox of unconfirmed process. opt_out_url left as a <verify:> placeholder since the real CCPA-specific webform could not be located; last_verified null per placeholder rule."
---

1. Email privacyteam@catalina.com and state that you are a California resident (or otherwise covered by applicable state privacy law) requesting to opt out of the sale/sharing of your personal information and/or requesting access to or deletion of the purchase/loyalty data Catalina holds about you.
2. Include your full name and the email address(es)/loyalty program(s) you believe Catalina's retail partners may have associated with your purchase history, since Catalina aggregates data through retailer loyalty programs rather than direct signup.
3. If you don't get a response, check the "Your Privacy Choices" / "Your Privacy Rights" link in the footer of catalina.com/legal, which routes through a OneTrust privacy-rights portal -- this may offer a formal webform alternative to email.
4. Note that because Catalina receives your data indirectly through retailer partners (grocery/pharmacy loyalty programs), you may also need to check opt-out options directly with those retailers to fully stop new data from reaching Catalina.
5. Retain a copy of your request and any confirmation email for your records, since this process is not independently verified against a live, rendered opt-out page.
