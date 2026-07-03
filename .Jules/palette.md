## 2025-05-14 - Skip to Content Pattern
**Learning:** Implementing a "Skip to Content" link is a high-impact, low-effort accessibility win for keyboard users. Pairing it with a `<main>` landmark with `tabindex="-1"` ensures that focus is correctly moved and managed across all browsers, preventing the "focus loss" that can happen when jumping to non-interactive elements.
**Action:** Proactively check for the presence of a "Skip to Content" link and a `<main>` landmark in all static site projects, especially those with fixed headers and many navigation links.
