## 2026-03-27 - [Fixing Tabnabbing Vulnerability]
**Vulnerability:** External links using `target="_blank"` were missing `rel="noopener noreferrer"`.
**Learning:** This is a classic security risk where a newly opened page in a different domain can control the original window via `window.opener`.
**Prevention:** Always include `rel="noopener noreferrer"` when using `target="_blank"` for external links to ensure cross-origin isolation.
