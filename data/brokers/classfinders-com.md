---
id: classfinders-com
name: Class Finders
domain: classfinders.com
category: people_search
people_search: true
tier: assisted
priority: high
method: form
opt_out_url: "https://www.classfinders.com/name_removal.php"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, other]
readd_days: null
legal_basis: [none]
last_verified: null
source: "dbw+tcp-research"
notes: "ClassFinders is a people-search site aggregating high-school/alumni directory profiles (over 13M profiles, per third-party writeups) -- a genuine people-search broker, not noise. classfinders.com and classfinders.com/about.php returned HTTP 403 to direct WebFetch (bot-blocked); routing reconstructed from multiple independent 2024-2025 opt-out-guide writeups (Onerep, DeleteMe, deletemyinfo.com) that consistently point to a dedicated 'Name Removal' page at classfinders.com/name_removal.php, distinct from the search/profile pages. Process is a self-serve search-then-remove form (name, graduation year, city/state) with no CAPTCHA or ID mentioned in any guide -- kept at assisted rather than guided since no gating step was reported, but this is not independently confirmed against a rendered page. required_fields includes 'other' for graduation year/city/state, which has no dedicated enum value. priority is high rather than crucial because reviewers describe the site as a lower-traffic alumni-focused niche broker rather than a major address/phone aggregator, but people_search safety stakes still apply."
---

1. Go to https://www.classfinders.com/name_removal.php.
2. Enter your first name, last name, high school graduation year, city, and state to search for your listing.
3. Click "Search" and review the results for a profile matching you.
4. Click "Remove this name" (or equivalent) on the matching profile to submit the removal request.
5. Allow up to a week for the removal to process, per the site's own guidance.
6. Because ClassFinders aggregates from other alumni-directory sources, check back periodically and repeat the removal if your listing reappears after a data refresh.
