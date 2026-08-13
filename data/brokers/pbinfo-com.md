---
id: pbinfo-com
name: "Pension Benefit Information, LLC"
domain: pbinfo.com
category: benefits_data_service
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://www.pbinfo.com/crf"
opt_out_email: null
phone: "1-800-327-2720"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, address, dob, ssn]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "curl-fetched pbinfo.com's California privacy notice (ca-privacy-policy) and its CCPA Consumer Request Form (pbinfo.com/crf) directly (both HTTP 200, static WordPress HTML). PBI Research Services / Pension Benefit Information, LLC works with pension plans, insurers, financial institutions, and government entities to locate people eligible for benefits and to detect fraud/overpayment to deceased individuals -- it collects and processes consumer identifiers (name, SSN, address, DOB, financial/employment info), some sourced from purchased third-party marketing lists and government/obituary records, as a service provider to its clients. It is not a classic resale broker (contracts reportedly prohibit resale/further sharing per the fetched policy) and is not a people-search consumer product, but it directly holds and processes consumer PII and offers its own CCPA request channel, so people_search is set false and priority high rather than crucial. The legacy source's CCPARequests@pbinfo.com email address was NOT found anywhere on the live pages fetched this session (privacy policy, CA privacy notice, or the CRF form) -- do not treat that address as confirmed; the only channels the current site itself offers are the web form at pbinfo.com/crf and phone 1-800-327-2720. The CRF form (fetched directly) requires: full name, zip code, date of birth, and the LAST 4 DIGITS of SSN to verify identity, plus request type (access/portability/deletion) and contact preference -- no CAPTCHA appeared in the fetched HTML, but the SSN-fragment + DOB requirement is a meaningful identity-verification bar, so tier is guided rather than assisted. required_fields includes ssn because the last-4-digits requirement will trip the frontend's sensitive-data guardrail, which is appropriate here. Not independently re-verified beyond this session's fetch; last_verified left null."
---

1. Go to PBI's CCPA Consumer Request Form at https://www.pbinfo.com/crf.
2. Enter your first and last name, zip code, date of birth, and the last 4 digits of your Social Security number -- PBI needs these to verify your identity against records it may hold about you.
3. Choose the type of request: access to specific information, a data portability request, or a deletion request.
4. Describe your request in the details field, and provide your preferred contact method (email or mailing address) for PBI's response.
5. Submit the form. You're limited to two access/portability requests within any 12-month period.
6. If you'd rather not use the web form, call PBI directly at 1-800-327-2720 and provide the same identifying information by phone.
7. Be aware PBI works on behalf of pension plans, insurers, and employers to locate people owed benefits or to detect overpayment fraud -- opting out or requesting deletion may make it harder for a former employer, pension plan, or union to find and pay you benefits you are owed, so consider this tradeoff before submitting a deletion request.
