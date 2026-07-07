## 2026-07-07 - Preventing Ghost Focus in Mobile Menus
**Learning:** Off-screen navigation menus that use only `transform: translateX()` or `right: -100%` can still receive keyboard focus even when they are not visible. This "ghost focus" creates a confusing experience for keyboard users who might find their focus indicator disappearing into an invisible menu. Using `visibility: hidden` in combination with positioning ensures that the menu and its contents are truly removed from the tab order when closed.

**Action:** Always combine off-screen positioning with `visibility: hidden` for mobile menus, and toggle to `visibility: visible` when the menu is active.

## 2026-07-07 - Screen Reader Context for Mobile Toggles
**Learning:** Icon-only buttons like hamburger menus need explicit ARIA state management to be useful for screen reader users. Without `aria-expanded` and `aria-controls`, a user might hear "button" without knowing what it does or whether the associated content is currently visible.

**Action:** Implement `aria-expanded` and `aria-controls` on mobile navigation toggles and programmatically update the `aria-expanded` state on click.
