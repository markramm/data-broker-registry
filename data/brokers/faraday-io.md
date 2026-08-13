---
id: faraday-io
name: Faraday, Inc.
domain: faraday.io
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://faraday.ai/privacy-options"
opt_out_email: null
phone: null
captcha: false
id_required: true
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "faraday.io redirects (308) to faraday.ai -- the company appears to have moved domains. WebFetch confirms Faraday operates the 'Faraday Identity Graph,' a predictive-marketing data product holding 1,500+ data points on ~240M US adults, making it squarely a marketing data broker. The dedicated opt-out page at faraday.ai/privacy-options is JS-rendered and WebFetch could only partially extract it: it describes a 'submit a request by entering your email below' flow but the actual form/email-input widget did not render in the fetched markdown, and the page also surfaced (possibly cached/adjacent) text about government-ID + utility-bill verification for access requests, which was not clearly scoped to opt-out specifically vs. full data-access requests. No email like ccpa@faraday.io was found live -- the legacy CSV's email is unconfirmed and NOT used here. Because the request mechanism is JS-gated and the identity-verification requirement is ambiguous, id_required set to true conservatively and tier kept guided. last_verified left null; this entry should be spot-checked by a human loading the live page."
---

1. Go to https://faraday.ai/privacy-options (Faraday's opt-out/do-not-sell page; note the company's domain appears to have moved from faraday.io to faraday.ai).
2. Enter your email address in the opt-out request field and submit, indicating you do not want Faraday to share/sell your information ("sale" under the CCPA) with its clients or other third parties.
3. Faraday's page notes it may require identity verification (potentially including a government-issued ID and a utility bill) for some request types -- be prepared to provide this if asked, though this appeared tied to full data-access requests rather than opt-out specifically.
4. As an alternative/supplemental step, use general industry opt-out tools referenced on Faraday's page: the DAA WebChoices tool, the NAI Consumer Opt-Out tool, the DAA AppChoices tool (mobile), or your device's ad-tracking settings.
5. Because this page is JavaScript-heavy and the exact form fields could not be fully confirmed, verify you're on the live faraday.ai domain before submitting, and consider following up if you don't receive confirmation.
