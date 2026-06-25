## 2025-05-15 - Accessibility Improvements for Static Portfolio

**Learning:** When implementing accessibility features like "Skip to Content" links in a project that restricts adding new CSS files or major dependencies, it's more efficient and cleaner to include the necessary utility classes (`sr-only`, `sr-only-focusable`) directly in the main stylesheet. This ensures consistency with the existing design tokens (e.g., colors, borders, shadows) and avoids issues with missing or external dependencies.

**Action:** For future micro-UX tasks, first check if existing stylesheets can be extended with standard accessibility patterns instead of linking external libraries like Bootstrap just for a few utility classes. Always verify that ARIA relationships (like `aria-controls` to `id`) are correctly mapped and functional.
