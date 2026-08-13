---
id: rd-com
name: Reader's Digest (Trusted Media Brands)
domain: rd.com
category: direct_marketer
people_search: false
tier: guided
priority: standard
method: form
opt_out_url: "https://privacy.trustedmediabrands.com/privacy-request-form/"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, full_name]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "The legacy CSV's opt_out_url (rd.com/privacy-policy/article10660.html) returned HTTP 404 via curl -- that page is dead. Reader's Digest is now published under Trusted Media Brands, Inc.; rd.com's live privacy-policy page (fetched via curl with a browser UA) links to trustedmediabrands.com/ca-privacy-notice/, which links to a 'ccpa-form-ca-residents' path that itself redirects (HTTP 301, confirmed via curl -I) to https://privacy.trustedmediabrands.com/privacy-request-form/ -- a live (HTTP 200) dedicated privacy-request-form portal, confirmed via curl. I could not render the form's JS to confirm exact fields or CAPTCHA presence, so captcha is a cautious guess (true) and tier is guided rather than assisted. The customercare@rd.com email from the legacy CSV was not confirmed anywhere in the fetched CA-privacy-notice content, so opt_out_email is left null rather than reused unverified. last_verified left null."
---

1. Go to https://privacy.trustedmediabrands.com/privacy-request-form/, the centralized privacy-rights portal for Trusted Media Brands (Reader's Digest's publisher).
2. Select the request type that applies to you -- e.g., "Do Not Sell/Share My Personal Information" or a deletion/access request -- and fill in the requested fields (typically name and email).
3. Complete any verification step (which may include a CAPTCHA) the form presents.
4. Submit the form and watch for a confirmation email.
5. If the online form doesn't work or you'd rather not use it, Trusted Media Brands' California privacy notice (https://www.trustedmediabrands.com/ca-privacy-notice/) lists alternative contact channels -- check that page for a current phone or mail option.
6. Because Reader's Digest is one of several Trusted Media Brands publications, this opt-out is intended to cover the parent company's marketing data broadly, not just rd.com specifically.
