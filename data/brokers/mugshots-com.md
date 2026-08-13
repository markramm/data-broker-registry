---
id: mugshots-com
name: Mugshots.com
domain: mugshots.com
category: mugshot
people_search: true
tier: guided
priority: crucial
method: email
opt_out_url: "https://mugshots.com/record-maintenance"
opt_out_email: "mugshots.com1@gmail.com"
phone: null
captcha: false
id_required: true
phone_required: false
charges_fee: false
required_fields: [email, full_name, gov_id, other]
readd_days: null
legal_basis: [none]
last_verified: null
source: "dbw+tcp-research"
notes: "Mugshots.com is a live, major mugshot-aggregator site (confirmed via direct WebFetch of the homepage, its site-policies page, and its record-maintenance page). It republishes arrest photos/records as 'news' content and explicitly states it does not charge for removal. Removal is not general-purpose, however: WebFetch of mugshots.com/record-maintenance found the site will remove a listing only for court-ordered expungement/sealing/destruction, identity theft, or death of the subject, and will only update (not remove) listings for favorable dispositions (not guilty, dismissal, acquittal, pardon, nolle prosequi) or completed non-favorable dispositions -- all gated on submitting signed, legible court/legal documentation. Given documentation is effectively a government-issued/court record requirement, id_required is true and tier is guided despite method being email, matching the precedent set on bustedmugshots.com. Contact emails found: mugshots.com1@gmail.com (expungement/sealing/identity-theft and death cases) and docverify1@gmail.com (favorable/non-favorable disposition updates); mugshots.com1@gmail.com is used as opt_out_email since it's the general/removal-request address. The site's privacy policy (site-policies.html, dated 2013) predates CCPA and has no do-not-sell mechanism -- legal_basis is none, and this is a documentation-gated content-removal process rather than a statutory opt-out. last_verified left null since this was not rendered by a human directly."
---

1. Determine whether your case qualifies for removal: Mugshots.com will remove a listing only if the case was court-ordered sealed/expunged/destroyed, you are a victim of identity theft, or the subject is deceased.
2. If your case instead ended favorably (not guilty, dismissal, acquittal, exoneration, pardon, nolle prosequi, adjudication withheld) or you completed all obligations of a non-favorable disposition (fines paid, probation finished, time served), Mugshots.com will update -- not remove -- the listing to reflect that outcome.
3. Gather legible, signed supporting documentation: a court order of expungement/sealing/destruction, identity-theft police report, a certified death certificate, or court records showing the final disposition, as applicable.
4. For expungement, sealing, identity-theft, or death cases, email mugshots.com1@gmail.com with your full name, a link to your specific listing, your Mugshots.com ID (if you have one), and the supporting documentation attached.
5. For disposition updates instead of removal, email docverify1@gmail.com with the same information and your court disposition records.
6. Mugshots.com states it processes requests on a first-come, first-served basis with no guaranteed timeline (illustrative figure cited in third-party guides: up to 10 business days) and discards illegible documents without notifying you -- make sure scans are clear before sending.
7. Mugshots.com explicitly states it does not charge for removal or updates -- do not pay anyone claiming to expedite this on the site's behalf.
8. Because mugshot photos are frequently re-scraped and republished by other, separately operated mugshot sites, a successful removal here will not remove copies elsewhere -- each site requires its own separate request.
