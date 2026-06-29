## 2025-05-15 - [Accessible Mobile Navigation]
**Learning:** Off-screen navigation menus (e.g., using `right: -100%`) remain discoverable by keyboard and screen readers ("ghost focus") if they are only visually hidden. Using `visibility: hidden` in combination with positioning ensures they are removed from the accessibility tree and tab order when closed, while still allowing for smooth CSS transitions.
**Action:** Always pair off-screen positioning with `visibility: hidden` and ensure `aria-expanded` is updated programmatically as a string to communicate state to assistive technologies.
