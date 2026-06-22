## 2025-05-15 - [Accessibility] Skip to Content link implementation
**Learning:** Implementing a "Skip to Content" link significantly improves keyboard accessibility for sites with many navigation links. Using `tabindex="-1"` on the target `<main>` element is crucial for cross-browser programmatic focus.
**Action:** Proactively check for skip links in single-page applications and static portfolios. Ensure semantic `<main>` tags are present and appropriately targeted.
