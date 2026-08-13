---
id: publicseek-com
name: PublicSeek
domain: publicseek.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "<verify: confirm exact opt-out path on atom.com for the PublicSeek brand -- /optout 404s and profile pages are bot-blocked (403)>"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "publicseek.com (302) redirects to https://www.atom.com/name/PublicSeek -- PublicSeek is a people-search profile-page brand operated by Atom.com, a known people-search/background-check company. Atom.com's own privacy policy (atom.com/legal/privacy, fetched via curl) points consumers to industry opt-outs (NAI/DAA) and lists service@atom.com as a contact, but I could not locate or confirm Atom's dedicated per-profile removal form: /optout returns 404 and profile pages return 403 (bot-blocked) to both WebFetch and curl with a browser UA. Given this is a live, active people-search product, marked crucial/guided rather than dropped, but the opt-out URL is left as a verify-placeholder and last_verified is null since I could not render the real removal flow."
---

1. Search your name at atom.com (the parent site behind the PublicSeek brand) and locate any profile matching you; copy that profile's exact URL.
2. Look for a "Do Not Sell My Info," "Remove My Info," or "CCPA / Privacy Rights" link in the atom.com site footer or on the profile page itself.
3. If a self-service removal form is available, submit the profile URL and a valid email address, and complete any CAPTCHA shown.
4. If no self-service form can be found, email service@atom.com with the profile URL, your name, and a request to remove your PublicSeek/Atom.com listing under CCPA "Do Not Sell/Share My Personal Information."
5. Watch for a confirmation email and follow any verification link it contains.
6. Re-check periodically, since people-search sites regularly re-ingest public records and profiles can reappear.
