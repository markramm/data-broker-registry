---
id: myspace-com
name: Myspace
domain: myspace.com
category: social_media
people_search: false
tier: auto
priority: standard
method: email
opt_out_url: "https://myspace.com/pages/privacy?page=do-not-sell"
opt_out_email: "compliance@support.myspace.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, full_name, phone]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Myspace is not dead -- it is still live and operating (confirmed via direct curl of myspace.com, HTTP 200, 'Featured Content on Myspace' branded as 'part of the People / Entertainment Weekly Network'), now positioned as a music/entertainment content site with user profiles rather than the general-purpose social network it was in the 2000s-2010s. It still holds user account data, so a CCPA opt-out remains relevant, but scope is narrower than a classic social-media privacy risk. Direct curl of myspace.com/pages/privacy?page=do-not-sell (the actual footer-linked 'Do-Not-Sell My Personal Information' page -- the assigned domain's eeaprivacy URL turned out to be the general EEA/GDPR notice, not the CCPA one) returned the real notice text: California residents can opt out of 'Sale' of personal information either via a CCPA Request Web Portal at https://ccpa.myspace.com/ or by emailing compliance@support.myspace.com with name, email address, and phone number. Since the plain-email path requires no login/form/CAPTCHA, this is tier auto per the schema's method:email-implies-tier:auto rule, even though a self-service portal also exists as an alternative. people_search is false -- Myspace does not resell identity/address lookups, it's a social/content platform. priority is standard given its now-niche reach and that this is an ad-targeting/data-sale opt-out, not an account/content deletion mechanism. last_verified left null since this was fetched via curl, not rendered/confirmed as a human would see it in-browser."
---

1. Go to Myspace's [Do-Not-Sell My Personal Information notice](https://myspace.com/pages/privacy?page=do-not-sell) (linked in the site footer under "Do-Not-Sell My Personal Information").
2. To opt out online, follow the link to the CCPA Request Web Portal at https://ccpa.myspace.com/ and complete the request there.
3. Alternatively, skip the portal and email compliance@support.myspace.com directly, including your name, email address, and a telephone number where you can be reached.
4. If you are submitting the request through an authorized agent rather than yourself, be prepared to provide written permission for the agent to act on your behalf -- Myspace states it may verify such requests directly with you.
5. This opt-out stops the sale/sharing of your personal information for advertising purposes; it does not delete your Myspace account or content. If you want your account and profile data removed entirely, use Myspace's account-deletion settings separately (not covered by this opt-out).
