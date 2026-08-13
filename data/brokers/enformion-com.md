---
id: enformion-com
name: Enformion
domain: enformion.com
category: people_search
people_search: true
tier: guided
priority: crucial
method: portal
opt_out_url: "https://www.enformion.com/opt-out/"
opt_out_email: null
phone: "877-820-8125"
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: "2026-08-13"
source: "dbw+tcp-research+chrome-verified"
notes: "WebFetch on enformion.com/en/privacy/ and enformion.com/opt-out/ (the latter also directly curled but Cloudflare-blocked the curl attempt, so relying on the earlier successful WebFetch render) confirms: Enformion is a people-search/public-records data broker selling 'Data Products' for fraud protection, identity verification, investigations, and debt collection, built from public records and third-party sources. The opt-out flow starts by submitting name and email through a form; Enformion emails a link to the actual opt-out form (email-first, two-step). The form requires a reCAPTCHA checkbox ('Complete the reCAPTCHA checkbox to verify you're not a robot') -- CAPTCHA-gated pushes this to guided tier per instructions. No government ID is required, and no fee is charged. After submission, a confirmation email is also sent, and the privacy policy states 'please allow 3 days for your record to be fully removed.' A phone alternative is listed: 877-820-8125. Authorized agents can submit on a subject's behalf by providing their own name/email alongside the subject's. Important caveat stated by Enformion itself: opting out only affects Enformion's own re-display of public-records data -- the underlying public records aren't erased, and the company explicitly warns your info may reappear in future re-ingestion, consistent with people-search re-add patterns generally. Chrome-driven check (2026-08-13): PARTIAL/corrected -- the URL is correct and loads as a real page titled 'Enformion Privacy Portal.' It's a multi-purpose privacy portal, not a single opt-out form: a dropdown labeled 'Select From Available Forms' offers Right to Opt-out, Right to Delete, Right to Know, and Right to Correct as separate request types -- updated method from form to portal to reflect this. The page's own text also states it handles privacy requests 'for Enformion and our affiliated websites, including Tracers.com and Endato.com' -- worth knowing since a single Enformion opt-out request may cover those sibling sites too, though this wasn't independently tested. Did not select/submit the 'Right to Opt-out' option to avoid entering real personal data at this stage."
---

1. Go to https://www.enformion.com/opt-out/.
2. Enter your name and email address in the initial form, check the authorization confirmation checkbox, and complete the reCAPTCHA.
3. Submit the form -- Enformion will send a link to your email address that takes you to the actual opt-out form.
4. Open that emailed link and fill in the opt-out form as completely and accurately as you can; the privacy policy warns that omitted or inaccurate information will only slow down processing.
5. Submit the completed form. You'll receive a confirmation email from Enformion once the request is logged.
6. If you'd rather not use the web form, you can instead call 877-820-8125 to start the process by phone.
7. Allow about 3 days for your record to be removed from Enformion's public-facing listings. This does not delete the underlying public records Enformion draws from, so your profile can reappear later if Enformion re-ingests those sources -- plan to periodically re-check and re-submit.
8. If you're opting out on someone else's behalf as an authorized agent, include your own name and email in addition to the subject's information.
