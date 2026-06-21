## 2026-06-21 - [Accessibility] Reliable Skip to Content Implementation
**Learning:** For a robust "Skip to Content" feature, simply linking to an ID is often insufficient for screen readers or older browsers to move the focus point. Wrapping the content in a semantic `<main>` tag with `tabindex="-1"` ensures that the focus is programmatically moved to the content area without adding the element to the natural tab order.
**Action:** Always pair "Skip to Content" links with a `<main>` or container element that explicitly handles focus via `tabindex="-1"`.
