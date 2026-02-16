# CSRF token implementation flaws
**Category:** Web-Client  
**Severity (typical):** High (because teams assume “we have tokens”)  
**CWE / OWASP:** CWE-352 / OWASP Top 10 adjacent

## Overview
This class covers cases where CSRF tokens exist but are not effective due to design or implementation flaws. The outcome is that cross-site requests can still succeed.

## Real-world impact
- Same as CSRF: unauthorized actions as the victim
- Often missed in reviews because “a token exists”, leading to persistent risk

## Common root causes
- Token not bound to session/user (works across accounts)
- Token validated only for presence (any value accepted)
- Token reused indefinitely, not rotated appropriately
- Token leak through caching, logs, referrer, or being embedded in URLs
- Token enforced only on some methods/routes (inconsistent middleware)
- Using “double-submit cookie” incorrectly (no integrity binding)

## Detection & validation
### Where to look
- Every state-changing endpoint that claims CSRF protection
- Multi-step forms (tokens often validated only on step 1)
- Alternate endpoints performing the same action (API vs web form)

### Signals
- Token value identical across sessions/users
- Request succeeds with empty/missing token
- Token accepted after logout/login or across browsers
- Token appears in URL parameters or is cached

### Safe validation steps
- Compare tokens across two distinct sessions/users (should differ)
- Replay a request with: missing token, invalid token, token from another session (must fail)
- Confirm the server is the one enforcing validation (not only front-end JS)

## Exploitation notes (high-level)
- Token flaws are often paired with weak SameSite cookies, making CSRF reliable
- Token leakage via referrer is more likely when tokens are in URLs or when external resources load on sensitive pages

## Fix patterns
- Session-bound synchronizer tokens validated server-side on every state-changing request
- Strict rejection on missing/invalid tokens
- Rotate tokens appropriately; avoid putting them in URLs
- Add SameSite cookies + Origin/Referer validation defense-in-depth for high-risk actions

## Verification (after fix)
- Token from another user/session fails
- Missing/empty token fails
- Token cannot be replayed indefinitely for sensitive actions (as per your design)
- Tokens are not present in URLs and are not cached

## Resources
- OWASP CSRF
- PortSwigger CSRF

**Related labs/challenges (optional):**
- Root-Me CSRF token themes
