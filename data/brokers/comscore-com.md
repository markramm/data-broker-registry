---
id: comscore-com
name: Comscore, Inc.
domain: comscore.com
category: advertising_adtech
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.comscore.com/About/Privacy/Data-Subject-Rights"
opt_out_email: null
phone: null
captcha: false
id_required: true
phone_required: false
charges_fee: false
verification: id_upload
required_fields: [full_name, email, address]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch on comscore.com/About/Privacy confirmed comscore is a large audience-measurement/analytics data broker collecting web-tagging (ScorecardResearch/VoiceFive), panel, and survey data. Their Data Subject Rights hub at the URL above routes to separate forms depending on data type: a Tagging Data form, a combined Panel/Other Data form, and a Workday portal for job applicants; DSR@comscore.com and privacy@comscore.com are general contact emails, plus a postal address (11950 Democracy Drive, Reston, VA 20190). The page explicitly states they require completing forms 'to allow us to verify your identity before processing your request' -- id_required set true on that basis, though the exact document type was not specified. Multi-form routing + identity verification -> guided tier. Large, well-known ad-measurement broker -> priority high."
---

1. Go to https://www.comscore.com/About/Privacy/Data-Subject-Rights (or click "Do not sell my personal information" in the comscore.com footer).
2. Choose the form matching your situation: the Tagging Data form if you were tracked via ScorecardResearch/VoiceFive web tags, or the Panel/Other Data form if you were a survey or panel participant.
3. Complete the form with your full name, email, and mailing address, and select the request type (opt-out of sale, deletion, access, etc.).
4. Be prepared for an identity-verification step -- Comscore states it verifies identity before processing requests.
5. Alternatively, email DSR@comscore.com or privacy@comscore.com directly, or write to Comscore, Inc., ATTN: Privacy, 11950 Democracy Drive, Reston, VA 20190.
6. Comscore reports a median 33-day response time for substantive replies; follow up if you haven't heard back within 45 days.
