---
id: innovis-com
name: "Innovis Data Solutions, Inc."
domain: innovis.com
category: credit_bureaus
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://www.optoutprescreen.com/"
opt_out_email: null
phone: "1-800-540-2505"
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [full_name, address, dob, ssn]
readd_days: 1825
legal_basis: [none]
last_verified: null
source: "dbw+tcp-research"
notes: "Innovis is the fourth major US credit bureau (with Equifax, Experian, TransUnion). Verified with WebFetch on several current innovis.com pages -- the legacy CSV's opt-out URL (innovis.com/InnovisWeb/pers_lc_opt_out.html) now 404s and is dead; the current site's nav link-scrape (curl) found the real path /personal/lc_optOut. That page, plus /personal/optOutOptIn, both make clear Innovis does NOT run its own standalone consumer 'opt out of data sale' portal analogous to Equifax's myprivacy.equifax.com -- instead its two consumer-facing controls are (1) a security freeze (/personal/securityFreeze -- restricts new-credit access to your file, separate product, not a sale opt-out) and (2) referring consumers to the shared four-bureau prescreen opt-out at optoutprescreen.com / 1-888-567-8688 to stop unsolicited firm-offer marketing lists (this repo already has a separate optoutprescreen-com.md entry -- do not conflate the two). Innovis's own /home/privacy link 302-redirects to business.innovis.com/privacy-notice, which explicitly states its CCPA section applies ONLY to B2B relationships and that Innovis 'does not engage in direct-to-consumer marketing activities' and provides no consumer sale-opt-out because it does not sell/share B2B personal information. Given no distinct Innovis-only consumer opt-out page exists, this entry routes to optoutprescreen.com (matching the CSV's stated intent to give consumers a working link) while the notes make the routing explicit; opt_out_email left null since Innovis's own privacy notice explicitly asks that inquiries NOT be submitted by email ('do not submit your inquiry to us by email'). General consumer assistance line 1-800-540-2505 and dispute line 1-866-712-0021 were both found; the former is used here as the general contact number. tier guided because the actual path requires understanding which of several Innovis-adjacent tools (freeze vs. prescreen opt-out vs. B2B request portal) applies, not a single clean click. priority high per instructions (credit bureau, real financial-privacy stakes). last_verified left null."
---

1. Innovis does not run its own separate 'opt out of data sale' web form for consumers the way some other bureaus do -- its consumer-facing privacy notice (routed from innovis.com to business.innovis.com) states its CCPA opt-out section applies only to business-to-business relationships, since Innovis says it does not sell or share consumer personal information for direct marketing to third parties in a way that would trigger a separate opt-out.
2. To stop creditors and insurers from receiving your name on marketing lists for unsolicited "firm offer" credit/insurance mail (the main consumer-facing list Innovis and the other three bureaus maintain), use the shared joint-bureau opt-out at https://www.optoutprescreen.com/ or call 1-888-567-8688. This is the mechanism Innovis's own site directs consumers to.
3. If your concern is restricting access to your Innovis credit file for new-credit applications (identity-theft protection rather than marketing), use Innovis's security freeze tool instead, at innovis.com/personal/securityFreeze, or call 1-866-712-4546; this is a different product from a data-sale opt-out.
4. For general consumer assistance, including questions about your Innovis file or privacy inquiries not covered by the above, call 1-800-540-2505, or write to Innovis Consumer Assistance, PO Box 530088, Atlanta, GA 30353-0088.
5. Do not email Innovis with personal information for these requests -- their own privacy notice specifically asks that inquiries not be submitted by email, to protect the confidentiality of your data.
6. If you believe information in your Innovis credit report itself is inaccurate, that is a separate dispute process (not a privacy opt-out): use your online Innovis account, call 1-866-712-0021, or mail an Investigation Request form to the same Atlanta PO Box.
