---
id: fetcher-ai
name: Tiplinks Inc
domain: fetcher.ai
category: people_search
people_search: true
tier: guided
priority: high
method: form
opt_out_url: "https://juicebox.ai/privacy-center"
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
notes: "WebFetch on fetcher.ai/privacy confirmed Fetcher (Tiplinks Inc) is an AI recruiting/candidate-sourcing platform that aggregates personal data about individuals -- name, job history, contact info, email, social profiles, education, skills -- pulled from LinkedIn/professional networks plus third-party people-data vendors (People Data Labs, FullContact, SeekOut, ContactOut, Hiretual, Hunter, SalesQL, RocketReach). This is effectively a downstream people-data aggregator on top of other brokers, so classified people_search:true. A dedicated opt-out page exists at app.fetcher.ai/opt-out with a stated 14-day processing window, and California residents can also write to support@fetcher.ai. The opt-out page itself is a JS-rendered single-page app; WebFetch could not confirm exact form fields or CAPTCHA presence, so tier set to guided and required_fields inferred conservatively (name + email, the minimum needed to identify a candidate record) rather than confirmed. Update 2026-10-21 (daily maintainer, issue #94): the page monitor found app.fetcher.ai/opt-out unreachable on 3 runs in a row, and a WebFetch on 2026-10-21 got HTTP 503 from it. The fetcher.ai homepage still loads. It now says Juicebox has acquired Fetcher's assets, and its footer 'Opt Out' link (under Support) points to https://juicebox.ai/privacy-center, so opt_out_url now points there. That privacy center is Juicebox App, Inc.'s general request form: access, deletion, correction, and opt-out of sale/sharing/targeted ads, with an authorized-agent option. Juicebox says it will contact the requester to verify identity. The fetched page does not mention Fetcher, and its exact form fields could not be read. fetcher.ai/privacy still names app.fetcher.ai/opt-out and support@fetcher.ai, so support@fetcher.ai stays as the email fallback. Nothing was submitted; last_verified stays null."
---

1. Fetcher's assets have been acquired by Juicebox, and the fetcher.ai footer's "Opt Out" link now goes to Juicebox's privacy center. Go to https://juicebox.ai/privacy-center.
2. Choose the request you want: opt out of sale/sharing, or deletion. Say that your data may be in Fetcher's candidate database, and give your name and the email address(es) a recruiter might have for you.
3. Juicebox says it will contact you to verify your identity before it acts on the request. Reply to that message, and share only what it asks for.
4. If the privacy center doesn't work, or you want to reach Fetcher directly, email support@fetcher.ai. Say you are exercising your right (under the CCPA, if you're a California resident) to opt out and to have your profile removed from Fetcher's candidate database. Fetcher's own privacy statement promises a reply within 30 days for rights requests.
5. Fetcher pulled candidate data from several other vendors (People Data Labs, FullContact, SeekOut, ContactOut, Hunter, RocketReach and others). Opting out here won't remove your data from those upstream sources, so opt out of each one separately if you want broader removal.
