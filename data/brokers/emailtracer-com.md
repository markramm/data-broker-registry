---
id: emailtracer-com
name: "EmailTracer"
domain: emailtracer.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://infotracer.com/optout/"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: ["full_name", "email"]
readd_days: null
legal_basis: []
last_verified: null
source: "data-brokers-watch + tcp-research"
notes: "emailtracer.com itself did not resolve (DNS NXDOMAIN) from this session despite having live AWS Route53 NS delegation, and WebFetch to infotracer.com/optout/ was rate-limited ('requested too many times') rather than cleanly blocked -- so this reads as bot/rate-limiting infrastructure rather than a dead site. Multiple independent 2026 removal guides (OneRep wiki, PurePrivacy, DeleteMe, meprism, eraseme.app) consistently and specifically identify EmailTracer as owned/operated by InfoTracer and describe the same removal mechanism: go to infotracer.com, click 'Remove my Data,' enter first/last name and state, provide an email, solve a CAPTCHA, submit, then confirm via emailed link; typical processing 3-7 business days. This matches the pattern already confirmed for criminalpages.com (also InfoTracer-family, same members.<domain> URL convention). Treating as guided given the CAPTCHA gate. last_verified left null because I could not personally render either emailtracer.com or the infotracer.com/optout/ form in this session -- based on guide consensus, not direct confirmation."
---

1. EmailTracer is operated by InfoTracer, so the working removal path is through InfoTracer's own opt-out portal rather than emailtracer.com directly.
2. Go to [infotracer.com](https://infotracer.com/) and click "Remove my Data" (or go directly to [infotracer.com/optout/](https://infotracer.com/optout/)).
3. Enter your first and last name and select your state, then enter an email address (consider using a masked/alias email).
4. Solve the CAPTCHA and submit the form.
5. Check your email for a confirmation message and click the confirmation link -- the removal isn't final until you confirm.
6. Processing typically takes 3-7 business days; since InfoTracer re-ingests public records, expect to need to repeat this periodically, and note that removal from EmailTracer doesn't remove you from other, unrelated data brokers.
