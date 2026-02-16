# SQL Injection (SQLi)
**Category:** Web-Server  
**Severity (typical):** Critical (data breach / auth bypass common)  
**CWE / OWASP:** CWE-89 / OWASP Top 10: A03 Injection

## Overview
SQL injection happens when untrusted input is incorporated into SQL queries in an unsafe way, allowing attackers to change query logic. It commonly affects authentication, search/filter endpoints, report generation, and any feature that builds SQL dynamically.

## Real-world impact
- Data breach (PII, credentials, financial records)
- Authentication bypass / privilege escalation
- Data tampering or deletion
- In some environments: pivot to OS command execution via DB extensions or misconfig

## Common root causes
- String concatenation to build SQL
- ORM misuse (raw queries/fragments) without parameter binding
- Dynamic identifiers (ORDER BY, column names) without allowlists
- Verbose error handling exposing SQL errors
- Weak separation of privileges for DB accounts

## Detection & validation
### Where to look
- Login forms, search, filters, pagination, sorting, `id=` parameters
- Admin/report endpoints (often more dynamic queries)

### Signals
- SQL errors (syntax errors, DB error codes)
- Response differences correlated with controlled input changes
- Timing differences correlated with controlled input changes
- Unexpected data returned or authentication anomalies

### Safe validation steps
- Establish baseline behavior and error handling
- Identify whether inputs are parameterized (code review if possible; black-box by behavior)
- Confirm injection class:
  - Error-based: errors disclose SQL/DB hints
  - Boolean-based blind: content changes predictably
  - Time-based blind: timing changes predictably

## Exploitation notes (high-level)
- Reliability depends on DB type, query structure, WAF behavior, and response stability
- Severity increases when the DB user is over-privileged or when sensitive tables are reachable
- Chaining is common: SQLi → read secrets → access other systems

## Fix patterns
- Use prepared statements / parameterized queries everywhere
- Avoid dynamic SQL identifiers; if needed, enforce strict allowlists
- Centralize error handling; never return DB errors to clients
- Enforce least privilege for DB accounts
- Add monitoring for anomalous query patterns and slow queries

## Verification (after fix)
- Inputs are bound parameters (not interpolated strings)
- Attempts to break query structure do not change server behavior
- Error messages no longer disclose DB internals
- Regression tests cover the previously vulnerable endpoints

## Resources
- OWASP: SQL Injection
- PortSwigger: SQL injection

**Related labs/challenges (optional):**
- Root-Me SQLi (string/error/time/auth)
