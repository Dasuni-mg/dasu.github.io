# 🎨 Palette's UX Journal

## 2025-06-28 - [Skip Link Implementation]
**Learning:** In single-page portfolios with sticky navigations, a 'Skip to Content' link is essential for keyboard users to bypass repetitive navigation. However, the target element (usually `<main>`) must have `tabindex="-1"` to ensure it can programmatically receive focus across all browsers.
**Action:** Always include a 'Skip to Content' link and ensure the target has `tabindex="-1"` for consistent keyboard navigation.
