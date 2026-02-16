# OS Command Injection
**Category:** Web-Server  
**Severity (typical):** Critical  
**CWE / OWASP:** CWE-78 / OWASP A03 Injection

## Overview
Command injection occurs when untrusted input is passed to system shell commands or dangerous process execution APIs in a way that allows an attacker to alter the command or execute additional commands.

## Real-world impact
- Remote code execution on the host/container
- Data theft, lateral movement, full infrastructure compromise
- Persistence and supply-chain style impact if build/deploy systems are hit

## Common root causes
- Building shell commands with string concatenation
- Using `shell=True` patterns or equivalent without strict control
- Unsafely calling system tools (ping, convert, ffmpeg, git, tar) with user arguments
- Inadequate sandboxing/permissions for the service account

## Detection & validation
### Where to look
- Diagnostics features (ping/DNS lookup), file conversion, backups, admin utilities
- CI/CD or “import/export” features invoking OS tools

### Signals
- Error messages from shell/tools
- Unexpected output that resembles tool output
- Time/resource anomalies triggered by inputs

### Safe validation steps
- Identify where user input reaches process execution
- Confirm whether the app uses safe APIs (argument arrays) vs shell parsing
- Verify service privileges and filesystem/network permissions (impact)

## Exploitation notes (high-level)
- Severity depends heavily on: execution context, sandboxing, egress, secrets available
- Many “minor” injections become critical due to exposed credentials/config

## Fix patterns
- Avoid shell; use safe libraries or exec APIs with argument arrays
- Strong allowlists for any user-controlled arguments
- Run with least privilege, isolate and sandbox execution
- Add timeouts, resource limits, and audit logs

## Verification (after fix)
- Inputs cannot alter execution behavior beyond allowed values
- No shell parsing is used
- Execution environment is least-privileged and restricted

## Resources
- OWASP: Command Injection
- PortSwigger: OS command injection
