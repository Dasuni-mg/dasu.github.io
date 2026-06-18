## 2026-06-18 - Mobile Navigation Accessibility Patterns
**Learning:** Mobile "hamburger" menus in static portfolios often lack the necessary ARIA attributes to communicate their state to screen readers. Simply toggling a CSS class is insufficient for accessibility.
**Action:** Always include `aria-expanded`, `aria-controls`, and `type="button"` on mobile menu toggles, and ensure the `aria-expanded` attribute is programmatically updated when the menu state changes.
