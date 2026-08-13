---
id: ancestry-com
name: "Ancestry.com"
domain: ancestry.com
category: personal_information
people_search: true
tier: assisted
priority: high
method: form
opt_out_url: "https://www.ancestry.com/legal/ccpa-donotshare-sell"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: ["other"]
readd_days: null
legal_basis: [ccpa, cpra]
last_verified: null
source: "dbw+tcp-research"
notes: "Direct WebFetch of ancestry.com/legal/ccpa-donotshare-sell returned HTTP 403 (bot-blocked); ancestry.com/cs/privacyphilosophy also 403'd. Findings are from WebSearch snippets of Ancestry's own California Privacy Statement: Ancestry states it does not sell personal information in the traditional CCPA sense, but does allow opt-out of 'sharing' for cross-context behavioral/targeted advertising via the Do Not Sell or Share My Personal Information / Opt Out of Targeted Advertising page (linked in site footers) and via Global Privacy Control signals. This is a browser/device-level ad-tracking opt-out, not a way to delete genealogical records or family-tree mentions of you (Ancestry's core people-search-adjacent content -- historical records, DNA matches, family trees where third parties may have entered your info -- has separate, more limited removal mechanisms not confirmed here). people_search is set true because Ancestry's record search functions expose living individuals' names/relationships/locations, but note the opt-out documented here only covers ad-targeting, not record deindexing. required_fields uses 'other' since this is a preference toggle, not an identity-verified request. last_verified left null since neither page could be directly fetched."
---

1. Go to [Ancestry's Do Not Sell or Share My Personal Information / Opt Out of Targeted Advertising page](https://www.ancestry.com/legal/ccpa-donotshare-sell) (also reachable via the "Do Not Sell or Share My Personal Information" link in the footer of Ancestry sites).
2. Follow the on-page instructions to opt out of the sale/sharing of your personal information for cross-context behavioral (targeted) advertising.
3. If your browser or device has Global Privacy Control (GPC) enabled, Ancestry says it will honor that signal automatically as an opt-out preference.
4. Note this only stops ad-targeting use of your data -- it does not remove your name from historical records, family trees other users have created, or DNA-match results. If you are named in another user's tree or a record and want that addressed, you will need to use Ancestry's separate content-removal/support process (not confirmed in this research pass).
5. Ancestry states it does not discriminate against users for exercising CCPA rights.
