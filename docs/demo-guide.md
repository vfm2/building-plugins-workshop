# Ignite — 10-minute demo guide

**Session:** Build a plugin once, use it everywhere with GitHub Copilot  
**Opening:** 5 minutes (your existing slides)  
**Demo:** 10 minutes  
**Scenario:** Implement a Figma deployment-status component with the same `figma-to-web` plugin across three Copilot clients.

## Before the session

- [ ] Open the plugin repo, Figma desktop frame, VS Code, CLI, Copilot App, and both demo HTML pages.
- [ ] Verify `figma-to-web` and the correct `web-design-guidelines` skill in each client.
- [ ] Test Figma design-context retrieval in the client(s) where you will demonstrate it.
- [ ] Confirm all clients use the same checkout or intentionally transfer code changes.
- [ ] Keep `demo/deployment-reference.html` open as a labeled prepared fallback.
- [ ] Save a clean starter copy / branch for repeatable rehearsals.
- [ ] Check the actual deployment HTML file paths; do not overwrite the original signup sample accidentally.

## Run of show

| Clock | Action | Message |
| --- | --- | --- |
| 0:00–5:00 | Existing intro | What plugins are and why reusable capabilities matter |
| 5:00–6:15 | Show `plugin.json`, `mcp.json`, `SKILL.md` | One package: manifest, tools, instructions |
| 6:15–8:15 | VS Code + Figma MCP | Retrieve the design and identify implementation requirements |
| 8:15–11:15 | Copilot CLI | Implement the component and inspect the diff |
| 11:15–13:30 | Copilot App | Review the result using the same skill |
| 13:30–15:00 | Browser reveal + close | Run the simulation; share the repo |

### Transition from your intro

> We've seen why plugins are useful. Now let's use one package to turn a Figma design into a working UI across three Copilot environments. The Figma MCP server supplies design context, and the reusable skill helps us apply web interface guidelines.

## 1. VS Code — inspect the Figma design

Open `plugin.json`, `mcp.json`, and `skills/web-design-guidelines/SKILL.md`. Point out their roles, then paste:

```text
Use the figma-to-web plugin and its web-design-guidelines skill.
Using the available Figma MCP tools, retrieve design context and a screenshot for:
<PASTE_FIGMA_FRAME_LINK>

Compare the design with demo/deployment-starter.html and identify the
three most important implementation requirements: visual layout,
interactive behavior, and accessibility. Do not edit any files.
State which tools and skill you actually used. If Figma access fails,
stop and tell me rather than guessing.
```

**Show:** A real Figma tool response and a short plan. The Figma design may not contain behavior requirements; the local brief fills that gap.

**Fallback (label it):**

```text
Use the figma-to-web plugin's web-design-guidelines skill.
Read demo/design-brief.md as a LOCAL synthetic design brief.
Do not call Figma. Compare the brief with demo/deployment-starter.html.
Give me the three most important implementation changes. Do not edit.
```

## 2. Copilot CLI — implement

Start a fresh CLI session from the repo root:

```bash
copilot --plugin-dir .
```

Use this prompt. If CLI has verified Figma access, use the first version:

```text
Use the figma-to-web plugin and its web-design-guidelines skill.
Retrieve the Figma design context for <PASTE_FIGMA_FRAME_LINK> using
Figma MCP. Also read demo/design-brief.md for the simulated interaction
requirements. Implement the design in demo/deployment-starter.html.

Build an accessible, responsive Build → Test → Deploy component with a
working Run deployment simulation, visible stage changes, and success
feedback. Keep it dependency-free and do not trigger real deployments.
Do not copy demo/deployment-reference.html. Summarize the diff and the
checks you actually performed. If Figma access fails, stop.
```

If CLI cannot use Figma, explicitly substitute:

```text
Use the figma-to-web plugin's web-design-guidelines skill.
Use demo/design-brief.md as a LOCAL synthetic design brief; do not call
Figma. Implement the requirements in demo/deployment-starter.html.
Create an accessible, responsive Build → Test → Deploy simulation with
visible stage transitions and success feedback. No dependencies or real
deployments. Do not copy demo/deployment-reference.html. Summarize the
diff and checks performed.
```

**Show:** Skill invocation, file diff, then the page in the browser. If generation runs long, switch to the clearly labeled prepared reference.

## 3. Copilot App — review

Ensure the App sees the updated file. If it uses a different worktree, bring the change across first. Then:

```text
Use the installed figma-to-web plugin's web-design-guidelines skill.
Review demo/deployment-starter.html against demo/design-brief.md.
Check semantic HTML, keyboard operation, visible focus, stage status
announcements, responsive behavior, and reduced-motion support.
Do not modify files. Give me at most three prioritized findings with
file:line references. Distinguish code review from browser tests.
```

If App Figma access is verified, add a request to retrieve the same frame and compare visual fidelity. If not, describe the local brief accurately. **Cross-client plugin reuse does not imply cross-client Figma authentication.**

## 4. Browser reveal and close

Open the updated starter page and click **Run deployment**. Show Build → Test → Deploy transitioning to success. If needed, open the prepared reference instead and say it was generated in advance.

> I defined the plugin once: a reusable skill and an MCP integration. Each Copilot environment can use that same package to support a different part of the workflow. The repository is the blueprint for building your own.

## Emergency fallback

- **Figma fails:** Use `demo/design-brief.md` and explicitly call it a local brief.
- **Generation is slow:** Open `demo/deployment-reference.html` and identify it as a prepared result.
- **App cannot see edits:** Review the reference in the App's accessible checkout; do not imply it sees the CLI's worktree.
- **Skill not loading:** Show the plugin source and explain the intended workflow; don't claim an invocation you cannot verify.

## One important migration note

The existing `scripts/validate.py`, `demo/index.html`, and `demo/reference.html` are for the original signup demo. Do not rename or delete them until you've updated the validator and verified the deployment example. For now, keep the new deployment files alongside them.
