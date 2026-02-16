# Open Redirect
**Category:** Web-Server  
**Severity (typical):** Medium (can become High in auth/OAuth flows)  
**CWE / OWASP:** CWE-601

## Overview
Open redirect occurs when an application redirects users to a URL controlled by attacker input without strict validation. It’s commonly abused for phishing, and it can be more severe when chained with authentication flows.

## Real-world impact
- Phishing using a trusted domain
- Token leakage in poorly designed OAuth/OIDC flows
- Security control bypasses where redirects are used as trust boundaries

## Common root causes
- Allowing absolute URLs or protocol-relative URLs in redirect parameters
- Weak allowlists (string contains checks, suffix checks)
- Inconsistent normalization/parsing of URLs

## Detection & validation
### Where to look
- `next=`, `returnUrl=`, `redirect=`, login flows, SSO callbacks
### Signals
- Redirect parameter accepts external destinations
- Redirect validation can be bypassed by URL parsing tricks
### Safe validation steps
- Confirm whether redirects are restricted to internal paths or strict allowlists
- Verify normalization before validation (scheme/host/encoding)

## Fix patterns
- Allowlist internal paths only (preferred)
- If external redirects are required: strict allowlist of hosts + robust URL parsing
- Avoid reflecting redirect targets in the response body

## Verification (after fix)
- External URLs are rejected
- Edge-case parsing/encoding does not bypass validation

## Resources
- OWASP: Unvalidated Redirects and Forwards
