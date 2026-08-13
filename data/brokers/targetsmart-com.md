---
id: targetsmart-com
name: TargetSmart
domain: targetsmart.com
category: political_voter_data
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://targetsmart.com/general/opt_out"
opt_out_email: null
phone: "1-888-678-6880"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, address, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "TargetSmart is a well-known political/voter-data broker serving campaigns and advocacy groups with voter files and consumer data enrichment -- confirmed via its own privacy center. WebFetch on targetsmart.com/privacy-policy/ (redirects to privacy.targetsmart.com) confirmed the site directs consumers to a 'Consumer Privacy Webform' at /general/opt_out requiring full name, current residence address, and current email, and explicitly states EMAIL REQUESTS ARE NOT ACCEPTED for privacy-rights purposes -- webform or phone (1-888-678-6880) are the only two channels. A direct WebFetch of the opt_out page itself returned 404 (likely a JS-routed SPA path not resolvable outside the app), so exact form mechanics/CAPTCHA weren't independently confirmed; kept guided out of caution even though no CAPTCHA was reported on the privacy-center page's description. Not flagged people_search since it's a political-data/analytics vendor rather than a public individual-lookup site, but the personal-address data footprint is real, hence high priority. last_verified left null."
---

1. Go to TargetSmart's Consumer Privacy Webform, linked from its Privacy Center at https://privacy.targetsmart.com/ (currently at https://targetsmart.com/general/opt_out).
2. Enter your full name, your current residential address, and a current email address -- TargetSmart states it cannot process a request without all three.
3. Specify that you are requesting opt-out/deletion of your personal information under CCPA.
4. Submit the form and watch for any follow-up confirmation, which TargetSmart says may arrive by U.S. mail as well as email.
5. If you prefer not to use the web form, call 1-888-678-6880 -- TargetSmart states this is the only other channel it accepts (it does not accept plain emailed requests).
