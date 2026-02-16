# XSS — Stored
**Category:** Web-Client

## What it is
Stored (persistent) XSS happens when attacker-controlled content is stored server-side (database, logs, profile fields, comments) and later rendered to other users without safe encoding/sanitization, causing their browsers to execute it.

## What it enables / impact
- Persistent account compromise (admin panels are common high-impact targets)
- Worm-like propagation (if it can self-post to the same feature)
- Long-lived phishing/defacement and sensitive data extraction from pages

## Preconditions / requirements
- A storage point that accepts attacker-controlled input
- A render point where that data is inserted into DOM/HTML/JS unsafely
- Victims (users/admin) view the page where it renders

## How to recognize (recon)
### Where to look
- Comments, support tickets, chat, usernames/display names, “bio”, HTML editors
- Admin dashboards listing user submissions (often less protected)

### Indicators
- The content persists across refresh/login
- Appears in multiple views (list view + details view)
- Output differs per view (safe in one, unsafe in another)

### Quick tests (high-level)
- Store a unique marker string and verify it renders later
- Compare rendering contexts (escaped in list, unescaped in details is common)
- Verify whether HTML is allowed intentionally (then check for safe sanitization)

## Common variants
- Stored HTML injection in rich-text/markdown renderers
- Stored XSS via unsafe HTML sanitizers (broken allowlists)
- Stored XSS through file upload metadata (filename, EXIF, SVG content)

## Mitigations (blue-team view)
- Encode on output; sanitize only if you intentionally allow HTML
- Use well-maintained sanitizers (strict allowlists), and test bypasses
- CSP, HttpOnly cookies, and strict session handling as defense-in-depth

## Resources
- OWASP: Cross Site Scripting (XSS)
- OWASP: XSS Prevention Cheat Sheet

**Related challenges:** 
- Root-Me: Web-Client XSS - Stored 1 / XSS - Stored 2