---
id: pulsepoint-com
name: PulsePoint, Inc.
domain: pulsepoint.com
category: adtech
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.pulsepoint.com/legal/customer-opt-out"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: []
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirmed via curl (server-rendered HTML) that pulsepoint.com is a healthcare/programmatic adtech marketing platform, not a people-search site. legal.quantcast.com-style legal hub at pulsepoint.com/legal/website-privacy-policy links to https://www.pulsepoint.com/legal/opt-out, which itself redirects (HTTP 301, confirmed via curl -I) to https://www.pulsepoint.com/legal/customer-opt-out -- fetched that page and confirmed real body text describing CCPA/CPRA 'selling,' 'sharing,' and 'targeted advertising' opt-out choices, plus a device-level opt-out link and a OneTrust-hosted privacy request webform elsewhere on the legal hub. Contact emails dataprivacy@pulsepoint.com and info@pulsepoint.com also confirmed present in the fetched HTML. No CAPTCHA/ID observed in the static HTML, but the actual opt-out control is likely a client-side toggle/cookie mechanism (curl could not render it), so left as guided rather than assisted/auto out of caution. last_verified left null since I did not render the live interactive control."
---

1. Go to https://www.pulsepoint.com/legal/customer-opt-out.
2. Read the page's description of what PulsePoint considers "selling," "sharing," and "targeted advertising," then use the opt-out control described there to disable those uses for your browser/device.
3. If you want opt-outs to apply across your devices (not just the current browser), also visit the industry-wide tools linked from PulsePoint's privacy policy: the NAI opt-out at optout.networkadvertising.org and the DAA's YourAdChoices tool.
4. For a broader access/correction/deletion request (not just an ad opt-out), email dataprivacy@pulsepoint.com with your request and enough detail (name, and if known, the PulsePoint cookie/device context) for them to locate your data.
5. If you're contacting PulsePoint about being removed from a client's marketing list rather than their own ad platform, use info@pulsepoint.com instead, as their privacy policy directs.
6. Keep a copy of any confirmation you receive; re-apply device-level opt-outs if you clear cookies or switch browsers, since cookie-based opt-outs don't persist across resets.
