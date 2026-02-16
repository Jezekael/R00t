# Session management (cookies, tokens, fixation, logout)
**Category:** Web-Client  
**Severity (typical):** High (often leads to account takeover)  
**CWE / OWASP:** CWE-384 (session fixation), CWE-613 (insufficient session expiration), OWASP Session Management

## Overview
Session management covers how an application creates, protects, rotates, and terminates authenticated sessions. In web apps, sessions are commonly stored in cookies (session IDs) or as signed tokens (e.g., JWT). Weak session handling is a frequent root cause of account compromise.

## Real-world impact
- Account takeover (session hijacking or fixation)
- Privilege misuse (shared sessions across devices/users)
- Persistent access due to weak logout/expiry

## Common root causes
- Missing `Secure`/`HttpOnly`/`SameSite` on session cookies
- Session ID not rotated after login or privilege change
- Overly long session lifetime, no idle timeout
- Logout does not invalidate server-side session
- JWT used as long-lived bearer token without revocation/rotation strategy

## Detection & validation
### Where to look
- Authentication flows: login, logout, password change, MFA enable/disable
- Cookie attributes and token storage (localStorage vs HttpOnly cookie)
- Session refresh endpoints and “remember me” features

### Signals
- Session cookie without `Secure` on HTTPS apps
- Session accessible to JS (not HttpOnly) without strong reason
- SameSite missing/None without Secure
- Session persists after logout or password change
- Same session ID remains after login (potential fixation risk)

### Safe validation steps
- Check cookie flags in browser devtools
- Verify session rotation after login and privilege changes
- Test logout: reuse the same cookie/token; it should be rejected
- Evaluate session lifetime: idle timeout + absolute timeout

## Exploitation notes (high-level)
- XSS + non-HttpOnly session cookies is a common chaining risk
- “Remember me” tokens often become the real weak point (long-lived, revocation missing)

## Fix patterns
- Cookies: `Secure; HttpOnly; SameSite=Lax` (or Strict where possible)
- Rotate session ID after login and after privilege elevation
- Implement idle + absolute timeouts
- Invalidate sessions on logout and sensitive credential changes
- If using JWT: short expiry + rotation + revocation strategy for refresh tokens

## Verification (after fix)
- Logout invalidates session server-side
- Session ID changes after login
- Cookie flags correct on all auth cookies across subdomains
- Password change/MFA change invalidates other sessions (policy-driven)

## Resources
- OWASP Session Management Cheat Sheet
- MDN Cookie attributes
