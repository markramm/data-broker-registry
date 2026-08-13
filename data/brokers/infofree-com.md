---
id: infofree-com
name: "Infofree.com"
domain: infofree.com
category: marketing_data_broker
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://privacycompliance.biz/other-dbusa/"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, other]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on infofree.com confirmed it sells access to consumer and business contact databases (advertised '245 Million Consumers', '50 Million Executives with Email', '22 Million Businesses') for sales-lead generation -- a genuine marketing data broker. Legacy CSV email (bob@infofree.com) looks like a personal/sales contact rather than a privacy channel, so not used as opt_out_email. The site's own footer 'Remove My Name/Opt-Out' link points to a shared multi-brand opt-out portal (privacycompliance.biz/other-dbusa/) covering Infofree and its sibling DatabaseUSA-family brands (AtoZdatabases, Salesflower, ResearchUSA, HDML). WebFetch on that portal confirmed a form requiring only email, full name, and state (a state field, mapped here to 'other' in required_fields), no CAPTCHA visible in the fetched content, and no login. Business/consumer contact list broker rather than a people-search product built around lookups, so priority standard."
---

1. Go to the [DatabaseUSA-family privacy opt-out portal](https://privacycompliance.biz/other-dbusa/), which Infofree's own site links to as its opt-out mechanism.
2. Select Infofree (or the relevant related brand, if you're unsure which list you're in) from the portal's options.
3. Enter your full name, email address, and state, then submit the "do not sell or share" / delete request.
4. No account, login, or CAPTCHA was found on the fetched form. Since this portal also covers sibling brands (AtoZdatabases, Salesflower, ResearchUSA, HDML), consider submitting once per brand if you want full coverage.
