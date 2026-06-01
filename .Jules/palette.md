## 2025-05-14 - Skip to Content for Keyboard Accessibility
**Learning:** Keyboard-only users and screen reader users must tab through every navigation link on every page load before reaching the main content. A "Skip to Content" link provides a fast path to the primary information, reducing interaction fatigue.
**Action:** Implement a skip link as the first focusable element on the page, targeting the main content container with `tabindex="-1"` to ensure focus shifts correctly.
