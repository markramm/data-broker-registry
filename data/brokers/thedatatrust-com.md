---
id: thedatatrust-com
name: Data Trust
domain: thedatatrust.com
category: political_voter_data
people_search: false
tier: guided
priority: high
method: phone
opt_out_url: "<verify: Data Trust's 'Your Privacy Choices' page (thedatatrust.com/your-privacy-choices/) links only to a general contact form, not a dedicated opt-out form -- confirm whether a real opt-out mechanism exists at that URL or elsewhere on the site>"
opt_out_email: null
phone: "855-695-5575"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Data Trust (thedatatrust.com) is a political/voter-data broker serving Republican and conservative campaigns and advocacy groups, tracking '300 million individuals with 2,500+ unique data points' per its own homepage -- a genuine, high-impact broker, though a campaign-data vendor rather than a public people-search tool. WebFetch on thedatatrust.com/privacy-policy/ confirmed a stated CCPA opt-out right exercisable via the 'Your Privacy Choices' link, phone (855-695-5575), or email; however the actual email address is Cloudflare-obfuscated in the page's HTML (rendered as an unreadable /cdn-cgi/l/email-protection token) so it could not be reliably recovered -- opt_out_email left null rather than guessing. Following the 'Your Privacy Choices' link (thedatatrust.com/your-privacy-choices/) led only to a marketing email-signup box and a 'Get Started' button pointing to a general /contact sales form (name, email, message, CAPTCHA) -- no dedicated privacy/opt-out form was found there. Given the working channel appears to be phone, method set to phone with the confirmed number; opt_out_url left as a verify-placeholder since the page linked from the privacy policy doesn't actually contain a working opt-out form, and last_verified is null per the placeholder rule."
---

1. Call Data Trust's privacy line at 855-695-5575 and state you are requesting to opt out of the sale/sharing of your personal information and/or a full deletion under CCPA (or your applicable state law).
2. Be ready to provide your full name and an email address so they can confirm the request in writing.
3. If you'd rather try in writing first, use the general contact form at thedatatrust.com/contact -- it is a sales-oriented form (not a dedicated privacy form), so explicitly state in the message field that this is a CCPA opt-out/deletion request, not a sales inquiry.
4. Data Trust states it will process opt-out requests within 15 business days -- follow up by phone if you don't hear back.
5. Note: the "Your Privacy Choices" link in the site footer did not lead to a working opt-out form as of this research (only a marketing signup and general contact button) -- phone is the most reliable confirmed channel.
