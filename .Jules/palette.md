## 2026-06-10 - Skip to Main Content Implementation
**Learning:** When implementing a 'Skip to Main Content' link for accessibility, the target element (e.g., `<main>`) needs `tabindex="-1"` to be programmatically focusable in all browsers when the link is clicked.
**Action:** Always include `tabindex="-1"` on the target of a skip link and wrap primary content in a `<main>` landmark.
