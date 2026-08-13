---
id: dogpile-com
name: Dogpile
domain: dogpile.com
category: search_engine_adtech
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "https://system1.com/terms/privacy-policy/privacy-inquiries"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Prior pass found System1 (Dogpile's parent/operator) has real CCPA sale/opt-out language but couldn't confirm the exact URL applied to Dogpile specifically. Fetched dogpile.com directly this round: its own footer links to https://system1.com/terms/privacy-policy (confirmed via curl on the raw homepage HTML -- Dogpile links to System1's policy as its own, resolving the prior ambiguity). Fetched that policy and found it explicitly embeds a privacy-inquiries link: https://system1.com/terms/privacy-policy/privacy-inquiries -- this is System1's actual CCPA/consumer-rights request entry point (referenced directly in the policy text, not third-party guesswork). The privacy-inquiries page itself returned HTTP 200 but its form content is JS-rendered (the page's CSP references *.formstack.com, indicating a Formstack-embedded form) so I could not directly confirm CAPTCHA/ID/phone gating from the fetched HTML -- tier:guided reflects that uncertainty rather than a confirmed hard gate. people_search:false -- Dogpile is a metasearch engine, not an identity/address lookup reseller; the CCPA sale language in System1's policy concerns ad-tech/browsing data broadly, not people-search profiles. priority:standard given it's a real, working consumer opt-out but not personal-safety-critical people-search data. last_verified left null since the form itself was not directly rendered."
---

1. Go to https://system1.com/terms/privacy-policy/privacy-inquiries -- this is the consumer privacy-rights request page linked from Dogpile's own privacy policy (Dogpile is operated by System1 and links to System1's policy as its own).
2. Locate the "Do Not Sell or Share My Personal Information" / privacy-inquiries submission form on that page.
3. Fill in your contact details (name and email) and specify that your request concerns Dogpile.com and System1's ad-tech data practices.
4. Submit the request and watch for a confirmation email; the policy states requests are handled per California (CCPA) consumer-rights timelines.
5. If the form doesn't load or you can't confirm submission, System1's main privacy policy page (https://system1.com/terms/privacy-policy) lists the same request channel -- check there for any updated contact instructions.
