# Local rehearsal design brief

**Synthetic workshop fixture, not exported from Figma.** This brief is the
deterministic source when a presenter has no Figma access. It proves skill reuse
and local implementation/review only, not a live MCP round trip.

Build a single-page workshop signup card:

| Element | Requirement |
| --- | --- |
| Canvas | Pale blue `#eef2ff`, centered card, no remote assets |
| Card | White, max width 32rem, 1.5rem padding, rounded corners |
| Content | One H1: "Build once. Bring it everywhere." |
| Supporting text | "A 15-minute introduction to portable agent plugins." |
| Signup heading | H2: "Get the workshop notes" |
| Field | Visible "Email address" label associated with an email input; autocomplete email |
| Action | Submit button named "Send me the notes", dark blue `#1e3a8a`, white text |
| Text color | `#172554` for headings, body text, and labels |
| Focus | Visible 3px dark blue outline, offset 3px |
| Mobile | Fits a 320 CSS pixel viewport without horizontal scrolling |
| Behavior | Local-only demo form; submission stays on this page and shows a confirmation. No email is sent or stored. |

`demo/index.html` deliberately starts with three review targets: a skipped
heading level, a placeholder-only email field, and a suppressed focus outline.
It otherwise works, so the implementation task can stay small.
`demo/reference.html` is a prepared fixed version for time-boxed rehearsals.

## Manual acceptance checks

Open the page, Tab through the controls, and check that focus is visible on each.
Click the email label to focus the field. Submit a valid dummy address and check
the on-page confirmation; submit an invalid address and check native validation.
At 320 CSS pixels, check that the card, field, and button fit without scrolling
horizontally. A browser/screen-reader check is still needed beyond static checks.
