## 2025-03-24 - [Mobile Menu Accessibility]
**Learning:** Even if a menu toggle button uses ARIA attributes like `aria-controls`, those attributes are useless if the target element doesn't have a matching `id`. Always verify that `aria-controls` points to an actual ID.
**Action:** Always add an `id` to the element being controlled when implementing ARIA-enabled toggles.

## 2025-03-24 - [Skip to Content Implementation]
**Learning:** Standard utility classes like `sr-only` are often available in projects using Bootstrap, but it's important to verify their presence in the CSS distribution to avoid visual regressions.
**Action:** Proactively check CSS files for expected accessibility utility classes before relying on them.
