---
id: mylife-com
name: MyLife
domain: mylife.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.mylife.com/privacyrequest"
opt_out_email: "privacy@mylife.com"
phone: "(888) 704-1900"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, address, dob, listing_url, other]
readd_days: null
legal_basis: [ccpa]
last_verified: "2026-08-13"
source: badbool+chrome-verified
notes: "Direct WebFetch of mylife.com/privacyrequest returned HTTP 403 (bot-blocked) in this session. Cross-checked against multiple independent 2026 guides (Surfshark, OneRep, Incogni, Security.org, LegalClarity, Reputation Rhino) that consistently confirm: no account creation or driver's-license upload is actually required to opt out (the site does push an account-registration popup as a dark pattern -- decline it), the web form at /privacyrequest is the primary path, email to privacy@mylife.com and phone to 888-704-1900 (M-F 6am-5pm PT) are genuine alternatives (not fallback-only), and processing takes roughly 14 business days. id_required and phone_required are both false since neither is actually mandatory through the form/email path -- set guided tier because of the aggressive upsell dark patterns and multi-step, slow-turnaround process, not a hard ID/phone gate. Chrome-driven check (2026-08-13): URL and page title confirmed correct. The page rendered blank in the automated Chrome-extension browsing environment used for the first check, but a human confirmed it renders normally in their own regular Chrome browser and pasted the actual rendered form content back: 'DELETION AND OPT OUT OF SALE OF PERSONAL INFORMATION' -- fields are State*, First/Last Name*, City/Postal Code*, Email*, Birth Year (YYYY)* ('helps us locate your correct profile'), Middle Initial (optional), Maiden Name or Alias Name (optional), and an optional profile-listing URL field. This is meaningfully more fields than the previously-documented full_name/email/address -- updated required_fields to include dob (birth year), listing_url, and other (state/city/zip) accordingly. No CAPTCHA mentioned in the pasted content, consistent with captcha:false above."
---

1. Go to the [MyLife privacy request page](https://www.mylife.com/privacyrequest).
2. If a "create a free account" or similar signup popup appears, decline it (look for a "continue without account" or close option) -- you do not need an account to submit this request.
3. Fill in the required fields: State, First/Last Name, City and Postal/Zip Code, Email, and Birth Year (used to match you to the correct profile among similarly-named people). Optionally add your Middle Initial, a Maiden Name/Alias, and the specific profile-listing URL if you have it -- these help MyLife find the right record faster but aren't strictly required.
4. Submit the form.
5. Watch your email for a confirmation message from MyLife and click the verification link -- the request does not proceed until you confirm. MyLife will also unsubscribe and delete any account registered under that email.
6. Alternative paths if the form gives you trouble: email privacy@mylife.com with your full name and profile details, or call (888) 704-1900 (Mon-Fri, 6am-5pm PT) and ask for your Reputation Profile to be deleted -- request a confirmation number if you call.
7. Allow up to 14 business days for removal; if nothing has changed by then, follow up by phone with any confirmation number you were given.
