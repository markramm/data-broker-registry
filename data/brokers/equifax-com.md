---
id: equifax-com
name: "Equifax Information Services LLC"
domain: equifax.com
category: credit_bureaus
people_search: false
tier: assisted
priority: high
method: portal
opt_out_url: "https://myprivacy.equifax.com/opt-in-opt-out/personal-info/"
opt_out_email: null
phone: "1-866-295-6801"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, address, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Fetched myprivacy.equifax.com/opt-in-opt-out/personal-info/ and equifax.com/personal/my-privacy/ (via curl, since WebFetch only returned the SPA shell) and equifax.com/privacy/ directly. This entry covers Equifax's OWN CCPA rights portal, which is distinct from two other things this repo/users should not conflate it with: (1) optoutprescreen.com -- the free FCRA/FACTA-mandated joint-bureau opt-out for prescreened credit/insurance offers, already its own separate entry at data/brokers/optoutprescreen-com.md; and (2) a security freeze/lock on your credit report, which restricts access to your file for new credit but is a separate product from the CCPA opt-out. Equifax's Privacy Preference Center at the myprivacy.equifax.com URL lets a consumer, without creating an account: (a) exercise Right to Know/Access, Right to Delete, and Right to Correct on personal info Equifax holds, and (b) exercise Right to Limit Use, Right to Opt-Out (stop Equifax selling/sharing personal info to third parties), and Right to Opt-In. The page states requests are free of charge, no account is required, but the consumer must supply personal information to complete the request, and standard requests are completed within 45 days per applicable law. A phone alternative is offered for consumers 18+: 1-866-295-6801 (Consumer Care, 9am-9pm ET Mon-Fri, 9am-6pm ET Sat/Sun). Separate downloadable mail-in forms exist for requests made on behalf of a minor, an incapacitated adult, or by an authorized agent. Equifax's main privacy.equifax.com hub also discloses it is a registered data broker under Texas law. No CAPTCHA or government-ID upload was described in the portal-overview text fetched; the portal is a guided multi-step flow (choose Right to Know/Delete/Correct vs. Right to Limit/Opt-Out/Opt-In, then a form) rather than a single click, so tier is assisted rather than auto, but nothing in the fetched text indicates ID-gating or CAPTCHA, so it stops short of guided. priority set to high per instructions (real financial-privacy stakes, distinct from the personal-safety/doxxing risk that drives crucial for people-search sites). required_fields is a reasonable inference (name, address, email to identify the requester and receive the confirmation/report) since the exact field-by-field form wasn't rendered for this session; treat as provisional."
---

1. Go to Equifax's Privacy Preference Center at https://myprivacy.equifax.com/opt-in-opt-out/personal-info/ -- no account or login is required.
2. Choose the request type: use "Right to Know/Access, Right to Delete, and Right to Correct" if you want to see, delete, or fix personal information Equifax holds, or use "Right to Limit Use, Opt-Out, and Opt-In" if you specifically want Equifax to stop selling or sharing your personal information with third parties.
3. Follow the guided form, supplying your name, address, and contact information so Equifax can locate your record and respond to you -- there is no fee for any of these requests.
4. If you'd rather not do this online, call Equifax Consumer Care at 1-866-295-6801 (9 a.m.-9 p.m. ET Monday-Friday, 9 a.m.-6 p.m. ET Saturday-Sunday) and make the request by phone.
5. If you're acting as a parent/guardian for a minor, on behalf of an incapacitated adult, or as an authorized agent, download and mail in the corresponding form linked from the same Privacy Preference Center page instead of using the online flow.
6. Expect your request to be completed within about 45 days; you'll see an on-screen confirmation after submitting, and if you requested to view your data you'll be notified separately when your Right to Know report is ready.
7. This CCPA opt-out is separate from two other Equifax tools you may also want: the free federal prescreen opt-out at optoutprescreen.com (stops pre-approved credit/insurance offer mailings from all four bureaus) and a security freeze on your Equifax credit report (restricts new-credit access to your file) -- neither is a substitute for the other.
