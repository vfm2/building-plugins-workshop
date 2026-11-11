# Demo guide

## Outcome and boundaries

Show one package supplying the same design-to-web instructions and Figma tool
connection across three Copilot surfaces. A plugin packages capabilities; it is
not a Figma editor plugin or a VS Code extension. Installation, permissions,
OAuth state, client support, and conversation history do not automatically
travel with the package.

The shared files are root `plugin.json`, root `mcp.json`, and
`skills/web-design-guidelines/SKILL.md`. The optional reviewer lives in
`com.github.copilot/agents/design-reviewer.agent.md`; it is not a portable
standard component and may not appear in every client.

## Prepare before the session

- Have current VS Code with Copilot, Copilot CLI, and Copilot app installed,
  signed in, and permitted by your organization's policies. Use the Copilot
  harness in VS Code. Python 3 serves the static sample and runs local checks.
- Review every package file before installation. There are no hooks or local
  MCP executables, but installing a plugin still grants capabilities.
- Use a disposable rehearsal branch or copy, not a production worktree. Keep
  all clients pointed at the same local checkout, or explicitly carry the diff
  between their isolated worktrees. A plugin does not synchronize source code.
- Disable a separately installed skill with the same `web-design-guidelines`
  name for rehearsal, or inspect the loaded skill's path to disambiguate.
- For live mode, choose a small design frame you are authorized to read.
  In Figma, **Copy link to selection** and retain its node ID. Do not use a
  fabricated example URL, private customer design, or public link without access.
  Use the local brief's signup card as a suggested frame to create yourself.
- For the exact three seeded findings, use the local brief. A different live
  Figma design can produce different findings and should not be forced to match.

### Figma authentication and access

The bundled server uses Figma's documented remote endpoint,
`https://mcp.figma.com/mcp`, with the Agent Plugins transport name
`streamable-http`. Do not replace it with VS Code's native `servers` /
`type: http` configuration: that is a different file format.

Start or enable the plugin's Figma server using each client's MCP controls and
complete the browser sign-in/consent flow if offered. VS Code exposes **MCP:
List Servers**. In Copilot app, inspect **Customize > Installed**, find the MCP
server, and choose **Sign in** when offered. CLI users should use the current
`/mcp` controls and their installed version's help. Credentials belong in the
client's authentication store, never in `mcp.json`, headers, prompts, or commits.
Do not install a second standalone Figma server just for this demo.

Figma's remote-server docs restrict connections to supported/catalog clients.
Generic HTTP transport support alone does not guarantee Figma OAuth access in
CLI or app. Check the [Figma catalog](https://www.figma.com/mcp-catalog) and
rehearse a real design-context call on each surface. Account permissions, seat
eligibility, and tool limits also apply. If any surface cannot connect, explicitly
switch to the local path below; do not claim a three-surface live MCP proof.

## Install the same package

Run commands from this repository's root. For local authoring, no remote
publication is needed in VS Code or CLI.

| Surface | Setup | Verify in a fresh session |
| --- | --- | --- |
| VS Code | Enable `chat.plugins.enabled` if needed. Run **Chat: Install Plugin from Source**, choose this repository's absolute local folder, and select the intended workspace/harness. | In **Chat: Open Customizations**, inspect the enabled `figma-to-web` plugin, its skill and Figma server. |
| Copilot CLI | Run `copilot --plugin-dir .` for a session-local development mount. For persistent installation on versions supporting local sources, run `copilot plugin install .`, then `copilot plugin list`. | Inspect the loaded skill's source and Figma tools. A development mount is not a persistent install; exit to remove it. |
| Copilot app | In **Customize**, use marketplace settings to add the GitHub repository or Git URL hosting this catalog. Browse for `figma-to-web`, review, then **Install**. | In **Customize > Installed**, confirm enablement, inspect the skill and MCP entry, and open a fresh repository session. |

**App publication prerequisite:** the marketplace and plugin must already exist
at the Git ref the app fetches. Uncommitted files in this checkout are not
available from a GitHub URL. Publish the prepared revision through your normal
review process before the event; then add
`https://github.com/vfm2/building-plugins-workshop` if that revision is on its
default branch. For another published revision, use a supported ref-pinned
source and verify it, or a separately published rehearsal repository. Do not
assume app installation sees this branch or that a CLI development mount is
automatically an app install. This workshop does not publish or push for you.

The supplied `.github/plugin/marketplace.json` catalogs the root plugin as
`figma-to-web@building-plugins-workshop`. After publication, CLI marketplace
installation is also available:

```sh
copilot plugin marketplace add vfm2/building-plugins-workshop
copilot plugin install figma-to-web@building-plugins-workshop
copilot plugin list
```

Do not combine a development mount with an installed copy in one session.
Use the source plugin files to make changes, not a client's installation cache.
After updates, reload/reinstall as appropriate and start a fresh session.

For a **verified persistent local CLI installation** without publishing, use the
included catalog:

```sh
copilot plugin marketplace add .
copilot plugin install figma-to-web@building-plugins-workshop
copilot plugin list --json
```

These commands were tested in an isolated `COPILOT_HOME` during authoring.
The installed CLI loaded the root package live and reported one installed
skill. That verifies discovery/installation, not skill execution or Figma auth.
For normal use, these commands change your CLI configuration. To remove this
workshop installation afterward, first run
`copilot plugin uninstall figma-to-web@building-plugins-workshop`, then
`copilot plugin marketplace remove building-plugins-workshop`.

## Exact prompts and cross-surface flow

Use the normal Copilot agent for the shared proof. Asking to use a skill is
portable; a particular slash-command spelling is not. Watch the activity trace
for loading this plugin's skill. Manually reading its file is a diagnostic,
not evidence of automatic plugin discovery.

### 1. VS Code: inspect the package, then get design context (2 minutes)

Open the manifest, skill, and MCP file. With live access, replace
`<PASTE_YOUR_FIGMA_SELECTION_LINK>` before sending:

```text
Use the figma-to-web plugin's web-design-guidelines skill. Read design context
and a screenshot for <PASTE_YOUR_FIGMA_SELECTION_LINK> using the available
Figma MCP tools. Compare that design with demo/index.html. Do not edit any
files or write to Figma. Report at most three actionable findings with
file:line, source/check, and smallest fix. State which source and tools you
actually used. If access fails, stop and report the failure.
```

Show the actual context/tool response, not just a connected badge.
Do not send local implementation content to Figma; retrieve only the design.

**Credential-free replacement prompt:**

```text
Use the figma-to-web plugin's web-design-guidelines skill in local rehearsal
mode. Do not call Figma or any external service. Compare demo/index.html
against demo/design-brief.md without editing files. Report the three seeded
issues with file:line, source/check, and smallest fix. Label the source as a
synthetic local brief, not Figma. State any browser checks not performed.
```

Expected local findings: H1 to H3 jump, missing persistent associated email
label, and removed keyboard focus outline. If fewer appear, inspect the loaded
skill source and the actual starter file rather than asserting success.

### 2. CLI: apply the same workflow (2 minutes)

Open the same checkout and start `copilot --plugin-dir .`. Use this local
prompt, or the live variant immediately below:

```text
Use the figma-to-web plugin's web-design-guidelines skill in local rehearsal
mode. Do not call Figma or any external service. Fix only demo/index.html to
meet demo/design-brief.md: correct the heading level, add a visible associated
email label, and restore visible keyboard focus. Preserve the local-only form
behavior and responsive layout. Do not copy demo/reference.html. Run
python3 scripts/validate.py, then summarize the source, diff, and checks
actually performed. Do not claim browser checks unless you perform them.
```

For a live run with a preflighted matching frame:

```text
Use the figma-to-web plugin's web-design-guidelines skill. Retrieve design
context and a screenshot for <PASTE_YOUR_FIGMA_SELECTION_LINK> using Figma MCP.
Implement that design in demo/index.html only, keeping the local-only form
behavior and adding no dependencies or remote assets. Do not write to Figma.
If access fails, stop and report it. Run python3 scripts/validate.py and
summarize the source, diff, and checks actually performed.
```

The local checks allow the starter to be either seeded or fixed; passing them
alone does not prove a repair. Inspect the diff and perform the manual checks.
Do not use the fixed-result fixture check as an arbitrary live-design oracle.

### 3. Copilot app: review the changed implementation (2 minutes)

Open the same checkout/folder or bring the intended diff into its worktree.
Confirm the file contains the CLI changes before reviewing. Show the installed
plugin and its source; do not re-paste the skill as a prompt.

```text
Use the figma-to-web plugin's web-design-guidelines skill in local rehearsal
mode. Do not call Figma or any external service. Review the current
demo/index.html against demo/design-brief.md without editing files. Report
remaining issues, or say no findings if the three seeded issues are resolved.
Distinguish code inspection from browser checks. Label the source as the
synthetic local brief.
```

For a live three-client proof, replace the local source instructions with:
"Retrieve design context and a screenshot for
<PASTE_YOUR_FIGMA_SELECTION_LINK> using Figma MCP. If access fails, stop and
report it." Remove the sentence labeling the source synthetic. Show the app's
actual tool response too; prior VS Code/CLI responses do not prove app access.

**Optional, only if ahead of time:** select `design-reviewer` in the agent
picker and repeat the review. Explain that this is a Copilot-specific role
wrapper around the same skill. Its no-edit behavior is an instruction, not a
security sandbox. The core demo does not depend on it.

## No-credential and time-box fallback

Use local rehearsal mode on all three surfaces from the start if credentials
or client access have not been verified. Explain: "The brief replaces design
retrieval today. We are demonstrating shared skill behavior, not a live Figma
connection." Keep the MCP configuration visible as the packaged integration.

If agent generation is slow, open `demo/reference.html` as the **prepared
result**, compare it to `demo/index.html`, and review the prepared result by
changing the review prompt's target filename. Do not present it as a new live
edit. If app installation is unavailable, show its documented setup and a
previously captured, labeled rehearsal result if you have one. Otherwise state
that app execution remains unverified. Do not invent a recording or result.

For repeat rehearsals, save a pristine starter copy before making edits.
Restore only your own rehearsal changes, with a reviewed diff. Do not reset a
shared worktree or discard other people's changes.

## Validation and preflight evidence

```sh
python3 scripts/validate.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory demo
```

Visit the page, Tab through it, click the label, submit a dummy email, and check
320px width. Use `reference.html` for the expected fixed behavior. Ctrl+C stops
the server. The Python check uses only the standard library and verifies this
workshop's manifest/config shapes, catalog consistency, skill metadata, local
Markdown links, and known sample invariants. It is not a general JSON Schema
validator or an accessibility audit.

Record before presenting, without credentials or private design content:

| Surface | Installed plugin/version and skill source | Figma context call or labeled fallback | Task outcome |
| --- | --- | --- | --- |
| VS Code | Not yet recorded | Not yet recorded | Not yet recorded |
| CLI | Not yet recorded | Not yet recorded | Not yet recorded |
| App | Not yet recorded | Not yet recorded | Not yet recorded |

These are a presenter checklist, not claimed validation results. A plugin
listed as installed is weaker evidence than a loaded skill plus a successful
tool response and the intended code/review result.

### Authoring evidence

On 2026-11-10, the eight offline checks passed, and both JSON documents also
passed the official Agent Plugins 1.0 JSON schemas using the available
`jsonschema` validator. Isolated CLI marketplace registration and plugin
installation succeeded on CLI 1.0.105; inventory showed enabled version 1.0.0.
The local HTTP server returned the prepared page, and a browser text snapshot
showed its heading, visible email label, field, and button. Subsequent browser
interaction requests timed out, so form interaction, keyboard focus, and
320px rendering remain manual checks. No live Figma calls or complete
VS Code/CLI/app agent runs were performed.

## Troubleshooting

| Symptom | Action |
| --- | --- |
| Plugin missing | Confirm plugin-capable version, Copilot harness, enablement and organization policy. Use the package root, not `skills/`, as the source. |
| Old or duplicate skill | Inspect source path, disable the duplicate, refresh/reinstall the source, and start a fresh session. |
| MCP parser error | Keep the root portable format: `$schema`, `mcpServers`, `type: streamable-http`. Do not paste native client configuration into it. |
| Figma sign-in missing/fails | Check the supported-client catalog, MCP server controls and consent flow. Do not add tokens to headers. Switch to labeled fallback after 20 seconds on stage. |
| Design denied or tool quota reached | Check file access and current Figma plan/seat limits before the event. Use the local brief rather than retrying throughout the talk. |
| CLI local install rejected | Use the documented development mount `copilot --plugin-dir .`; inspect your installed CLI's help. Do not assume CLI flags are identical in the app. |
| App cannot find this plugin | Ensure catalog and root plugin are published at the fetched ref, then refresh the marketplace. A local mount does not publish it. |
| App reviews old code | Check its worktree and target file; carry the CLI diff explicitly if workspaces differ. |
| Port 8000 busy | Stop only your own server or choose another port and update the browser URL. |

Local CLI 1.0.105 accepted `--plugin-dir` in its help but rejected
`copilot plugin install .` as an invalid source during authoring. Use the
development mount for that version; do not treat the persistent local-source
example in newer documentation as verified on every installed build.

## Official resources

Setup/capability references consulted on 2026-11-10; recheck before presenting:

- [Agent Plugins manifest](https://agent-plugins.org/plugin-authors/manifest)
- [Portable MCP format and authentication limits](https://agent-plugins.org/plugin-authors/mcp-servers)
- [VS Code plugin authoring reference](https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference)
- [VS Code plugin installation](https://code.visualstudio.com/docs/agent-customization/agent-plugins)
- [Copilot CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference)
- [Copilot app customization and marketplace installation](https://docs.github.com/en/copilot/how-tos/github-copilot-app/customize-github-copilot-app)
- [Create and share a marketplace](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/create-and-share-plugin-marketplaces)
- [Figma remote setup and supported-client restrictions](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
- [Figma tools and prompts](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)
