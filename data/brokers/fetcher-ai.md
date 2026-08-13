---
id: fetcher-ai
name: Tiplinks Inc
domain: fetcher.ai
category: people_search
people_search: true
tier: guided
priority: high
method: form
opt_out_url: "https://app.fetcher.ai/opt-out"
opt_out_email: "support@fetcher.ai"
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
notes: "WebFetch on fetcher.ai/privacy confirmed Fetcher (Tiplinks Inc) is an AI recruiting/candidate-sourcing platform that aggregates personal data about individuals -- name, job history, contact info, email, social profiles, education, skills -- pulled from LinkedIn/professional networks plus third-party people-data vendors (People Data Labs, FullContact, SeekOut, ContactOut, Hiretual, Hunter, SalesQL, RocketReach). This is effectively a downstream people-data aggregator on top of other brokers, so classified people_search:true. A dedicated opt-out page exists at app.fetcher.ai/opt-out with a stated 14-day processing window, and California residents can also write to support@fetcher.ai. The opt-out page itself is a JS-rendered single-page app; WebFetch could not confirm exact form fields or CAPTCHA presence, so tier set to guided and required_fields inferred conservatively (name + email, the minimum needed to identify a candidate record) rather than confirmed. last_verified left null."
---

1. Go to https://app.fetcher.ai/opt-out and submit the opt-out request with your name and email address (the page is a web app -- allow it to fully load before submitting).
2. If the opt-out page doesn't work or you prefer email, write to support@fetcher.ai and state that you are a California resident (if applicable) exercising your CCPA right to know about and opt out of the collection/sharing of your personal data, and ask to be removed from Fetcher's candidate database.
3. Note that Fetcher pulls candidate data from several other data vendors (People Data Labs, FullContact, SeekOut, ContactOut, Hunter, RocketReach, and others) -- opting out of Fetcher alone won't remove your data from those upstream sources, so consider opting out of each separately if you want broader removal.
4. Fetcher states it aims to process opt-out/access requests within 14 days.
