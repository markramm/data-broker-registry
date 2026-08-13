---
id: valpak-com
name: "Valpak (Valpak Direct Marketing Systems)"
domain: valpak.com
category: direct_mail_marketing
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://www.valpak.com/cpa/california"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [full_name, email, address, phone]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirmed via curl fetch that valpak.com is live and active post the 2020 Cox Target Media sale to Platinum Equity (unlike sibling coxtarget.com, found dead in a prior round) -- the site is serving current coupon listings under the Valpak brand. The footer contains two separate consumer-facing tools: 'Do Not Sell My Info (CA Residents Only)' linking to /cpa/california, and a separate 'Request Envelope Address Removal' link (for stopping the physical Blue Envelope mailer specifically, distinct from the CCPA data-sale opt-out -- not modeled as a separate field here but worth noting). Direct fetch of /cpa/california rendered a real embedded form requiring First Name, Last Name, Email, Phone, Street Address, City, Zip Code, restricted to California residents, with a 'Send' button; no CAPTCHA text appeared in the fetched HTML. Valpak is fundamentally a direct-mail coupon/advertising company rather than a dedicated data reseller, so priority is standard; the CCPA form requires several PII fields but no CAPTCHA/ID, so assisted tier. last_verified left null since this was a raw HTML fetch/regex extraction, not a full rendered-page confirmation."
---

1. Go to Valpak's California Consumer Privacy Act page at [valpak.com/cpa/california](https://www.valpak.com/cpa/california).
2. Confirm you are a current California resident (the form is restricted to CA residents).
3. Enter your first name, last name, email address, phone number, street address, city, and zip code.
4. Click "Send" to submit the Do Not Sell My Personal Information request.
5. If you separately want to stop receiving Valpak's physical "Blue Envelope" mailer at your address, use the distinct "Request Envelope Address Removal" link in the site footer -- that is a mailing-list removal, separate from this CCPA data-sale opt-out.
