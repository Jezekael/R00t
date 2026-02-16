# LDAP Injection
**Category:** Web-Server  
**Severity (typical):** Medium → High (can be Critical if it enables auth bypass)  
**CWE / OWASP:** CWE-90 / OWASP Top 10: A03 Injection :contentReference[oaicite:0]{index=0}

## What it is
LDAP injection happens when user-controlled input is inserted into an LDAP query (most often an LDAP **search filter**) without proper escaping/encoding, allowing an attacker to change the query logic. :contentReference[oaicite:1]{index=1}

## What it enables / impact
- Authentication bypass (depending on how the LDAP filter is used in login logic). :contentReference[oaicite:2]{index=2}  
- Unauthorized directory data access (user enumeration, attribute leakage like emails, groups, phone numbers). :contentReference[oaicite:3]{index=3}  
- Business impact via identity compromise (access to internal apps relying on LDAP/AD auth). :contentReference[oaicite:4]{index=4}

## Preconditions / requirements
- The application constructs LDAP filters or DNs by concatenating strings that include untrusted input. :contentReference[oaicite:5]{index=5}  
- Lack of correct escaping for the **specific LDAP context**:
  - **Search filter escaping** (for `(uid=...)`, `(&(a=b)(c=d))`, etc.)
  - **DN escaping** (when input is used in a Distinguished Name) :contentReference[oaicite:6]{index=6}

## How to recognize (recon)
### Where to look
- Enterprise login forms using LDAP/Active Directory (AD) behind the scenes
- “Search user” / directory lookup features (autocomplete, staff directory)
- Password reset flows (lookup by username/email)
- Admin panels that query groups/roles from LDAP

### Indicators
- Error messages that mention LDAP parsing / filter syntax / directory server issues (sometimes only in logs)
- Different behavior when inputs contain LDAP special characters used in filters (e.g., `*`, `(`, `)`, `\`, NUL). :contentReference[oaicite:7]{index=7}  
- User enumeration signals (different responses for “user not found” vs “wrong password”)

### Quick tests (high-level)
- Map the exact request that triggers the LDAP lookup (which field, which endpoint, which parameters)
- Check whether the application:
  - rejects special filter metacharacters, or
  - escapes them consistently (server-side), and
  - produces identical outcomes when given “syntactically interesting” inputs (no logic change)
- If you have code access: verify the filter is built using safe APIs or correct LDAP escaping functions for the relevant context. :contentReference[oaicite:8]{index=8}

## Common variants
- **Auth filter manipulation**: login logic uses a filter like `(uid=<input>)` or `(&(uid=<u>)(userPassword=<p>))` and can be altered if input isn’t escaped. :contentReference[oaicite:9]{index=9}  
- **Search feature injection**: directory search endpoints (often easier to reach than auth)
- **DN injection**: untrusted input used to build a DN string (different escaping rules than filters). :contentReference[oaicite:10]{index=10}

## Mitigations (blue-team view)
- **Escape untrusted data correctly for LDAP context**:
  - Use **LDAP Search Filter escaping** when building filters
  - Use **LDAP DN escaping** when building DNs :contentReference[oaicite:11]{index=11}  
- Prefer **safe LDAP query-building APIs/libraries** over string concatenation. :contentReference[oaicite:12]{index=12}  
- Standardize authentication errors (avoid user enumeration).
- Apply least privilege to directory binds (service account should only read what’s needed).

## Resources
- OWASP: LDAP Injection Prevention Cheat Sheet :contentReference[oaicite:13]{index=13}  
- PortSwigger: LDAP injection (issue definition + risk) :contentReference[oaicite:14]{index=14}  
- MITRE: CWE-90 :contentReference[oaicite:15]{index=15}  

**Related challenges:** 
- (Optional) Root-Me: LDAP injection – authentication
