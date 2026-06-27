## 2024-06-27 - [Accessibility & Semantic Navigation]
**Learning:** Static portfolio templates often focus on visual "active" states (like CSS classes) for navigation but neglect semantic accessibility. Screen readers need `aria-current="page"` to understand the current context in a single-page layout. Additionally, "Skip to Content" links are essential for keyboard navigability in sites with sticky navbars to avoid repetitive tabbing through the header.

**Action:** When implementing or refactoring navigation/scroll-spy logic, ensure that the semantic `aria-current` attribute is synchronized with the visual active class. Always provide a hidden-until-focused skip link targeting a `<main>` element with `tabindex="-1"`.
