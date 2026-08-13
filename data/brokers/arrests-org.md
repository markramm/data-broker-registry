---
id: arrests-org
name: Arrests.org
domain: arrests.org
category: mugshot
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://arrests.org/remove/"
opt_out_email: "<verify: removal contact email is Cloudflare-email-protected on third-party guides, literal address not independently confirmed>"
phone: null
captcha: false
id_required: true
phone_required: false
charges_fee: false
required_fields: [listing_url, full_name, address, phone, dob, gov_id]
readd_days: null
legal_basis: [none]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch of arrests.org returned HTTP 403 (site live, actively bot-blocking). Multiple independent 2025-2026 removal guides (Incogni, Onerep, PurePrivacy, idstrong, EXPOSE, mugshotremovalservice) converge on the same mechanism: a mugshot/arrest-record aggregator organized by state; removal via a per-listing form at arrests.org/remove/?id=<RecordID> (Record ID taken from your listing's URL), where you select a removal reason (charges dropped/not adjudicated guilty, sealed/expunged, or 'remove my date of birth and address') and upload a redacted government photo ID (name/DOB/photo visible, other fields blacked out) plus supporting court documentation if applicable. An alternate email-based route is described by multiple guides but the literal address is Cloudflare-email-protected in every source found and could not be confirmed -- left as a <verify:> placeholder rather than guessed. Guides consistently state removal itself is free ('Arrests.org doesn't charge for it, but it does require photo ID verification'), but also consistently warn that paid 'expedited removal' resellers have historically marked up what should be a free process -- charges_fee left false per the site's own stated policy, with a strong do-not-pay warning in the instructions below. Processing 5-30 days. gov_id + guided tier reflect the photo-ID upload requirement; legal_basis left [none] since no CCPA/GDPR opt-out-of-sale framing was found -- this is a direct takedown-request process, not a statutory data-sale opt-out. last_verified left null."
---

1. Find your listing on arrests.org and copy the Record ID from its URL.
2. Go to the removal form, following the pattern https://arrests.org/remove/?id=<your Record ID> (replace with the ID from step 1).
3. Select the removal reason that applies to you: charges were dropped/not adjudicated guilty, the arrest was sealed or expunged, or you're only requesting removal of your date of birth and address from the listing.
4. Upload a redacted copy of a government-issued photo ID -- black out everything except your name, date of birth, and photo -- plus any supporting court documents (expungement order, disposition record) relevant to your selected reason.
5. Submit the form and allow 5-30 days for a decision; Arrests.org does not always grant removal requests and may not remove all associated data even when it does.
6. Do not pay anyone for "expedited" removal -- legitimate removal through Arrests.org's own process is free, and paid resellers offering faster removal have been reported as a markup scheme, not an official service.
7. Removing the listing here is a privacy/visibility fix only -- the underlying arrest record remains in official court and police databases until you separately expunge or seal it through the court system.

**Sensitive-data note:** this process requires uploading a (redacted) government photo ID. Only proceed if you're comfortable sharing that; there's no lower-friction alternative documented.
