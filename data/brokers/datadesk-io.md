---
id: datadesk-io
name: "DataDesk"
domain: datadesk.io
category: advertising_adtech
people_search: false
tier: auto
priority: standard
method: email
opt_out_url: "https://datadesk.io/help/do-not-sell-my-personal-info"
opt_out_email: "privacy@datadesk.io"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
verification: null
required_fields: [other]
readd_days: null
legal_basis: [ccpa, gdpr]
last_verified: null
source: "ca-registry+tcp-research"
notes: "Listed in the California data broker registry (Datadesk Inc., privacy@datadesk.io). The rights URL is a JavaScript app. A plain fetch returned only 'You need to enable JavaScript', so I rendered it in a headless browser on 2026-11-21. The page, 'Do Not Sell or Share My Personal Information' (effective Sept 1 2026), says DataDesk is a registered California data broker. To opt out, email privacy@datadesk.io, or in Europe use the consent tool of the site or app (IAB TCF vendor 1641). It honours Global Privacy Control. It asks you to include your Advertising Identifier (iOS or Android ad ID) or browser cookie ID, because it holds no names, addresses or phone numbers. It builds advertising profiles from device and cookie IDs, IP addresses, browsing data and hashed emails, so the ad ID is what it matches on. It says it acts within 15 business days and tells clients and partners to stop using the data. Opting out does not delete the data: deletion needs a separate request, or California's DROP platform at privacy.ca.gov. required_fields is 'other' for the advertising ID. Ad-tech data, so priority standard. Not walked through by a human: last_verified null."
---

1. Find your device's advertising ID. On iOS: Settings → Privacy & Security → Apple Advertising. On Android: Settings → Google → Ads. On a computer, DataDesk also accepts a browser cookie ID.
2. Email privacy@datadesk.io. Say you are opting out of the sale and sharing of your personal information and of its use for advertising and profiling. Include the advertising ID(s) from step 1.
3. Opting out does not delete your data. To delete it too, ask for deletion in the same email. California residents can also use the DROP platform at privacy.ca.gov.
4. DataDesk says it acts within 15 business days. Turning on Global Privacy Control in your browser also sends an opt-out signal it says it honours.
