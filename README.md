# Build a plugin once and use it everywhere with GitHub Copilot!

A 15-minute lightning session: your existing **5-minute opening**, then a
**10-minute demo and close**. Package one reusable skill and Figma MCP
integration, then use that same package in VS Code, Copilot CLI, and Copilot app.

Start with the [demo guide](docs/demo-guide.md) for setup and exact prompts.
Use the [facilitator script](docs/facilitator-script.md) for timing and transitions.
No deck file was present in this repository; the script maps to deck sections
rather than inventing slide numbers.

## What is in the package?

```text
plugin.json                              Agent Plugins 1.0 manifest
mcp.json                                 Portable Figma MCP configuration
skills/web-design-guidelines/SKILL.md     Portable, original workshop skill
com.github.copilot/agents/                Optional Copilot-specific reviewer
com.github.copilot/rules/                Always-on Copilot-specific guardrails
.github/plugin/marketplace.json          Catalog for discovery and app install
demo/                                    Local brief, starter, prepared result
docs/                                    Demo guide and facilitator script
scripts/validate.py                      Dependency-free workshop checks
```

The shared workflow requires only the skill and MCP server, not the custom
agent. No hooks, credentials, framework dependencies, or remote assets are bundled.
The similarly named `web-design-guidelines` skill is self-contained workshop
content, not a vendored third-party skill.

## Quick local rehearsal

From the repository root, with Python 3 and a current Copilot CLI installed:

```sh
python3 scripts/validate.py
copilot --plugin-dir .
```

In that CLI session, use the fallback review prompt from the demo guide.
Open `demo/index.html` directly in a browser to see the starter, or run:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory demo
```

Visit <http://127.0.0.1:8000/>. The prepared result is at
<http://127.0.0.1:8000/reference.html>. Stop the server with Ctrl+C.
The signup is local-only; no email is sent or stored.

**Scope of proof:** offline checks validate package structure, local links, and
fixture invariants. They do not prove client loading, skill selection, browser
accessibility, or an authenticated Figma round trip. Complete the three-client
preflight in the demo guide before presenting those as live results.
