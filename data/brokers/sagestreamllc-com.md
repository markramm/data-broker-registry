---
id: sagestreamllc-com
name: "SageStream, LLC"
domain: sagestreamllc.com
category: credit_and_identity_data
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://consumer.risk.lexisnexis.com/opt"
opt_out_email: null
phone: null
captcha: false
id_required: true
phone_required: false
charges_fee: false
required_fields: [full_name, address, dob, ssn, gov_id]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "SageStream LLC is a nationwide consumer reporting agency (credit reports/scores supplied to card issuers, retailers, wireless carriers) under FCRA, and is now part of LexisNexis Risk Solutions -- WebFetch on sagestreamllc.com surfaced links into the same consumer.risk.lexisnexis.com portal used by risk.lexisnexis.com (also in this batch): consumer report request (/consumer), security freeze (/freeze), opt-out of prescreened credit/insurance offers (/opt), file dispute, and identity-theft blocking. Because SageStream is an FCRA consumer-reporting agency rather than a marketing-data broker, the most relevant consumer action is usually a security freeze (blocks new-account access to your file) and/or opting out of prescreened offers, both of which require identity verification (name, address, DOB, plus SSN or government ID) consistent with FCRA requirements. required_fields/id_required mirror the sibling risk-lexisnexis-com.md entry since it is the same verification backend. This is treated as a distinct entry from risk-lexisnexis-com.md because SageStream is a separately named, separately regulated (FCRA) legal entity with its own consumer-facing product set (freeze, dispute, blocking) even though the portal infrastructure is shared. last_verified left null; captcha not confirmed either way."
---

1. Go to the LexisNexis Risk Solutions consumer portal, which SageStream (now part of LexisNexis Risk Solutions) uses for consumer requests: https://consumer.risk.lexisnexis.com/opt to opt out of prescreened credit/insurance offers, or https://consumer.risk.lexisnexis.com/freeze to place a security freeze on your SageStream file.
2. To see what SageStream has on file about you first, use the consumer report request tool at https://consumer.risk.lexisnexis.com/consumer.
3. Complete the required identifying fields: full name, street address, city, ZIP, and date of birth, plus either your Social Security number or driver's license number and state -- this is required under FCRA identity-verification rules.
4. If you want to stop unsolicited prescreened credit or insurance offers generated from your SageStream file, select the opt-out option; this is separate from a full security freeze.
5. If you want to prevent new creditors from accessing your SageStream file entirely (recommended if you're concerned about identity theft), place a security freeze instead at the /freeze link.
6. If you're a confirmed identity-theft victim, use the blocking tool to have fraudulent information removed from your file, and the file-dispute tool to challenge inaccurate information.
7. Requests are verified before processing and confirmations are typically sent by U.S. Mail, consistent with FCRA-regulated consumer reporting agency practices.
