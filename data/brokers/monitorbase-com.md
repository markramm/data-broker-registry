---
id: monitorbase-com
name: MonitorBase
domain: monitorbase.com
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://my.monitorbase.com/privacypolicy"
opt_out_email: null
phone: "888-795-6575"
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, phone, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "MonitorBase (Lender Feed LC) is a B2B trigger-lead monitoring service for mortgage professionals -- it scans consumers' credit/real-estate activity (Experian-sourced) and alerts mortgage brokers/lenders when a past contact is shopping for a new loan. Not a people-search site (no direct-to-consumer lookup product), so people_search is false and priority is high rather than crucial. WebFetch of my.monitorbase.com/privacypolicy confirmed a CCPA 'Do Not Sell My Personal Information' section with two channels: a phone line (888-795-6575) and an online form at the bottom of the same privacy-policy page (name/email/phone/address fields, request-type selector, CAPTCHA, and a certification checkbox). No dedicated opt-out email was found -- the only email referenced on the page is Support@monitorbase.com, shown in a data-breach-notification context, not as a stated opt-out channel, so opt_out_email is left null and method is form (CAPTCHA-gated -> tier guided) rather than email. last_verified left null since this is reconstructed from a single WebFetch render, not a human-confirmed page view."
---

1. Go to the [MonitorBase Privacy Policy page](https://my.monitorbase.com/privacypolicy), which also hosts the "Do Not Sell My Personal Information" request form.
2. Scroll to the opt-out/request form at the bottom of the page.
3. Select the request type for opting out of sale of personal information, then enter your name, email, phone number, and mailing address.
4. Complete the CAPTCHA and check the certification box confirming you are the person (or an authorized agent) making the request.
5. Submit the form. MonitorBase states opt-out requests submitted this way are processed automatically, typically within about a day.
6. If you prefer not to use the web form, you can instead call MonitorBase's privacy line at 888-795-6575 to request the same opt-out.
