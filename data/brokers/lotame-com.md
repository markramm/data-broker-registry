---
id: lotame-com
name: "Lotame Solutions, Inc."
domain: lotame.com
category: adtech_identity_broker
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://legal.epsilon.com/dsr/"
opt_out_email: null
phone: "1-866-267-3861"
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email, address]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Lotame is a large B2B audience-data/identity-graph company for advertisers. WebFetch on lotame.com/privacy/ (Privacy Center) confirmed Lotame now routes consumer CCPA/GDPR privacy requests to its parent Epsilon's shared Consumer Privacy Request portal at legal.epsilon.com/dsr/ (Lotame's own privacy@lotame.com contact from the legacy CSV was not found on the live page; the portal link was the only confirmed channel), reflecting Lotame's acquisition by Publicis/Epsilon. The Epsilon portal itself (see data/brokers/epsilon-com.md, a separate broker entry for Epsilon directly) offers a country-selector Consumer Privacy Request Form plus a US phone line (1-866-267-3861); exact form fields render via JS and weren't directly visible to WebFetch. captcha:true and required_fields are carried over as inferences from the Epsilon entry's research, not independently re-observed for Lotame specifically. High priority given Lotame's scale as an identity/audience-data broker; not people-search. last_verified left null."
---

1. Go to https://legal.epsilon.com/dsr/ -- Lotame's parent company Epsilon's shared Consumer Privacy Request portal, which now handles Lotame's consumer privacy requests.
2. Select your country/region (US consumers should pick United States).
3. Fill out the Consumer Privacy Request Form with your name, email, and mailing address, specifying that your request concerns Lotame specifically (mention "Lotame" by name in any free-text field, since the portal is shared across Epsilon's brands).
4. Submit the form and complete any verification step it presents.
5. Alternatively, call 1-866-267-3861 to submit the same request by phone.
6. If acting as an authorized agent on someone else's behalf, be ready to provide written proof of your authority.
