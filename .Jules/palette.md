# Palette's UX Journal

## 2025-05-14 - Initial Audit
**Learning:** The portfolio lacks basic accessibility landmarks and skip-navigation, which is a common pattern in static templates.
**Action:** Implement a "Skip to Content" link and use semantic `<main>` landmark to improve keyboard navigation efficiency.

## 2025-05-14 - Scope Management & Micro-UX
**Learning:** In a "micro-UX" context, even helpful additions like form requirement indicators can push a change over strictly enforced line limits and dilute the focus of a primary accessibility fix.
**Action:** Prioritize the highest-impact accessibility fix (Landmarks/Skip-links) when strict line constraints are in place, and keep PRs atomic.
