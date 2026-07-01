## 2025-05-15 - [Accessibility & Mobile Navigation]
**Learning:** For portfolios with sticky headers, anchor link navigation often causes content to be obscured by the navbar. Using `scroll-padding-top` on the `html` element is the most robust way to solve this without brittle JavaScript offsets. Additionally, mobile menus must manage `aria-expanded` and respond to the "Escape" key to meet basic accessibility standards.
**Action:** Proactively check for header occlusion on anchor links and implement `scroll-padding-top` alongside ARIA state management for toggles.

## 2025-05-15 - [Artifact Management in Static Repos]
**Learning:** Repositories without a `.gitignore` (like this static portfolio) are prone to including environment artifacts like `server.log` or verification scripts in PRs, which can lead to review blockers.
**Action:** Manually audit the file list and delete all non-essential artifacts before requesting a final code review or submitting.
