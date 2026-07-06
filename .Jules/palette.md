## 2026-07-06 - Preventing Ghost Focus in Mobile Menus
**Learning:** Off-screen navigation menus that use only `transform` or `position` to hide remain in the tab order, causing "ghost focus" where keyboard users can navigate to invisible links. Using `visibility: hidden` removes them from the accessibility tree and tab order while still allowing for smooth CSS transitions.
**Action:** Always pair positioning-based hiding with `visibility: hidden` for off-screen menus and ensure `aria-expanded` correctly communicates state to screen readers.
