# HTTP, Web Sessions & Common Web Vulnerabilities

## HTTP & Web Sessions
- HTTP is stateless: each transaction = one request + one response. Common methods: `GET`, `POST`, `PUT`, `DELETE`, `OPTIONS`, `TRACE`, `CONNECT`.
- Proxies act as intermediaries (caching, firewall traversal).
- Messages: **headers** (control) + **body** (content).
- Sessions: tracked via session IDs / tokens — must be long, random, securely stored, and rotated to prevent fixation and hijacking.

---

## Injection Vulnerabilities
### SQL Injection (SQLi)
- Impact: read/modify/delete DB data, escalate control.
- Types: **In-band**, **Blind**, **Out-of-band**.
- Techniques: UNION, boolean, error-based, time-based, OOB exfiltration.
- Prevention: parameterized queries, prepared statements, stored procedures, least privilege.

### Command Injection
- Occurs when user input is passed to system/shell commands without sanitization.
- Mitigation: avoid shell invocation, validate/whitelist input, use safe APIs.

### LDAP Injection
- Injection into LDAP queries leads to auth bypass or information disclosure.
- Mitigation: sanitize input, use parameterized LDAP APIs.

---

## Authentication & Session Risks
- **Credential brute force / password spraying**: use MFA, lockout policies, rate-limiting.
- **Default / weak credentials**: enforce password policies and inventory.
- **Session hijacking / fixation**: use secure, HttpOnly, SameSite cookies; rotate session IDs after login; use TLS everywhere.
- **Kerberos abuses**: mitigate with strong secret management, restrict delegation, monitor for golden/silver ticket behaviors.

---

## Authorization Issues
- **Parameter pollution**: multiple parameters with same name can alter server behavior — validate and normalize inputs.
- **Insecure Direct Object References (IDOR)**: enforce authorization checks server-side; avoid using predictable identifiers.

---

## Cross-Site Scripting (XSS)
- Types: **Reflected**, **Stored (Persistent)**, **DOM-based**.
- Locations: inputs, headers, hidden fields, error messages.
- Mitigations: context-aware escaping, CSP, HTTPOnly cookies, input validation, auto-escaping templates.

---

## CSRF & Clickjacking
- **CSRF**: use anti-CSRF tokens, require same-site cookies, verify origin/referer for state-changing requests.
- **Clickjacking**: set `X-Frame-Options` / `Content-Security-Policy: frame-ancestors` and validate `window.top` where applicable.

---

## Other Common Flaws
- **Directory traversal**: validate and canonicalize file paths; avoid exposing filesystem paths.
- **Cookie manipulation**: protect cookies with `Secure`, `HttpOnly`, `SameSite`; validate server-side.
- **Sensitive data in comments / hard-coded credentials**: remove secrets from code; use secret managers.
- **Verbose error messages**: return generic errors to users; log details internally.
- **Race conditions**: apply proper synchronization and atomic operations.
- **Unprotected APIs**: enforce authN/authZ, input validation, rate limits, and TLS.
- **Missing code signing**: use code signing to ensure integrity where applicable.

---

## Tools & Testing Aids
- Web proxies: Burp Suite, OWASP ZAP.
- Discovery/fuzzing: `gobuster`, `ffuf`, `dirb/dirbuster`, `feroxbuster`.
- Exploit lookup: `searchsploit`.

---

## Defensive Summary
- Adopt secure-by-default coding: parameterized queries, input validation, least privilege.
- Enforce TLS everywhere, use strong session management, MFA, logging/monitoring, and regular pentests.

*End of document.*

