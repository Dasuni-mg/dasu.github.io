## 2025-05-15 - Improving Navigation with Skip Links
**Learning:** For single-page portfolios with sticky navigation, keyboard users often have to tab through numerous links every time they want to reach the main content. Implementing a "Skip to Content" link that targets a `<main>` element with `tabindex="-1"` significantly improves the keyboard navigation experience.
**Action:** Always include a Skip Link and ensure the target element is focusable but not in the regular tab order by using `tabindex="-1"`.
