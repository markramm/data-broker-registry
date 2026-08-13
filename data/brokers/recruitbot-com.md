---
id: recruitbot-com
name: RecruitBot
domain: recruitbot.com
category: recruiting_data
people_search: false
tier: auto
priority: standard
method: email
opt_out_url: "<verify: https://recruitbot.com/removal-request/ returned HTTP 404 on direct fetch -- confirm correct current path for the web removal form before linking it>"
opt_out_email: "privacy@recruitbot.com"
phone: "8884816811"
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [full_name, email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "therecruitbot.com HTTP 301-redirects to www.recruitbot.com -- same entity, not a separate broker. RecruitBot is a B2B recruiting/sourcing SaaS product (per its own homepage copy: 'in-house recruiters,' 'hiring managers,' 'recruiting agencies') built on a self-described 'proprietary database of 655+ million candidate profiles' including contact info and employment history -- it is not a consumer people-search site and doesn't publicly surface individual listings the way Spokeo/TruePeopleSearch do, so people_search is false and priority is standard rather than crucial/high. Its privacy policy (fetched at recruitbot.com/privacy-policy) explicitly states a CCPA right to opt out of 'sale' of Personal Information via three channels: emailing privacy@recruitbot.com, calling (888) 481-6811, or a web form at https://recruitbot.com/removal-request/. The removal-request URL returned a bare HTTP 404 when fetched directly in this session, so it is not used as the primary opt_out_url and is instead flagged with a <verify> placeholder; email is the confirmed, lower-friction channel and is used as the recommended method (tier:auto). Company name/entity details were not visible on the homepage footer beyond 'RecruitBot Copyright 2026.' Not independently confirmed by rendering the removal form page itself."
---

<!-- Real instructions based on RecruitBot's published CCPA opt-out/removal channels. -->
1. RecruitBot is a B2B candidate-sourcing tool for recruiters, not a public people-search site -- your data may appear in it only as part of its recruiting/candidate database, not as a public searchable profile page.
2. To request that RecruitBot stop selling/sharing your personal information or remove your candidate record, email privacy@recruitbot.com from the email address you want covered by the request.
3. State clearly that you are requesting a CCPA "opt-out of sale" and deletion of your personal information from RecruitBot's candidate database, and include your full name (and any known alternate names or prior employers) to help them locate your record.
4. If you don't get a response, call RecruitBot's toll-free privacy line at 1-888-481-6811 and reference your email request.
5. RecruitBot's published compliance metrics cite a median response time of about 2 days for these requests; if you have a web browser handy, you can also try https://recruitbot.com/removal-request/ (named in their privacy policy), but this URL did not load during verification, so email is the more reliable channel for now.
