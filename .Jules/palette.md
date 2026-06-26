## 2025-05-15 - [Mobile Navigation Accessibility]
**Learning:** Off-screen navigation menus (e.g., using `right: -100%`) remain in the keyboard tab order if they are still `display: flex/block`. This creates a confusing experience for screen reader and keyboard users who encounter "invisible" links.
**Action:** Use `visibility: hidden` in conjunction with off-screen positioning. `visibility` is animatable and correctly removes elements from the accessibility tree and tab order while allowing for smooth CSS transitions.
