---
id: checkpeople-com
name: CheckPeople
domain: checkpeople.com
category: people_search
people_search: true
tier: assisted
priority: crucial
method: form
opt_out_url: "https://checkpeople.com/opt-out"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: [ccpa]
last_verified: "2026-07-29"
source: badbool
notes: "WebFetch on checkpeople.com/opt-out loaded successfully and rendered a single-field suppression form (email only) with a Terms/Privacy checkbox. No CAPTCHA, no listing URL, no name/DOB field on this form itself, contrary to some older third-party guides describing a separate full-name+birthdate step. There is also a distinct 'Right to Know' pre-step at checkpeople.com/privacy-rights (requires name+email) for requesting a copy of what CheckPeople holds on you, but it is not required to complete the opt-out -- noted below as optional context, not a required field."
---

1. Go to the [CheckPeople opt-out page](https://checkpeople.com/opt-out).
2. Enter the email address you want CheckPeople to associate with your suppression request.
3. Check the box agreeing to the Terms of Service and Privacy Policy, then submit the form.
4. Watch your inbox for a verification email from CheckPeople and click the confirmation link inside it -- the request is not applied until you confirm.
5. Optional: if you also want to see what CheckPeople has on file about you before or after opting out, submit a separate "Right to Know" request at [checkpeople.com/privacy-rights](https://checkpeople.com/privacy-rights) (requires your name and email); this is informational and not required for the opt-out itself.
6. Re-check periodically -- people-search sites re-ingest public records, so a listing can reappear months later.
