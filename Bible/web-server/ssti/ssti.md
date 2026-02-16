# Server-Side Template Injection (SSTI)
**Category:** Web-Server  
**Severity (typical):** High to Critical (can lead to RCE depending on engine)  
**CWE / OWASP:** CWE-94/95 family (code injection patterns), OWASP Injection

## Overview
SSTI occurs when user input is evaluated by a server-side templating engine as template syntax. This can expose data from the template context and sometimes enable code execution or sensitive actions, depending on the engine and sandboxing.

## Real-world impact
- Exposure of secrets (config, environment variables, internal objects)
- SSRF/file reads depending on template capabilities and app wiring
- Potential remote code execution in worst-case configurations

## Common root causes
- Rendering user-controlled strings as templates (e.g., “custom email template”, “preview” features)
- Overly powerful template context exposed to user content
- Insecure sandboxing or outdated engine escape paths
- Treating templates as “safe” because they’re not “code”

## Detection & validation
### Where to look
- Email templating, PDF/report generation, notification systems
- “Preview your message/signature/template” features
- CMS-like “custom page” builders

### Signals
- Template engine names in errors/logs
- Rendering behavior that transforms expressions/filters
- Differences between stored input and rendered output

### Safe validation steps
- Determine whether user input is rendered as template logic vs plain text
- Fingerprint the engine via error messages (if present) or technology stack knowledge
- Validate whether template rendering has access to sensitive context objects

## Exploitation notes (high-level)
- Severity depends on: engine (Jinja/Twig/etc.), sandbox, exposed objects, and output channels
- Stored SSTI (saved template rendered later) can increase impact and reach

## Fix patterns
- Never render untrusted input as template code
- Use strict allowlists for template variables and filters (if user templating is required)
- Harden context: pass only minimal data required
- Sandbox + least privilege + egress restrictions as defense-in-depth

## Verification (after fix)
- Untrusted input is treated as data (escaped), not executed as template syntax
- Template context does not expose sensitive objects
- Tests cover “preview” flows and stored template flows

## Resources
- PortSwigger: SSTI
- Engine-specific docs (Jinja2/Twig/etc.)

**Related labs/challenges (optional):**
- Root-Me SSTI
