## 2025-05-14 - Mobile Menu Ghost Focus
**Learning:** Off-screen navigation menus that only use `position: fixed` and `right: -100%` remain in the tab order, allowing keyboard users to "ghost focus" invisible links. This creates a confusing experience for screen reader and keyboard-only users.
**Action:** Use `visibility: hidden` and `visibility: visible` alongside positioning. Transitioning `visibility` allows for smooth animations while correctly removing the element from the accessibility tree and tab order when hidden.
