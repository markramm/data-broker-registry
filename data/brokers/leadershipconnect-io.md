---
id: leadershipconnect-io
name: Leadership Connect
domain: leadershipconnect.io
category: marketing_data_broker
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "https://leadershipconnect.io/opt-out/"
opt_out_email: "privacy@leadershipconnect.io"
phone: "(202) 347-7757"
captcha: true
id_required: true
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on leadershipconnect.io privacy policy confirmed: B2B data intelligence broker aggregating business-contact info on government officials, congressional staff, contractors, and other decision-makers for its 'GovConnect'/'Leadership Connect' platform. Policy describes a DSAR portal at /dsar/ and explicitly reserves the right to request 'a copy of your driver's license or other government-issued ID' for identity verification before processing requests -- id_required set true on that basis, which pushes this to guided tier despite no CAPTCHA being mentioned. Mail address (325 7th St NW, Suite 800, Washington DC 20004, Attn Chief Privacy Officer) and phone (202) 347-7757 also available as alternate channels. This is business-contact data on professionals in their work capacity, not consumer people-search, so priority is standard. Not independently re-rendered live; last_verified left null. Maintainer re-check 2026-10-26 (Fixes #39): the monitor saw /dsar/ redirect to the homepage, and today /dsar/ returned HTTP 429 to a direct fetch. The site footer's 'Do Not Sell My Personal Information' link now goes to https://leadershipconnect.io/opt-out/ (HTTP 200), which embeds a 'Request Optout' form from https://optout.leadershipconnect.io/ (HTTP 200): required Name and Email fields and a reCAPTCHA-gated Submit button, so captcha is now true (tier stays guided) and method is form. The privacy policy still says it may ask for ID before acting, so id_required stays true. The policy still lists the 325 7th St NW, Suite 800 mailing address while the site footer now shows 525 9th Street NW, Suite 600; step 5 gives both. Nothing was submitted; last_verified is null."
---

1. Go to https://leadershipconnect.io/opt-out/ (the "Do Not Sell My Personal Information" link in Leadership Connect's footer). The request form loads in a frame on that page.
2. Enter your full name and email address.
3. Click "Submit" and complete the CAPTCHA if one appears.
4. Be prepared to provide proof of identity if requested -- Leadership Connect's policy states it may ask for a photo ID, driver's license, or a recent utility/credit-card bill before processing.
5. If the form is unavailable or you prefer another channel, email privacy@leadershipconnect.io with your name and the record you want removed, call (202) 347-7757, or mail a written request to the Chief Privacy Officer, Leadership Connect, Washington, DC 20004. The privacy policy gives 325 7th St NW, Suite 800, while the site footer now shows 525 9th Street NW, Suite 600.
