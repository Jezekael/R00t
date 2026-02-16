# HTTP Header Injection (CRLF)
**Category:** Web-Server  
**Severity (typical):** Medium to High (depends on cache/proxy and sinks)  
**CWE / OWASP:** CWE-113

## Overview
HTTP header injection occurs when untrusted input is used to build HTTP headers without removing CR/LF characters, allowing attackers to inject or manipulate headers. In some setups it can enable cache poisoning or response splitting behavior.

## Real-world impact
- Cache poisoning / content confusion via injected headers
- Cookie injection or security header manipulation in some chains
- Redirect poisoning if Location/header logic is affected

## Common root causes
- Setting headers from user input (Location, Content-Disposition filenames) without sanitizing CR/LF
- Framework misuses or unsafe header concatenation
- Proxy/cache behavior differences

## Detection & validation
### Where to look
- Redirect endpoints, download endpoints (filename), proxy headers
### Signals
- Header values reflect user input
- Unexpected duplicated headers or altered response behavior
### Safe validation steps
- Confirm the app rejects/strips CR and LF in any header-bound input
- Review caches/proxies in front of the app (impact multiplier)

## Fix patterns
- Reject or strip `\r` and `\n` from any value used in headers
- Use framework-safe header setters (not raw concatenation)
- Harden cache configuration and validate redirect targets

## Verification (after fix)
- Inputs cannot inject new header lines
- Security headers remain consistent under test cases

## Resources
- OWASP: HTTP Response Splitting / Header Injection references
- CWE-113
