# Figma to Web — GitHub Copilot Plugin

One plugin packages a **Design-to-Code Agent**, **web-design-guidelines skill**, and **Figma MCP integration**. Use it to turn a Figma frame into an accessible, responsive UI in your own project.

## What's inside

```text
plugin.json
mcp.json
com.github.copilot/agents/design-to-code.agent.md
skills/web-design-guidelines/SKILL.md
```

- **Agent:** coordinates design retrieval, implementation, and review on supported Copilot clients.
- **MCP:** provides access to Figma design context after the client is authenticated and connected.
- **Skill:** supplies reusable UI quality and accessibility guidance.

The skill and MCP configuration use the Agent Plugins 1.0 layout. The custom agent is a Copilot-specific component; exact availability varies by client.

## Try the workshop

1. Open the separate starter repository: `deployment-pipeline-demo`.
2. Install or load this plugin in your supported Copilot client. For a local Copilot CLI rehearsal from **this plugin repository**, run `copilot --plugin-dir .` (use your current CLI's supported plugin loading flow).
3. Connect/authenticate the Figma MCP server if prompted.
4. Select the `design-to-code` agent where supported, and give it a Figma **frame link** and the target `index.html`.
5. Ask the agent to implement the design and simulate Build → Test → Deploy.
6. Open `index.html` in a browser to see the result.

### Example prompt

> Use the design-to-code agent and the web-design-guidelines skill. Retrieve this Figma frame with Figma MCP: [FRAME_URL]. Implement the design in `index.html` in the open starter repository. Build an interactive local Build → Test → Deploy simulation with accessible status updates, keyboard focus, responsive layout, and reduced-motion support. Do not add dependencies or perform a real deployment. Explain which MCP tools and skill guidance you used.

## Client note

Agent, skill, and MCP discovery can differ across VS Code, Copilot CLI, and Copilot App. Test the exact installation, agent selection, and Figma authentication flow in each client before presenting it live. If a client doesn't expose the custom agent, demonstrate the shared skill/MCP functionality there and state that distinction explicitly.

## Workshop architecture

**Plugin repository** (this repo) → reusable agent, skill, MCP config.  
**Starter application repository** (`deployment-pipeline-demo`) → intentionally plain HTML app.  
**Figma** → target appearance, layout, and component states.

No finished implementation is bundled with the public starter app. Keep a private rehearsal copy for a fallback.
