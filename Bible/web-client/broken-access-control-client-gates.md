# JavaScript — Client-side Authentication / Authorization Logic
**Category:** Web-Client

## What it is
A class of issues where authentication/authorization is enforced partially or fully in client-side JavaScript (UI gates, hidden routes, client checks) instead of being enforced by the server.

## What it enables / impact
- Unauthorized access to pages/features if server endpoints are not protected
- Privilege escalation by calling protected APIs directly
- Bypass of “disabled” UI restrictions (buttons/menus) when server trusts client

## Preconditions / requirements
- Server does not enforce authorization robustly
- Sensitive endpoints exist and can be accessed without proper server checks

## How to recognize (recon)
### Where to look
- SPA route guards, feature flags, “isAdmin” checks in JS
- “Disabled” buttons or hidden links that become enabled by JS
- API calls in DevTools Network tab

### Indicators
- UI blocks access but endpoints still respond when called directly
- Role/permission checks appear only in frontend code
- Different users get same API responses (server not filtering)

### Quick tests (high-level)
- Enumerate API endpoints used by the UI and verify server-side enforcement
- Compare responses across roles/accounts for the same endpoint
- Inspect whether server uses claims it can verify (session-side role) vs client-provided role

## Common variants
- Hidden admin links/routes
- “Premium feature” gating in JS only
- Client-side checks on IDs/ownership (“only show your documents”)

## Mitigations (blue-team view)
- Enforce authorization server-side for every request
- Treat client as untrusted; validate identity/role/ownership on the server
- Use least privilege + consistent access control middleware

## Resources
- OWASP: Broken Access Control
- OWASP: Authorization Cheat Sheet

**Related challenges:** 
- Root-Me: Web-Client Javascript - Authentication (series), HTML - disabled buttons