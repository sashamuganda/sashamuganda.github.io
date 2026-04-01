# Sentinel Journal - Sasha Muganda Portfolio

## 2025-05-14 - Initial Security Audit
**Vulnerability:** Use of `target="_blank"` without `rel="noopener noreferrer"` in social links.
**Learning:** This can lead to tabnabbing where the opened page can control the original page via `window.opener`.
**Prevention:** Always include `rel="noopener noreferrer"` when using `target="_blank"`.

**Vulnerability:** Use of `innerHTML` for dynamic content.
**Learning:** Although the data is currently static, using `innerHTML` is a dangerous pattern that can lead to XSS if the data source becomes untrusted.
**Prevention:** Use `textContent`, `createElement`, and `appendChild` or other safe DOM APIs.
## 2026-03-27 - [Fixing Tabnabbing Vulnerability]
**Vulnerability:** External links using `target="_blank"` were missing `rel="noopener noreferrer"`.
**Learning:** This is a classic security risk where a newly opened page in a different domain can control the original window via `window.opener`.
**Prevention:** Always include `rel="noopener noreferrer"` when using `target="_blank"` for external links to ensure cross-origin isolation.
