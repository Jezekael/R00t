# LDAP Injection
**Category:** Web-Server  
**Severity (typical):** Medium to High (auth bypass / data exposure)  
**CWE / OWASP:** CWE-90

## Overview
LDAP injection happens when user input is concatenated into LDAP filters or queries without proper escaping. Attackers can modify filter logic to bypass authentication or query unauthorized directory data.

## Real-world impact
- Authentication bypass in LDAP-backed login flows (worst case)
- User enumeration and directory attribute leakage
- Access to internal identity metadata useful for further attacks

## Common root causes
- Constructing LDAP filters via string concatenation
- Not escaping LDAP special characters according to the LDAP filter syntax
- Overly permissive directory queries and error disclosure

## Detection & validation
### Where to look
- Enterprise login portals, “search user” features, password reset lookups
- Admin tools querying directory users/groups

### Signals
- LDAP syntax errors or directory error messages
- Response changes when input includes filter meta-characters
- Differences between “user not found” vs “bad password” enabling enumeration

### Safe validation steps
- Identify how the filter is built (code review if possible)
- Confirm proper escaping for filter contexts
- Ensure auth logic cannot be satisfied by manipulating filters

## Exploitation notes (high-level)
- Authentication bypass feasibility depends on the specific filter logic and directory permissions
- Even without bypass, enumeration and attribute leakage can be impactful

## Fix patterns
- Use parameterized LDAP APIs or robust escaping for filter contexts
- Validate and normalize inputs (allowlists where possible)
- Standardize auth error messages to reduce enumeration

## Verification (after fix)
- Special characters are escaped; filter logic cannot be altered
- Auth success requires valid credentials, not filter manipulation
- Directory queries return only authorized data

## Resources
- OWASP: LDAP Injection
