---
id: veraset-com
name: "Veraset, LLC"
domain: veraset.com
category: location_data_broker
people_search: true
tier: guided
priority: crucial
method: email
opt_out_url: "<verify: veraset's own privacy policy cites https://www.veraset.com/do-not-sell-my-personal-information/ as its opt-out form, but a direct fetch of that exact URL returned the site's 404 'Page Not Found' page -- confirm whether this is a temporary outage or the link is stale before using it>"
opt_out_email: "privacy@veraset.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: none
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch and curl both confirm Veraset is a mobile-location data broker: sells 'billions of daily GPS pings worldwide' as 'business intelligence,' and its own privacy policy discloses sharing 'your device's location information, mobile advertising identifier, venues and events you attended' with clients who 'may also resell your information to other third parties.' Given precise-location tracking, people_search set true per this batch's guidance. The privacy policy (fetched at veraset.com/legal/privacy-policy) directs consumers wanting to opt out of the sale of hashed email, mobile ad ID, and location data to 'complete Veraset's opt-out and do not sale form at https://www.veraset.com/do-not-sell-my-personal-information/.' A direct curl fetch of that exact URL (including a redirect-normalized variant) returned HTTP 404 with the site's own 'Page Not Found' template -- i.e., the link Veraset cites in its own current privacy policy appears broken as of this research. The same policy's Contact section gives a working fallback: privacy@veraset.com, or mail to Veraset LLC, 127 S Peyton St Suite 301, Alexandria, VA 22314. Because the documented web form is currently unreachable, method is set to email (the confirmed-working channel) and opt_out_url is left as a verify placeholder pending confirmation the form URL is fixed. Guided tier reflects the need to fall back to a manual email given the broken self-serve form. last_verified left null."
---

1. Email privacy@veraset.com and state that you are requesting, under the CCPA, that Veraset not sell or share your hashed email address, mobile advertising identifier, and location data.
2. Include your name and email address, and any device/advertising-identifier information you can provide to help them locate your records (optional, but may help them process the request).
3. Note: Veraset's own privacy policy also points to an online "Do Not Sell My Personal Information" form at veraset.com/do-not-sell-my-personal-information/, but that exact URL returned a "Page Not Found" error when checked -- try it, but expect to need the email route instead.
4. If email does not get a response, you can also mail a written request to: Veraset, LLC, Attention: Data Privacy Officer, 127 S Peyton St, Suite 301, Alexandria, VA 22314.
5. Separately, review and restrict location-sharing permissions for apps on your phone, since Veraset sources location data through partner apps rather than directly from you.
