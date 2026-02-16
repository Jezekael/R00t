# XSS — Reflected
**Category:** Web-Client

## What it is
Reflected Cross-Site Scripting is a client-side injection where attacker-controlled input is immediately reflected in the server’s response and executed by the browser. The payload typically travels via URL parameters, headers, or form fields and runs only when a victim loads the crafted request.

## What it enables / impact
- Credential/session theft (depending on cookie flags and app design)
- User impersonation / actions as the victim (through script-driven requests)
- Data exfiltration from the page (DOM scraping), phishing UI overlays

## Preconditions / requirements
- Untrusted input reaches an executable sink (HTML, attribute, JS, URL context)
- Missing or incorrect context-aware output encoding
- Victim must load the malicious link/request while authenticated (for higher impact)

## How to recognize (recon)
### Where to look
- Search pages, error pages, “message=” / “q=” / “redirect=” parameters
- Any “echo” functionality (preview, debug banners)
- Reflections in headers (some apps reflect into HTML title/meta)

### Indicators
- Your marker string appears in the HTML response
- Reflection context changes based on quoting/escaping
- CSP may be absent or permissive (but CSP alone doesn’t prove XSS)

### Quick tests (high-level)
- Send a unique marker and confirm it reflects
- Determine the context (text node vs attribute vs script string vs URL)
- Check whether special characters are encoded appropriately for that context

## Common variants
- HTML injection vs script-context injection
- Attribute-based injection (event handlers, href/src contexts)
- “Filtered” reflected XSS (bypass relies on weak filtering rather than proper encoding)

## Mitigations (blue-team view)
- Context-aware output encoding everywhere user data is rendered
- Prefer safe templating / auto-escaping, avoid string concatenation into HTML/JS
- Defense-in-depth: strict CSP, HttpOnly cookies, input validation (allowlists)

## Resources
- OWASP: Cross Site Scripting (XSS)
- OWASP: XSS Prevention Cheat Sheet

**Related challenges:** 
- Root-Me: Web-Client XSS - Reflected