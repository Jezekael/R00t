# JavaScript — Obfuscation
**Category:** Web-Client

## What it is
Obfuscation is deliberate transformation of JavaScript to make it hard to read (renaming, encoding strings, control-flow flattening, packing). In CTFs, it often hides secrets/logic; in the wild, it hides IP or malicious behavior.

## What it enables / impact
- Hides client-side logic flaws (auth checks, feature gates)
- Conceals secrets mistakenly embedded in client code
- Slows analysis and reverse engineering (but does not prevent it)

## Preconditions / requirements
- The relevant logic/secret is actually present in the client-side code
- You can retrieve the JS bundle(s) from the application

## How to recognize (recon)
### Where to look
- Minified bundles, inline scripts, dynamically loaded JS
- Service workers, source maps (`.map`), webpack chunk files

### Indicators
- Unreadable variable names, large encoded strings, eval-like constructs
- Many small functions, strange arithmetic/string decoding
- Suspicious runtime decoding patterns

### Quick tests (high-level)
- Beautify + rename symbols progressively
- Identify entry points (event handlers, auth checks, API calls)
- Search for keywords (endpoints, “token”, “admin”, “secret”, “flag”)

## Common variants
- Simple minification vs heavy packing (string arrays/decoders)
- Control-flow flattening
- Webpack bundles with hidden modules

## Mitigations (blue-team view)
- Never rely on client-side secrecy for access control
- Keep secrets server-side; use short-lived tokens issued server-side
- Assume JS is readable by attackers; design accordingly

## Resources
- MDN: JavaScript debugging in DevTools
- Webpack: source maps overview

**Related challenges:** 
- Root-Me: Web-Client Javascript - Obfuscation (series)