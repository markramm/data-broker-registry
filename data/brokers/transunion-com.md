---
id: transunion-com
name: Transunion
domain: transunion.com
category: identity_verification_services
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://www.transunion.com/consumerprivacy"
opt_out_email: null
phone: null
captcha: false
id_required: true
phone_required: false
charges_fee: false
required_fields: [full_name, address, email, phone, dob, ssn, gov_id]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: data-brokers-watch
notes: "WebFetch on transunion.com/consumerprivacy returned HTTP 403 (bot-blocked). Corroborated via search of TransUnion's own privacy notices and third-party opt-out guides: TransUnion is a full Credit Reporting Agency, and its consumer privacy/opt-out portal legitimately verifies identity before acting -- it may request name, address, email, phone, DOB, and either full or last-4 SSN, and for higher-sensitivity requests can require a copy of a driver's license or other government ID, knowledge-based security questions, or an SMS passcode. This is materially different from marketing data brokers: id_required and ssn/gov_id in required_fields reflect a real, documented verification step, not a speculative guess. This is separate from TransUnion's free annualcreditreport.com-style credit-freeze process, which uses lighter verification; the CCPA/CPRA privacy-rights portal is the one referenced by opt_out_url. Method changed from form to portal (a persistent authenticated account/portal flow, not a single-page form) and tier is guided given the identity-verification burden. Not freshly confirmed against a rendered page (bot-blocked) -- last_verified left null."
---

<!-- Real instructions based on TransUnion's documented CCPA/CPRA consumer-privacy request process. -->
1. Go to https://www.transunion.com/consumerprivacy and scroll to the "Your Privacy Choices" link, or find it in the site footer.
2. Choose the type of request: opt-out of sale/sharing, limit use of sensitive personal information, access, or deletion.
3. Provide your name, address, email, phone number, and date of birth so TransUnion can locate your file.
4. Be prepared to provide your Social Security number (or last four digits) and, for some requests, a photo of a government-issued ID (driver's license or state ID) -- TransUnion uses this to verify you are who you claim to be before touching a credit file.
5. You may also be asked to answer knowledge-based security questions or confirm a one-time passcode sent to your phone.
6. Submit the request online, by phone, or via the one-time paper form TransUnion provides; processing can take longer than a typical data-broker opt-out because of the added identity-verification steps.
