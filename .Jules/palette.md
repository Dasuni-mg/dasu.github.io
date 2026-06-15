## 2026-06-15 - [Skip to Content Accessibility]
**Learning:** Implementing a "Skip to Content" link requires both a visible-on-focus link and a semantic <main> landmark with tabindex="-1" to ensure focus is correctly managed across all browsers, especially when the target is not naturally focusable.
**Action:** Always pair skip links with a clear <main id="main-content" tabindex="-1"> target.
