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
opt_out_email: "support@okcaller.com"
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
notes: "Confirmed via WebFetch on okcaller.com homepage and okcaller.com/faq.php: OkCaller is a caller-ID/reverse-phone-lookup site publishing name-to-number listings ('Reliable, verifiable contact information', 300M+ Caller Name IDs given away) -- genuine people-search-adjacent broker, so priority crucial. The FAQ describes an SMS-based opt-out you trigger from the phone number being removed, plus CNAM blocking via your carrier as an alternative, and an escalation path (certified mail to their PO or emailing support@okcaller.com with subject 'OPTOUT FAILURE AFTER COMPLIANCE WITH TOS') if the SMS method fails. The exact SMS short code/keyword was not shown in the fetched content, so the process below is described at the level of detail confirmed; phone-verification-gated so tier guided, phone_required true. last_verified left null since no live render of the removal flow itself was captured."
---

1. Find your listing on okcaller.com by looking up your own phone number, and note the exact page URL.
2. From the phone you want removed, use OkCaller's SMS-based opt-out service (the specific short code is published on the site's FAQ/help pages) to request removal of that number's listing.
3. As an alternative or backup, contact your telecom carrier and request CNAM (Caller Name) blocking, which stops your name from being displayed by Caller ID systems including OkCaller.
4. If the SMS opt-out does not remove your listing, send a certified letter to: OkCaller.com Opt-Out, 10312 Orchid Reserve Dr, West Palm Beach, FL 33414.
5. You can also email support@okcaller.com with the subject line "OPTOUT FAILURE AFTER COMPLIANCE WITH TOS" to escalate a failed removal request.
6. Re-check your listing periodically, since caller-ID data can be re-aggregated from carrier and public sources.
