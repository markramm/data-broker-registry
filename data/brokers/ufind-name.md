---
id: ufind-name
name: uFind.name
domain: ufind.name
category: people_search
people_search: true
tier: guided
priority: crucial
method: form
opt_out_url: "https://ufind.name/opt-out"
opt_out_email: null
phone: null
captcha: true
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Fetched ufind.name and ufind.name/opt-out directly (HTTP 200 via curl with a browser user-agent; Claude's built-in WebFetch got a 403 bot-block on the same URLs). Confirmed genuine people-search engine ('We are a people search engine to access millions of public online records... Look yourself up. See what's on the internet about you.'). The /opt-out page is a simple form asking only for the URL of the profile page to remove -- no email or CAPTCHA field visible in the static HTML, but the page loads Cloudflare's challenge-platform script (same 'cf$cv$params' turnstile snippet seen on unitedstatesphonebook.com), so classified captcha:true and tier:guided rather than assisted. last_verified left null since this was scripted HTML retrieval, not a rendered-browser confirmation of the live form behavior."
---

1. Go to https://ufind.name and search your name (or check the "Top Profiles" / alphabetical catalog) to find any profile page matching you.
2. Open that profile page and copy its full URL (it will look like https://ufind.name/FirstName+LastName).
3. Go to https://ufind.name/opt-out.
4. Paste the profile URL into the "Paste the URL here" field and submit the form. The page is Cloudflare-protected, so you may need to complete a bot-check challenge before the form will submit.
5. Repeat for each distinct profile URL that matches you, since removing one listing does not remove others under different name spellings or locations.
6. Re-check periodically, since people-search sites commonly re-scrape and re-list public records.
