## 2026-06-17 - [Accessible Skip Navigation]
**Learning:** When implementing a "Skip to Content" link, the target element (e.g., <main>) must have `tabindex="-1"` to ensure it can programmatically receive focus in all browsers, even if it is not naturally focusable.
**Action:** Always include `tabindex="-1"` on the main content container when it's the target of a skip link.
