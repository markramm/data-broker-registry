---
id: truedata-co
name: TrueData
domain: truedata.co
category: adtech_data_broker
people_search: false
tier: auto
priority: standard
method: email
opt_out_url: "https://truedata.co/assets/TrueData-Advertising-Privacy-Policy.pdf"
opt_out_email: "dataprivacy@truedata.co"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email, other]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "Not to be confused with the unrelated stock-market/financial-data-feed company also called 'TrueData' (truedata.in/.tv). This truedata.co is a Texas-registered data broker (site footer states 'the entity maintaining this website is a data broker under Texas law') doing offline/identity-resolution data for digital advertising; recently acquired by ID5. WebFetch on the homepage and on /opt-out-request rendered directly (not bot-blocked): the opt-out form only requires country/state/email, with name/address/phone/mobile-ad-ID as optional fields, no CAPTCHA and no ID upload mentioned. WebFetch on /privacy-policy/ (a rendered PDF) confirmed the same opt-out URL plus a separate access/delete-request form at https://info-prod.truedata.co/access-delete-request and a privacy@truedata.co contact address for verification follow-up. Not a people-search site (no per-person profile pages found) -- classified as an adtech/marketing data broker, standard priority. tier set to assisted rather than auto because the primary documented path is the web form, not a plain email opt-out, even though the email address is also usable. 2026-11-26 maintainer update (fixes #267): the page monitor found the old form host info-prod.truedata.co unreachable for 3 runs, and today it did not connect at all. The truedata.co homepage (fetched today, HTTP 200) now carries a notice: on September 30, 2026 the TrueData audience business and brand were acquired by Cloud Technologies S.A., and the former TrueData Solutions, Inc. now operates separately as Twine Data, Inc. (twinedata.com, privacy@twinedata.com). The homepage links a new Advertising Privacy Policy PDF from TrueData Audiences LLC (Delaware). Its section 9.2 says opt-out, deletion and access requests go to dataprivacy@truedata.co, and you must include enough to identify the browser, device or advertising ID. It also says recognized opt-out preference signals are honored. No web form is linked anymore, so method changed form -> email and tier assisted -> auto, and opt_out_url now points to that policy. The old privacy@truedata.co address and the access/delete form were dropped because the new policy does not mention them. Did not email anyone or check whether the Twine Data route works. last_verified stays null."
---

1. TrueData's old opt-out web form no longer loads. Since a September 30, 2026 acquisition, TrueData Audiences LLC (part of Cloud Technologies S.A.) runs the TrueData audience data. Its Advertising Privacy Policy is at https://truedata.co/assets/TrueData-Advertising-Privacy-Policy.pdf.
2. Email dataprivacy@truedata.co. Say you are opting out of the sale and sharing of your personal information and of targeted advertising under your state's privacy law (e.g. CCPA/CPRA), and that you also want your data deleted if you wish.
3. TrueData keys its data to pseudonymous identifiers, not names. Include the email address(es) you want suppressed and, if you can, your phone's mobile advertising ID (and any connected-TV ad ID). Its policy says it may turn down requests it can't match to an identifier.
4. Turn on a browser opt-out preference signal such as Global Privacy Control. TrueData's policy says it honors these where the law requires it.
5. The company that used to be TrueData Solutions, Inc. is now a separate business, Twine Data, Inc. It may also hold older data about you. For full coverage, send the same request to privacy@twinedata.com (see https://twinedata.com).
