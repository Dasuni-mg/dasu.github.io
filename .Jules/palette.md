## 2025-03-24 - Accessibility and Contrast Polish

**Learning:** Static portfolio templates often overlook basic accessibility features like "Skip to Content" links and proper ARIA states for mobile navigation. Additionally, default text colors in "modern" themes frequently fail WCAG AA contrast ratios (4.5:1) for secondary text.

**Action:** Always audit the mobile navigation toggle for `aria-expanded` and `aria-controls`. Implement a "Skip to Content" link as a standard practice for one-page portfolios. Verify color contrast of secondary text against the background using standard accessible color palettes (e.g., Tailwind's 600/700 series for light backgrounds).
