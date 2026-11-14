---
id: opensend-com
name: "Opensend Inc."
domain: opensend.com
category: identity_resolution
people_search: false
tier: auto
priority: high
method: email
opt_out_url: "https://www.opensend.com/privacy-policy"
opt_out_email: "privacy@opensend.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Authored 2026-11-05 by the daily maintainer from California's data broker registry (Opensend Inc, listing privacy@opensend.com and opensend.com/privacy-policy). I fetched https://www.opensend.com/privacy-policy (HTTP 200). Opensend's clients install its scripts and pixels on their websites, and the policy says Opensend uses the visit data to identify visitors and their contact information (such as email address), working with marketing partners and data brokers. So it is an identity-resolution / visitor-identification broker, not people-search: priority high. The policy has no web form, portal or opt-out link. Its 'Your State Privacy Rights' section lists California among the states whose residents can opt out of sales and targeted advertising and request access or deletion, and says to send all such requests to privacy@opensend.com. That is a plain email route, so method email and tier auto. required_fields [email, full_name] is our judgment: the policy doesn't say what identifies you, and the email address you want suppressed is the main key Opensend matches on. The policy describes no verification step. last_verified null."
---

Opensend identifies visitors to its clients' online stores and matches them to email addresses for marketing. Its only opt-out channel is email.

1. Send an email to privacy@opensend.com with the subject "Opt-out of sale/sharing and deletion request".
2. In the body, say that you are opting out of the sale and sharing of your personal information and of its use for targeted advertising, and that you also want your personal information deleted. Include your full name and every email address you want suppressed. If you live in California or another state with a privacy law, say so.
3. Opensend says it keeps a minimal suppression record after an opt-out so it can honor your request. That is expected.
4. Keep a copy of your email. If you don't hear back within 45 days, send a follow-up to the same address and mention your original request date.
