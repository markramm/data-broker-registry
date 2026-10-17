---
id: bdo-com
name: BDO USA, LLP (Global Corporate Intelligence / Investigative Due Diligence)
domain: bdo.com
category: background_check
people_search: true
tier: assisted
priority: high
method: form
opt_out_url: "https://form.bdo.com/"
opt_out_email: "privacy@bdo.com"
phone: "1-616-575-8785"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [full_name, email, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "2026-10-16 maintainer run (Fixes #68): the old opt_out_url (bdo.com/do-not-sell-my-personal-information, HTTP 200) no longer holds a form; it now says BDO GCI's privacy request process has moved to form.bdo.com. Fetched https://form.bdo.com/ (HTTP 200, 'Privacy Request Form (BDO GCI Services)'). It requires first and last name, an email address for responses, country, street address, city, state and ZIP, a self/authorized-agent choice, and one request type per submission (opt-out, delete, access, correct). Phone, middle name and extra emails/phones/addresses are optional. The form markup wires up reCAPTCHA Enterprise but sets data-recaptcha-enabled=false and shows no challenge widget, so captcha: false and tier assisted (was guided); a person should confirm no challenge appears on submit. The page does not say how the request is verified, so verification is null. Nothing was submitted. Background kept from the earlier pass: the form covers only BDO's Global Corporate Intelligence (GCI) unit, which compiles and sells due-diligence research reports on named individuals; BDO's audit/tax/advisory business states it does not sell personal information. Treated as people_search-adjacent at high priority. last_verified stays null."
---

1. Go to https://form.bdo.com/ (Privacy Request Form for BDO GCI Services). It only covers BDO's Global Corporate Intelligence unit.
2. Enter your first and last name, an email address for responses, and your full home address (street, city, state, ZIP). BDO says it uses the address to tell you apart from people with the same name.
3. Optionally add phone numbers, other email addresses or past addresses (up to 10 each) to help BDO find every record.
4. Confirm you are the person named (or that you are an authorized agent), then choose "Request to Opt-out" and submit.
5. The form takes one right per submission. To also ask for deletion, submit it again with "Request to Delete" selected.
6. Alternatively, email privacy@bdo.com or call 1 (616) 575-8785 with the same request.
7. The opt-out does not undo due-diligence reports already produced before your request.
