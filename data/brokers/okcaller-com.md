---
id: okcaller-com
name: OkCaller.com
domain: okcaller.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://okcaller.com/faq.php"
opt_out_email: "info@okcaller.com"
phone: null
captcha: false
id_required: false
phone_required: true
charges_fee: false
verification: sms_confirm
required_fields: [listing_url, phone]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirmed via WebFetch on okcaller.com homepage and okcaller.com/faq.php: OkCaller is a caller-ID/reverse-phone-lookup site publishing name-to-number listings ('Reliable, verifiable contact information', 300M+ Caller Name IDs given away) -- genuine people-search-adjacent broker, so priority crucial. The FAQ describes an SMS-based opt-out you trigger from the phone number being removed, plus CNAM blocking via your carrier as an alternative, and an escalation path (certified mail to their PO or emailing support@okcaller.com with subject 'OPTOUT FAILURE AFTER COMPLIANCE WITH TOS') if the SMS method fails. The exact SMS short code/keyword was not shown in the fetched content, so the process below is described at the level of detail confirmed; phone-verification-gated so tier guided, phone_required true. last_verified left null since no live render of the removal flow itself was captured. 2026-11-23 maintainer update (Fixes #259): the page monitor snapshot of okcaller.com/faq.php taken 2026-11-22 (now served from www.okcaller.com) shows a rewritten opt-out FAQ. You now open your number's listing, choose SMS or phone-call verification, request a PIN, and enter the PIN on the website to finish the opt-out. The certified-mail address and the 'OPTOUT FAILURE AFTER COMPLIANCE WITH TOS' email subject are gone. If verification fails, the FAQ now says to email info@okcaller.com with the listing address and a description of the error, and not to email the PIN. support@okcaller.com is still listed for general questions. Carrier CNAM settings are still mentioned, with a caveat that they may not remove every directory listing. opt_out_email moved to info@okcaller.com; verification stays sms_confirm (a PIN by text or call). A live re-fetch on 2026-11-23 got HTTP 429, so this rests on the monitor snapshot. The listing-page flow was not walked through; last_verified stays null."
---

1. Look up your own phone number on okcaller.com and open that number's listing page. Note its exact URL.
2. On the listing page, start the opt-out and choose SMS or phone-call verification. Only do this for a number you control.
3. OkCaller sends a PIN to that number. Enter the PIN on the website to finish removing or updating the listing. Keep the PIN private.
4. If verification fails, email info@okcaller.com with the listing's URL and a description of the error. Don't include the PIN or any password.
5. You can also ask your phone carrier about its caller-name (CNAM) settings. OkCaller notes this may not remove every directory listing or records already saved.
6. Re-check your listing from time to time, since caller-ID data can be re-aggregated from carrier and public sources.
