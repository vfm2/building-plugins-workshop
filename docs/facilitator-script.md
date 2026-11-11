# 15-minute facilitator script

**Title:** Build a plugin once and use it everywhere with GitHub Copilot!

**Session description:** In this lightning session, learn how to build one
agent plugin and use it across VS Code, GitHub Copilot CLI, and GitHub Copilot
App. See how portable plugins bring reusable skills and MCP integrations to each
environment while still feeling native. Leave with a practical blueprint for
shipping cross-surface agent experiences.

Keep the existing opening to five minutes. The remaining ten minutes include
the package walkthrough, three-surface demo, resources, and close. This is a
presenter-led demo, not a timed hands-on lab; install and authenticate beforehand.
The repository contains no slide deck, so section names below map to the
confirmed deck structure without assigning slide numbers.

## Before the room opens

Use the [demo guide](demo-guide.md) for setup and copy-ready prompts. Pre-open
the deck, package files, VS Code chat, CLI, app session, and browser preview.
Keep the prepared result available. Check which source mode you will use.

Live mode requires a successful Figma design-context call in each client,
an authorized selection link, and a frame matching the rehearsed task.
Otherwise choose synthetic local mode and label it throughout. Preinstall the
same published revision in the app. Confirm that all clients see the intended
code or prepare to carry a small diff between isolated worktrees.

## Run of show

| Clock | Deck/demo section | Show and do | Useful read-aloud text |
| --- | --- | --- | --- |
| 0:00-1:30 | Existing opening: plugin essentials and formats | Introduce the bundle. Contrast Agent Plugins 1.0 with client-specific formats. | "A plugin is a package for a repeatable workflow. Our portable pieces are a skill and an MCP connection; client-specific additions stay separate." |
| 1:30-3:15 | Existing opening: why plugins | Explain the cost of repeating setup and instructions. Use the design-to-web task as the concrete example. | "I want the same review process wherever I work. The skill carries the process, and MCP supplies the design context." |
| 3:15-5:00 | Existing opening: supported surfaces | Name VS Code, CLI, and app; set the portability boundary. Transition into demo. | "We'll use the same package in three places. Each client still controls installation, authentication, and permissions. Let's follow one design-to-web task." |
| 5:00-6:30 | Demo: build the package once | In VS Code, show root `plugin.json`, `skills/.../SKILL.md`, and `mcp.json`. Point to the schema, checklist, endpoint and transport. Show the three-file blueprint; the prepared files avoid typing boilerplate. | "The schema selects Agent Plugins 1.0. Skills and MCP are discovered in standard locations; I don't list their paths in the manifest. This is the complete portable core." |
| 6:30-8:30 | Demo: VS Code design review | Show the enabled plugin. Run the live source/review prompt, or the exact local replacement. Show a real tool response or explicitly labeled local source, then the findings. | Live: "These findings use context retrieved from my selected Figma frame." Local: "This synthetic brief replaces Figma retrieval today. This run proves skill reuse, not a live MCP connection." |
| 8:30-10:30 | Demo: CLI implementation | Start the local mount and run the matching implementation prompt. Show skill loading, the small diff, and source label. Use prepared output if the edit takes too long. | "I haven't rewritten the workflow for the terminal. The same skill guides the implementation. A local mount is for development; it isn't a publication or permanent install." |
| 10:30-12:30 | Demo: app review | Confirm the updated file in the app checkout, show the installed package, then run review-only. For live mode, show the app's own Figma response too. | "Now the app reviews the changed implementation with the same skill. The conversation didn't move between clients; the reusable package did." |
| 12:30-14:00 | Demo: result and extension boundary | Preview the changed page or clearly marked prepared result. Tab to show focus and click the email label. Point briefly to `com.github.copilot/agents/`. | "The portable workflow stands on its own. This optional reviewer adds a Copilot-specific role, so it lives in the Copilot namespace. Hooks aren't needed for this task." |
| 14:00-15:00 | Resources and close | Return to resources slide; link the repository and official references from the guide. End on the blueprint. | "Start with one repeatable task. Package its instructions as a skill, add the tool connection it needs, and verify both in each target client. Build the package once, then test the experience where people will use it." |

## What counts as the proof?

Show the same `figma-to-web` package/version and skill source on each surface,
not three copied prompts containing all the instructions. For a live MCP claim,
show successful design-context retrieval on each surface. For local rehearsal,
show the same brief, skill-driven edit and review, while explicitly stating the
integration was not exercised. A connected badge alone is not a round trip.

The demo is one task: inspect the design, implement a small improvement, then
review the result. It is not three separate feature tours. Avoid marketplace
administration, OAuth setup, or custom-agent configuration live.

## Time-box decisions

At 20 seconds of authentication/tool failure, say: "This client isn't connected
to Figma, so I'll use our local rehearsal brief." Do not imply the connection
worked. At 45 seconds of generation delay, open the prepared result and name it
as prepared. Move on at the scheduled surface boundary.

If behind at 12:30, skip the custom-agent picker and show its namespaced file
only. If the app cannot run, say that execution is unverified and show its
installation path, not an invented result. Protect the final minute for the
blueprint and resources. Questions can follow the timed session.
