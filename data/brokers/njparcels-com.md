---
id: njparcels-com
name: NJParcels.com
domain: njparcels.com
category: property_records
people_search: false
tier: assisted
priority: standard
method: form
opt_out_url: "https://njparcels.com/redaction/"
opt_out_email: null
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [listing_url, email, full_name]
readd_days: null
legal_basis: [none]
last_verified: null
source: "dbw+tcp-research"
notes: "Confirmed via direct curl fetch of njparcels.com/redaction/ (HTTP 200, fully rendered). NJParcels.com is a New Jersey property-records lookup site (tax assessment data, sales history, comparable sales across NJ's 21 counties). It publishes a genuine redaction/removal request form (POST to /redaction/) with fields request_page (the URL of the page to redact), request_email, request_name, request_reason (free text), and a request_confirm checkbox -- no CAPTCHA markup found in the fetched HTML. The page states the site has offered removal since 2014, over 30,000 pages redacted, requests evaluated within 72 hours, and >99.9% of requests honored (though the site reserves the right to refuse bulk/automated requests). people_search left false -- this is property/tax-record data (owner name/address tied to a parcel), not a general identity/reverse-lookup product, and the site notes it is not a consumer reporting agency. Because the mechanism is a simple, non-CAPTCHA web form (not a plain mailto), classified assisted rather than auto. last_verified left null despite the direct render since the form's own JS validation and confirmation-email flow after submission weren't exercised."
---

1. Search your name or address on njparcels.com to find the property record listing that names you, and copy that page's URL.
2. Go to https://njparcels.com/redaction/ and fill in: the URL of the page you want redacted, your email address, your full name, and a brief reason for the request.
3. Check the confirmation checkbox and submit the form.
4. Requests are typically evaluated within 72 hours; note that redaction removes your name from NJParcels' public pages going forward but does not remove the underlying record from the municipal/county/regional government sources NJParcels draws from -- your name will remain available directly from those official sources regardless.
5. Also note it may take additional time for search engines to drop cached copies of the old page after the redaction takes effect.
