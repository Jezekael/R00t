# Path Traversal / Local File Read (LFI-style)
**Category:** Web-Server  
**Severity (typical):** High (secrets disclosure; can chain to RCE)  
**CWE / OWASP:** CWE-22 / OWASP A01 (often paired with misconfig)

## Overview
Path traversal occurs when user input influences a filesystem path and an attacker can escape the intended directory to access other files. In many stacks this results in local file read; in some languages/frameworks it can become “include” behavior (historical LFI), enabling more serious chains.

## Real-world impact
- Disclosure of config/secrets (DB creds, API keys, private keys)
- Exposure of source code or environment files
- Chaining to RCE via uploaded files, logs, or template/config injection (stack-dependent)

## Common root causes
- Accepting raw file paths from users instead of using IDs/allowlists
- Incorrect canonicalization before validation
- Over-permissive file permissions for the app user
- “Convenience” features: file preview, language packs, theme/template loaders

## Detection & validation
### Where to look
- `file=`, `path=`, `page=`, `template=`, download/view endpoints
- Report generation, import/export, media rendering, localization

### Signals
- Errors change as path patterns change (not found vs forbidden vs parse error)
- Partial file content leak
- Different behavior with encoded path separators

### Safe validation steps
- Determine if the app maps IDs → known files (safer) or accepts arbitrary paths (risk)
- Check whether the server enforces confinement to a base directory
- Review which files are readable by the service account (in scope for impact)

## Exploitation notes (high-level)
- Severity increases drastically if secrets/configs are readable
- Many real incidents are “file read → cloud creds → cloud takeover” chains

## Fix patterns
- Do not accept raw paths; use allowlisted file IDs
- Canonicalize (resolve) then validate; enforce path confinement
- Store sensitive files outside web/application-readable directories
- Run with least privilege and containerize/isolate where possible

## Verification (after fix)
- Attempts to traverse outside the base directory fail consistently
- Only allowlisted files are retrievable
- Secrets are not readable by the service account

## Resources
- OWASP: Path Traversal
