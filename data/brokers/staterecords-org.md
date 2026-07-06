---
id: staterecords-org
name: "State Records (United States State Records)"
domain: staterecords.org
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://staterecords.org/optout"
opt_out_email: "privacy@staterecords.org"
phone: "617-262-9317"
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, address]
readd_days: null
legal_basis: [ccpa]
last_verified: 2026-07-03
source: data-brokers-watch
notes: "Original opt_out_url pointed at a downloadable PDF form (members.staterecords.org/.../data_opt_out_form.pdf), which WebFetch could not render as text; replaced it with the live web opt-out page at staterecords.org/optout, which WebFetch fetched successfully and confirmed matches this description (first/last name + state required, city optional, submit to find records, then a separate confirmation step with email + CAPTCHA). A mail-in alternative exists (InfoPay Data Opt Out Dept, PO Box 130369, Boston, MA 02113) that DOES require a copy of state ID/passport and optionally notarization -- id_required left false here because the web/email routes do not require it; the mail route is noted as an alternative below. Judicial-personnel/family removal has a separate email path via privacy@staterecords.org."
---

<!-- Real instructions based on StateRecords.org's live web opt-out form. -->
1. Go to https://staterecords.org/optout.
2. Enter your first name, last name, and select your state (city is optional) to search for your listing.
3. Check the box next to the matching record(s) and choose "Remove Data."
4. On the confirmation screen, enter your email address and complete the CAPTCHA, then submit.
5. Check your email and confirm the removal request via the link sent to you.
6. If you're a judge, law-enforcement officer, or protected family member, you can instead email privacy@staterecords.org with subject line "Attention Covered Person Removal Request," or call 617-262-9317. A notarized mail-in option (with a copy of state ID) exists via InfoPay Inc., PO Box 130369, Boston, MA 02113, but is only necessary if the online/email routes don't resolve your case.
