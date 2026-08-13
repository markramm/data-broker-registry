---
id: merchantcircle-com
name: MerchantCircle
domain: merchantcircle.com
category: business_directory
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://privacyportal.onetrust.com/webform/27aa5d67-8136-4a08-ae4b-9860992e2375/a419e1e1-4937-4e26-8573-1f2d7fe677c8"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on https://www.merchantcircle.com/pages/privacy.html confirmed a live CCPA 'Do Not Sell or Share My Personal Information' link and a 'Limit the Use of Sensitive Personal Information' link, both pointing to the same OneTrust privacy-portal webform. MerchantCircle is primarily a local-business directory/reviews site (not a people-search product), but it runs a standard ad-tech CCPA opt-out for site-visitor personal information, so it's included as a lower-impact, standard-priority entry. Exact required fields for the OneTrust form were not itemized in the fetched content; email and full name are the near-universal minimum for these forms, listed here as a reasonable inference rather than a confirmed field list -- flagged in case a future verification pass finds otherwise. No CAPTCHA/ID gating was mentioned, so assisted rather than guided tier. support@merchantcircle.com is listed on the privacy page as general merchant support, not confirmed as a dedicated CCPA contact, so opt_out_email is left null rather than asserted."
---

1. Go to the OneTrust privacy request form linked from MerchantCircle's privacy page: https://privacyportal.onetrust.com/webform/27aa5d67-8136-4a08-ae4b-9860992e2375/a419e1e1-4937-4e26-8573-1f2d7fe677c8
2. Select the request type "Do Not Sell or Share My Personal Information" (or "Limit the Use of Sensitive Personal Information" if that better matches your request).
3. Enter your name and a valid email address so MerchantCircle can respond to your request.
4. Submit the form and watch for a confirmation email; follow any verification link it contains.
5. If the OneTrust form is unavailable, MerchantCircle's privacy page (https://www.merchantcircle.com/pages/privacy.html) lists support@merchantcircle.com as a general contact -- you can try emailing there and citing your CCPA rights, though this is not confirmed as their dedicated privacy channel.
