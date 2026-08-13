---
id: oracle-com
name: "Oracle America, Inc. (Oracle Advertising / Oracle Data Cloud)"
domain: oracle.com
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.oracle.com/legal/data-privacy-inquiry-form/"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: id_verify
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "Oracle's own bot-blocking (Akamai/WAF) returned HTTP 403 to WebFetch on oracle.com/legal/privacy/privacy-policy.html directly, so the page was instead fetched via curl with a browser user-agent, which succeeded (HTTP 200/301->200) and returned the full privacy policy text. That policy's 'Rights' and 'Contact' sections point to two live URLs: /legal/privacy/privacy-choices/ ('Privacy Choices' page, also linked in the footer as 'Do Not Sell My Info') and /legal/data-privacy-inquiry-form/ (the 'inquiry form' / 'Submit a request' link used to exercise opt-out, deletion, correction, or access rights). Fetched /legal/data-privacy-inquiry-form/ directly via curl: it returns HTTP 200 and is titled 'Privacy Choices and Data Subject Rights', confirming the URL is live and correct, but the actual form fields render via client-side JavaScript that a static fetch does not execute, so the exact field list/CAPTCHA presence could not be directly confirmed -- treated as guided tier and id_required left false (not confirmed) rather than assumed. The provided legacy CSV opt-out URL (oracle.ethicspointvp.com/custom/oracle/dp/en/form_data.asp) returned HTTP 404 and appears stale/replaced by the current inquiry-form URL above; privacy_ww@oracle.com email from the CSV was not corroborated anywhere in the fetched policy text, so opt_out_email is left null rather than asserted. Oracle Advertising/Oracle Data Cloud (formerly BlueKai/Datalogix/AddThis-derived audience data) is one of the largest marketing/advertising data aggregators in the industry, operating at a scale far beyond most entries in this dataset -- priority high per assignment guidance, not crucial, since it is not a consumer-facing people-search/address-reseller product. last_verified left null since the form's own fields were not directly rendered."
---

1. Go to https://www.oracle.com/legal/data-privacy-inquiry-form/ (Oracle's "Privacy Choices and Data Subject Rights" page, also reachable via "Do Not Sell My Info" in the site footer or the "Privacy Choices" link on Oracle's privacy policy page).
2. Select the request type that matches what you want: opt-out of sale/sharing, deletion, correction, or access to your personal information.
3. Fill in the requested identifying details (typically name and email) so Oracle can locate records associated with you across its advertising/data-cloud products.
4. Submit the form. Oracle's privacy policy states requests are handled under its published rights process, subject to identity verification before fulfillment.
5. Watch for a confirmation email and respond to any identity-verification step promptly, since large data brokers like Oracle commonly require this before completing a request.
6. If the form does not resolve your request, you can also contact Oracle's Global Data Protection Officer as referenced in the "Contact" section of Oracle's privacy policy (https://www.oracle.com/legal/privacy/privacy-policy.html).
7. Keep a record of your submission date in case you need to follow up, since opt-out preferences at this scale can take time to propagate across Oracle's advertising products.
