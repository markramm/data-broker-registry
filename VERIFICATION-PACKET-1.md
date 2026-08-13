# Verification Packet 1 — Chrome-driven opt-out check

**Repo**: `/Users/markr/make-yourself-expensive` (data-broker-registry)
**Purpose**: These 10 broker entries were authored by an AI research pass (WebFetch/WebSearch), not by a human clicking through the live flow. `last_verified` is `null` on all of them. This packet asks Claude in Chrome to actually drive the real opt-out flow for each site, note what's true vs. what needs correcting, and stop for a human at any point that requires solving a CAPTCHA, confirming an email, or supplying real personal information.

## How to use this packet

Start a new session with Chrome/browser-control access (MCP or equivalent) and paste this prompt:

> You have access to a browser tool for Chrome. I want you to visit 10 data-broker opt-out pages one at a time and report back what you actually find — NOT what a privacy guide says should be there. For each site:
> 1. Navigate to the `opt_out_url` given below.
> 2. Report: does the page load? Does it match the described `method` (form/portal)? What fields does the form actually ask for? Is there a CAPTCHA? Does it require an account/login?
> 3. **Do NOT submit any form with real personal information.** Do not solve a CAPTCHA to get past a wall — if a CAPTCHA blocks you from even *seeing* the form, note that and move on; if it only appears at final submission, you can stop there and note it without submitting.
> 4. **Do NOT use my real name/email/DOB/address anywhere.** This pass is about confirming the *mechanism* (what the page looks like, what it asks for), not completing a real opt-out request yet. If the page structure can't be confirmed without submitting real data, note that as "confirmed structure, could not test submission."
> 5. If a site is dead, redirects elsewhere, or the URL 404s, say so clearly.
> 6. Give me a short verdict per site: `CONFIRMED` (matches as documented), `PARTIAL` (mostly right, note discrepancy), or `WRONG` (URL/mechanism doesn't match, here's what's actually there).
>
> Work through all 10, then give me one consolidated report at the end in the format specified below. Paste the [full packet below] as your reference data.

## The 10 sites

### 1. intelius.com
- **opt_out_url**: https://www.intelius.com/opt-out
- **documented method**: portal (guided tier)
- **documented fields**: full_name, dob, email
- **documented captcha**: yes
- **note**: This may be the SAME underlying portal as peopleconnect.us's suppression center (both are PeopleConnect-family brands). Check whether intelius.com/opt-out redirects to suppression.peopleconnect.us or is genuinely separate.

### 2. beenverified.com
- **opt_out_url**: https://www.beenverified.com/app/optout/search
- **documented method**: form (assisted tier)
- **documented fields**: full_name, email
- **documented captcha**: yes

### 3. mylife.com
- **opt_out_url**: https://www.mylife.com/privacyrequest
- **documented method**: form (guided tier)
- **documented fields**: full_name, email, address
- **documented captcha**: no

### 4. fullcontact.com
- **opt_out_url**: https://platform.fullcontact.com/your-privacy-choices
- **documented method**: portal (guided tier)
- **documented fields**: email, full_name
- **documented captcha**: no

### 5. peopleconnect.us
- **opt_out_url**: https://suppression.peopleconnect.us/
- **documented method**: form (assisted tier)
- **documented fields**: full_name, email, dob
- **documented captcha**: no
- **note**: Documented as the shared suppression hub for the whole PeopleConnect family (Intelius, TruthFinder, Instant Checkmate, USSearch). Please confirm this is real and check what "covers other brands too" actually looks like on the page (a checkbox? separate submissions?).

### 6. instantcheckmate.com
- **opt_out_url**: https://suppression.peopleconnect.us/login
- **documented method**: portal (guided tier)
- **documented fields**: email, full_name, dob
- **documented captcha**: no
- **note**: Same underlying portal as #5 per our notes, but with `/login` appended — confirm whether that's a real distinct step (account required?) or just a URL variant.

### 7. nuwber.com
- **opt_out_url**: https://nuwber.com/removal/link
- **documented method**: form (assisted tier)
- **documented fields**: listing_url, email
- **documented captcha**: no

### 8. enformion.com
- **opt_out_url**: https://www.enformion.com/opt-out/
- **documented method**: form (guided tier)
- **documented fields**: full_name, email
- **documented captcha**: yes

### 9. checkthem.com
- **opt_out_url**: https://www.checkthem.com/optout/
- **documented method**: form (guided tier)
- **documented fields**: listing_url, email, full_name
- **documented captcha**: yes

### 10. contactout.com
- **opt_out_url**: https://www.contactout.com/optout
- **documented method**: form (assisted tier)
- **documented fields**: email, full_name
- **documented captcha**: no

## Report format to bring back

For each site, one block like this:

```
### <domain>
verdict: CONFIRMED | PARTIAL | WRONG
opt_out_url: <the URL that actually works, if different>
method: <email|form|portal|mail|phone|unsupported>
captcha: <true|false>
id_required: <true|false>
required_fields: <list>
notes: <anything a future reader needs to know — redirects, login walls, dead links, shared-portal confirmation, etc.>
```

Paste all 10 blocks back into the make-yourself-expensive conversation and Claude Code will update the `.md` files, set `last_verified` to today's date on confirmed entries, and commit.
