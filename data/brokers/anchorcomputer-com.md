---
id: anchorcomputer-com
name: Anchor Computer, Inc.
domain: anchorcomputer.com
category: marketing_data_broker
people_search: false
tier: guided
priority: high
method: form
opt_out_url: "https://ecom2.anchorcomputer.com/privacyrequest"
opt_out_email: "privacyteam@anchorcomputer.com"
phone: "1-800-646-2563"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, address, dob, phone, email]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "WebFetch of anchorcomputer.com homepage and /privacy-policy confirmed directly. Anchor Computer is a marketing-data/mailing-list compiler offering 'customer profiling and data validation to segmentation and targeting' built on '6B+ Permissioned signals,' and its privacy policy lists name, SSN, postal address, email, phone, plus demographic data (age, religion, ethnicity, marital status, gender, hobbies) among categories sold. Policy explicitly grants CPRA right to opt out of sale and right to deletion, and names the online form at ecom2.anchorcomputer.com/privacyrequest ('Individual Consumer Opt-Out Submission Form') plus email/phone alternatives. Form fields (name, address, last-4 SSN, DOB, phone, email) are as listed in the privacy policy text, not independently confirmed by rendering the form itself -- guided tier given the sensitive-field combination (SSN, DOB) even without CAPTCHA. last_verified left null since the live form itself wasn't rendered. 2026-10-27 maintainer, after page-monitor #17: the form no longer has the 'SSN (last 4 digits)' field (snapshot of 2026-10-26; confirmed by fetching https://ecom2.anchorcomputer.com/privacyrequest, HTTP 200: its inputs are FirstName, LastName, Suffix, Address Line 1 and 2, City, State, Zip, DateOfBirth, PhoneNumber, Email and three request checkboxes, no SSN). ssn removed from required_fields and the steps; the form marks State, Date of Birth, Phone Number and Email as required. Tier stays guided (DOB is still asked for). The page now cites California 'CRPA' instead of 'CCPA'; no change to the process. last_verified unchanged."
---

1. Go to the Anchor Computer opt-out form at https://ecom2.anchorcomputer.com/privacyrequest.
2. Enter your first and last name, mailing address, phone number, and email address.
3. Enter your date of birth, which Anchor Computer uses to match your record in its marketing database. The form no longer asks for any part of your Social Security number.
4. Tick the request you want: "Delete my data", "Do not sell my data", or (California residents) "Request full report". Then submit the form.
5. Alternatively, skip the form and email the same information directly to privacyteam@anchorcomputer.com, or call 1-800-646-2563 to request opt-out/deletion by phone.

**Sensitive-data note:** this process asks for your date of birth. Only proceed if you're comfortable sharing that; the phone and email channels ask for the same information, so there's no lower-friction path available.
