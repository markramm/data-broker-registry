---
id: peopledatalabs-com
name: "People Data Labs"
domain: peopledatalabs.com
category: data_enrichment
people_search: false
tier: assisted
priority: high
method: form
opt_out_url: "https://www.peopledatalabs.com/do-not-sell-or-share"
opt_out_email: "privacy@peopledatalabs.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "peopledatalabs.com's marketing site is a JS-rendered SPA (curl/WebFetch both return only the page title on most routes), but its public sitemap.xml (fetched directly, HTTP 200) lists an explicit https://www.peopledatalabs.com/do-not-sell-or-share page, confirming the URL is real and current rather than guessed. Raw HTML source of that page (fetched via curl) contains form input placeholders 'Full Name*' and 'Email*', confirming those two fields are required; no CAPTCHA markup was found in the raw source. People Data Labs is a well-known B2B identity-resolution / data-enrichment provider that supplies profile data (name, employment, contact info, social profiles) to other companies' platforms -- a genuine data broker, but not a consumer-facing people-search product (people_search: false). opt_out_email (privacy@peopledatalabs.com) is carried over from the legacy source data and was NOT independently re-confirmed on any page successfully rendered this session (the SPA blocked static confirmation) -- flagged here as likely-correct given it matches PDL's known standard privacy-contact convention, but treat with a bit more caution than the do-not-sell-or-share URL, which was directly confirmed via sitemap+raw-HTML. No CAPTCHA/ID found -> tier assisted rather than guided. Not independently re-verified beyond this session's fetch; last_verified left null."
---

1. Go to https://www.peopledatalabs.com/do-not-sell-or-share.
2. Enter your full name and email address in the form and submit -- the page states "Once you submit this form, we will no longer sell your personal information."
3. If the form is unavailable or you prefer email, send your opt-out/deletion request to privacy@peopledatalabs.com instead, including your full name and any details (e.g. LinkedIn URL, employer) that would help them locate your profile in their database.
4. Watch for a confirmation reply; People Data Labs' scope is B2B data enrichment (selling profile data to other companies' platforms) rather than a public search tool, so there's no separate consumer-facing listing to check afterward.
