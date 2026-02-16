# File Upload Security
**Category:** Web-Server  
**Severity (typical):** High to Critical (RCE possible)  
**CWE / OWASP:** CWE-434 / OWASP A03 (injection chains), A05 (misconfig)

## Overview
File upload issues occur when an application allows users to upload files that are interpreted in a dangerous way (executed, parsed as active content, or used to overwrite/poison server-side processing). The risk depends on validation, storage location, and how uploads are served/processed.

## Real-world impact
- Remote code execution (worst case, if server executes uploaded content)
- Stored XSS (e.g., SVG/HTML uploads served as active content)
- Sensitive file overwrite / configuration poisoning
- Malware hosting and reputational damage

## Common root causes
- Validation based only on filename extension or client-provided MIME type
- Serving uploads directly from a web-executable directory
- Content sniffing / incorrect Content-Type on responses
- Using user-controlled filenames/paths
- Unsafe parsers (image/document processing) without sandboxing

## Detection & validation
### Where to look
- Avatar uploads, attachments, imports, document conversions, media upload APIs

### Signals
- Uploaded files are accessible via predictable URLs
- Server responds with permissive Content-Type
- Filenames preserved and reflected in paths/headers
- Different validation behavior between UI and API endpoints

### Safe validation steps
- Determine: where files are stored, how they are served, what Content-Type is returned
- Check whether the upload directory is non-executable
- Confirm server-side validation (magic bytes) and strict allowlists

## Exploitation notes (high-level)
- Risk is highest when uploads are executed or interpreted as active content
- Even “image only” uploads can be risky if processing libraries are vulnerable

## Fix patterns
- Strict allowlist by content (magic bytes) + size limits
- Store outside web root; serve via a safe download handler
- Randomize filenames, strip metadata, avoid user-controlled paths
- Set safe response headers: correct Content-Type, `Content-Disposition`, disable sniffing
- Sandbox file processing (separate service/container)

## Verification (after fix)
- Disallowed content types are rejected server-side
- Upload URLs are not executable and do not render active content unexpectedly
- Response headers are correct and consistent

## Resources
- OWASP: Unrestricted File Upload
