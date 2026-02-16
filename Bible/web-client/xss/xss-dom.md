# XSS — DOM-Based
**Category:** Web-Client

## What it is
DOM-based XSS occurs when JavaScript running in the browser takes attacker-controlled data (URL, fragment, postMessage, localStorage, etc.) and writes it into the DOM using unsafe sinks, without proper sanitization/encoding. The server may never see the payload.

## What it enables / impact
- Same as other XSS: data theft, account actions, phishing overlays
- Bypasses some server-side filters because payload is handled client-side

## Preconditions / requirements
- A source of attacker-controlled data in the browser
- An unsafe sink (DOM APIs or framework patterns) that interprets it as HTML/JS/URL
- Insufficient client-side sanitization/encoding

## How to recognize (recon)
### Where to look
- JS that reads from: `location`, `document.URL`, `location.hash`, query params
- `postMessage` handlers, localStorage/sessionStorage reads
- SPA routers and dynamic rendering logic

### Indicators
- Payload changes only affect client-side rendering (view-source may look clean)
- Behavior differs when changing only URL fragment (`#...`)
- Security issues disappear when JS is disabled

### Quick tests (high-level)
- Identify sources and sinks in JS (manual review + browser devtools)
- Change URL inputs (query/hash) and observe DOM changes
- Use breakpoints on DOM writes to trace the data flow

## Common variants
- DOM clobbering interactions
- postMessage handler injection
- Framework-specific template injection patterns

## Mitigations (blue-team view)
- Avoid HTML-interpreting sinks; use text-safe APIs
- Use trusted sanitization for any HTML you must render
- Strong CSP + Trusted Types (where feasible)

## Resources
- OWASP: DOM Based XSS
- MDN: DOM APIs and safe text insertion

**Related challenges:** 
- Root-Me: Web-Client XSS - DOM Based (and related DOM XSS series)