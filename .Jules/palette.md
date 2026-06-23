## 2024-05-24 - Skip to Content for Accessibility
**Learning:** In a static portfolio with a fixed/sticky navigation, a "Skip to Content" link is essential for keyboard users to bypass repetitive navigation. Using `tabindex="-1"` on the target `<main>` element ensures it can receive programmatic focus even if it's not normally focusable, which is crucial for accessibility.
**Action:** Always wrap primary content in a `<main>` tag with a unique ID and `tabindex="-1"` when implementing skip links.
