---
id: foursquare-com
name: Foursquare
domain: foursquare.com
category: geolocation_data_broker
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://foursquare.com/data-requests"
opt_out_email: "privacy@foursquare.com"
phone: "8006730117"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [other]
verification: identity_confirm
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "Foursquare is a genuine location-data company that collects precise geolocation via its City Guide/Swarm consumer apps and licenses movement/places data to third parties (it is a member of the NAI's Precise Location Information Solution Provider program). WebFetch on foursquare.com/legal/privacy-center/ confirmed a real Privacy Center with a dedicated 'Opt-Out Page' (foursquare.com/data-requests) that requires an iOS or Android Mobile Advertising Identifier (MAID) rather than name/email -- this is a mobile-ad-ID-gated flow distinct from a normal web form, hence guided tier despite no CAPTCHA being mentioned. A Privacy Portal (Atlassian service desk) and a toll-free line (800-673-0117) exist as alternate channels for users who can't log in or don't have app access. required_fields set to [other] to reflect the MAID requirement, which isn't in the schema's enum. last_verified left null -- confirmed via WebFetch summaries, not a rendered screenshot of the live form."
---

1. If you have used Foursquare's City Guide or Swarm app, log into your account and use the in-app privacy/data controls to request access, correction, or deletion of your data -- this is the fastest path.
2. If you cannot log in, go to https://foursquare.com/data-requests to submit an opt-out of the sale/sharing of your personal data. This page asks for your device's Mobile Advertising Identifier (MAID) rather than your name -- find your iOS "Advertising Identifier" or Android "Advertising ID" in your phone's privacy settings before starting.
3. Alternatively, for deletion or access requests when you can't log in, use the Privacy Portal at https://foursquare.atlassian.net/servicedesk/customer/portal/25 and submit a support ticket describing your request.
4. You can also email privacy@foursquare.com directly with your request, or call the toll-free privacy line at (800) 673-0117.
5. Separately, use your phone's OS-level ad-tracking controls (Limit Ad Tracking / disable Advertising ID) to stop new location data from being associated with your device going forward, since Foursquare's opt-out only affects data already collected.
6. Expect identity/device verification before the request is processed; there's no published turnaround time, so follow up if you don't hear back within a few weeks.
