---
name: web-design-guidelines
description: Apply practical accessibility, interaction, responsive layout, and UI quality guidelines when implementing or reviewing web interfaces.
---

# Web design guidelines

Use this skill when asked to implement UI from a design, review a web page, or improve usability and accessibility.

## Implementation checklist
- Use semantic HTML: headings in order, meaningful labels, real buttons for actions.
- Ensure keyboard access, visible focus indicators, and predictable tab order.
- Provide accessible status updates for asynchronous progress (`role="status"` or `aria-live="polite"`), without announcing every animation frame.
- Pair icons and colors with readable text; maintain strong foreground/background contrast.
- Use responsive layouts and avoid horizontal scrolling on narrow screens.
- Support `prefers-reduced-motion` for nonessential animations.
- Preserve clear loading, disabled, success, and error states; don't make inactive controls look interactive.
- Avoid unnecessary dependencies, remote assets, and speculative behavior.

## Review output
Give up to five actionable findings with file/line references when possible, severity, and a specific fix. Clearly distinguish inspected code from tested behavior. If asked to implement, apply the fixes and summarize the result.
