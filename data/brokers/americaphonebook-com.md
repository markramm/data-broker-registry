---
id: americaphonebook-com
name: "America Phone Book"
domain: americaphonebook.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://www.americaphonebook.com/contact.php"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: ["phone", "other"]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Legacy CSV had only a 'privacyduck.com' source_url. Direct WebFetch of americaphonebook.com/contact.php returned HTTP 403 (bot-blocked), so process is reconstructed from consistent third-party guide descriptions (DeleteMe, Optery, Atlas Privacy, GuaranteedRemovals): a removal-request form asking for the listed phone number and zip code, no CAPTCHA mentioned by these guides. This is a reverse-phone-lookup / people-search site publishing names tied to phone numbers and addresses -- real personal-safety stakes -- so priority is crucial despite the simple form, per the rule that people-search sites default to crucial. required_fields uses 'phone' plus 'other' for zip code since zip isn't in the field enum. Not independently confirmed against the live page; last_verified left null."
---

1. Go to [americaphonebook.com/contact.php](https://www.americaphonebook.com/contact.php).
2. Enter the phone number associated with your listing and your zip code in the removal request form.
3. Submit the form; a confirmation notice should appear on screen acknowledging the request.
4. Removal is reported to typically take anywhere from 24-48 hours up to 5-7 business days.
5. If you have multiple listings (different numbers or addresses), repeat this process separately for each one, since removing one listing does not clear others.
