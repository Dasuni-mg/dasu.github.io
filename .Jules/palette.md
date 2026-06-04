## 2026-06-04 - Accessible Mobile Navigation
**Learning:** Mobile navigation menus (hamburger menus) often lack proper ARIA attributes in static portfolios, leaving screen reader users unaware of the menu's state (expanded vs. collapsed).
**Action:** Always include `aria-expanded` and `aria-controls` on the toggle button and synchronize the `aria-expanded` state via JavaScript whenever the menu is toggled.
