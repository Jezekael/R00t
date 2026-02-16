# CSRF (missing defenses)
**Category:** Web-Client  
**Severity (typical):** High (if state-changing actions are exposed)  
**CWE / OWASP:** CWE-352 / OWASP Top 10: A01 Broken Access Control (often adjacent)

## Overview
Cross-Site Request Forgery (CSRF) is when a victim’s browser is tricked into sending an authenticated request to a target application. “Missing defenses” means the application does not implement effective CSRF protections for state-changing actions (e.g., profile updates, email/password change, payments, administrative actions).

## Real-world impact
- Unauthorized state changes as the victim (email/password change, MFA changes, address update)
- Fraudulent transactions or business actions (orders, transfers, invoice approval)
- Privilege impact if sensitive/admin actions are exposed

## Common root causes
- No CSRF tokens on state-changing endpoints
- Relying on CORS as “protection” (CORS does not stop CSRF)
- Using GET for state changes
- Session cookies configured without a robust SameSite strategy
- Inconsistent protection (some endpoints protected, others not)

## Detection & validation
### Where to look
- Any action that changes server state: settings, profile, password, email, billing, admin features
- JSON API endpoints invoked from the browser
- Legacy endpoints and “back-office” actions

### Signals
- No anti-CSRF token present in forms or request headers
- Server accepts state changes without verifying origin context
- Session cookies missing/weak `SameSite`, missing `Secure`

### Safe validation steps
- Map a state-changing request (method, parameters, cookies)
- Check whether the request includes an unpredictable token bound to the user/session
- Confirm server enforcement: missing/invalid token should hard-fail (4xx or no state change)
- Review cookie flags (`SameSite`, `Secure`, `HttpOnly`) and whether the app uses cookies for auth

## Exploitation notes (high-level)
- Severity depends on: action sensitivity, re-auth requirements, MFA protections, and cookie SameSite policy
- Endpoints that accept “simple” submissions (standard form POSTs) are typically higher risk
- “JSON-only” endpoints may still be CSRFable depending on how the app authenticates (cookies) and content-type handling

## Fix patterns
- Use CSRF tokens (synchronizer tokens) for all state-changing endpoints
- Ensure tokens are: unpredictable, session-bound, validated server-side, and rejected when missing/invalid
- Configure session cookies: `SameSite=Lax` (baseline) or `Strict` (where possible) + `Secure` + `HttpOnly`
- Consider Origin/Referer validation for sensitive actions as defense-in-depth (not the only control)
- Avoid state changes via GET

## Verification (after fix)
- Missing token → request must fail and state must not change
- Invalid token → request must fail and state must not change
- Token from another session/user → must fail
- Confirm sensitive actions require re-authentication where appropriate (password/MFA changes)

## Resources
- OWASP: Cross-Site Request Forgery (CSRF)
- PortSwigger: CSRF
- MDN: SameSite cookies

**Related labs/challenges (optional):**
- Root-Me CSRF (various)
