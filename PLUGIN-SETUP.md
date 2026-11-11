# Figma-to-web demo plugin

This folder is an Agent Plugins 1.0 package. It includes a portable
`web-design-guidelines` skill and Figma MCP configuration, an optional
Copilot-specific review agent, and a tiny signup-page fixture.

## Install from this folder

Extract the ZIP and open a terminal in the extracted `figma-to-web` folder.

- **VS Code:** run **Chat: Install Plugin from Source** and select this folder.
  Start a new Copilot chat and inspect the installed plugin and skill.
- **Copilot CLI, temporary session:** run `copilot --plugin-dir .`.
- **Copilot CLI, persistent local install:**

  ```sh
  copilot plugin marketplace add .
  copilot plugin install figma-to-web@building-plugins-workshop
  copilot plugin list
  ```

  These commands change the CLI's local plugin configuration. To remove the
  plugin later, run `copilot plugin uninstall
  figma-to-web@building-plugins-workshop`, then
  `copilot plugin marketplace remove building-plugins-workshop`.
- **GitHub Copilot app:** the app installs plugins from a GitHub repository or
  Git URL marketplace, not from this ZIP or a local folder. Make this package
  available at an approved hosted Git ref, then add that marketplace in
  **Customize** and install `figma-to-web`. No repository is published by this
  ZIP.

## Try the no-credential rehearsal

Use the normal Copilot agent and ask:

```text
Use the web-design-guidelines skill in local rehearsal mode. Do not call Figma
or any external service. Compare demo/index.html with demo/design-brief.md.
First report the seeded issues without editing. Then fix only demo/index.html
to match the brief. Preserve its local-only form behavior and add no dependencies.
Run python3 scripts/validate.py and summarize the changes and checks actually
performed. Label the source as a synthetic local brief, not Figma.
```

The starter contains a heading-level jump, a placeholder-only email field, and
hidden focus styling. `demo/reference.html` is a prepared fixed result. Open
either file directly, or serve the folder with
`python3 -m http.server 8000 --bind 127.0.0.1 --directory demo`. The form never
sends or stores an email.

## Live Figma mode

Replace the local brief in your prompt with a link to a Figma frame you are
authorized to read. Enable the plugin's Figma server and complete the client's
sign-in/consent flow if supported. The remote endpoint is
`https://mcp.figma.com/mcp`; credentials are never placed in this package.

Figma currently restricts its remote MCP server to clients in its MCP catalog.
Check the current catalog and successfully retrieve design context on each
client before claiming a live integration. Generic MCP configuration does not
guarantee that Copilot CLI or the Copilot app can authenticate. If a client
cannot connect, use the local rehearsal prompt and say that Figma was not
called.

See `docs/demo-guide.md` for exact prompts, troubleshooting, and preflight
details. The local validator checks package structure and fixtures; it does not
test authentication, client execution, or browser accessibility.
