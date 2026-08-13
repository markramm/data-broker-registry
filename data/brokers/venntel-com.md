---
id: venntel-com
name: "Venntel, Inc."
domain: venntel.com
category: location_data_broker
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.venntel.com/opt-out"
opt_out_email: "privacy@venntel.com"
phone: "877-717-9985"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [full_name, email, phone, other]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch confirms Venntel is a mobile-device location-data broker: 'Venntel provides real-world location intelligence. Our platform merges, categorizes and interprets disparate Location Data,' sourced from partner apps and resold to customers (including, per public reporting, government/law-enforcement customers). Given the precise-location tracking involved, people_search is set true per this batch's guidance on personal-safety stakes. The privacy policy describes an opt-out via 'Opt-Out & Do Not Sell Form' at venntel.com/opt-out, or by emailing privacy@venntel.com, or by disabling location services on the device directly. WebFetch on the opt-out form itself showed fields for First Name, Last Name, Company name*, Business email*, Phone number*, a Request Type dropdown*, and an optional Message -- notably the form is phrased for 'Company'/'Business email,' i.e. built more for business inquiries than individual consumers, which is unusual and worth flagging; a plain consumer likely still uses it by entering personal info in those fields, or should use the plain-language privacy@venntel.com email instead. No CAPTCHA observed. Because opt-out is device/identifier-scoped (mobile ad ID) rather than simple email-based, and the form's business-oriented framing adds friction, classified guided rather than auto despite method:email being available as a fallback. last_verified left null."
---

1. Note that Venntel's opt-out is tied to mobile advertising identifiers and location data associated with your device(s), not just your name -- disabling location-sharing permissions on each device is also part of fully opting out.
2. Go to the Venntel opt-out form at [venntel.com/opt-out](https://www.venntel.com/opt-out).
3. The form is labeled for "Company"/"Business email" fields; as an individual consumer you can still fill in your own name, email, and phone number, selecting the closest matching "Request Type" (e.g., opt-out / do-not-sell).
4. Submit the form.
5. If the form does not work for an individual request, instead email privacy@venntel.com directly and state you are a consumer requesting to opt out of the sale of your location data under the CCPA.
6. You can also call 877-717-9985 to make the same request by phone.
7. Separately, review and restrict location-sharing permissions for apps on your phone, since Venntel sources location data through third-party apps' SDKs rather than directly from you.
