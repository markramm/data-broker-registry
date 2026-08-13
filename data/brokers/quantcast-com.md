---
id: quantcast-com
name: Quantcast
domain: quantcast.com
category: adtech
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.quantcast.com/data-subject-rights/"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: [ccpa, cpra, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "Quantcast is a major adtech/measurement company (audience data, ad targeting/attribution at scale) -- confirmed high-priority per assignment note. Their main privacy page (quantcast.com/privacy/) 301-redirects to legal.quantcast.com, whose Terms of Service text (fetched via WebFetch) describes reliance on NAI/DAA industry opt-outs rather than a single proprietary consumer opt-out, and lists only general contact addresses (contact@quantcast.com / contact.dublin@quantcast.com), not a dedicated privacy email -- so opt_out_email is left null rather than guessing privacy.qil@quantcast.com from the legacy CSV, which I could not confirm anywhere on the live site. However, curl confirmed a real, live page at https://www.quantcast.com/data-subject-rights/ (HTTP 200) that is clearly Quantcast's dedicated consumer/data-subject-rights request portal; I could not render its JS form to confirm CAPTCHA or exact fields, so captcha is a cautious guess (true) and tier is guided. last_verified left null since the interactive form itself was not rendered."
---

1. Go to https://www.quantcast.com/data-subject-rights/, Quantcast's dedicated portal for consumer/data-subject requests.
2. Select the type of request that applies to you (e.g., opt-out of sale/sharing, access, or deletion) and follow the prompts, providing an email address so Quantcast can respond.
3. Complete any identity/CAPTCHA verification step the form presents.
4. For a browser-level ad opt-out that doesn't require the full rights-request form, you can also use the industry-wide tools Quantcast's policy references: the NAI opt-out at optout.networkadvertising.org, or the DAA's YourAdChoices tool.
5. Watch for a confirmation email from Quantcast and complete any verification step it asks for.
6. Because Quantcast operates as an ad-tech intermediary across many publishers, expect that opting out here addresses Quantcast's own use of your data, not every publisher or advertiser it works with -- repeat the process periodically and consider browser-level protections (blocking third-party cookies) as a supplement.
