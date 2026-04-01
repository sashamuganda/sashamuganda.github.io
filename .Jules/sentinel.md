# Sentinel Journal - Sasha Muganda Portfolio

## 2025-05-14 - Initial Security Audit
**Vulnerability:** Use of `target="_blank"` without `rel="noopener noreferrer"` in social links.
**Learning:** This can lead to tabnabbing where the opened page can control the original page via `window.opener`.
**Prevention:** Always include `rel="noopener noreferrer"` when using `target="_blank"`.

**Vulnerability:** Use of `innerHTML` for dynamic content.
**Learning:** Although the data is currently static, using `innerHTML` is a dangerous pattern that can lead to XSS if the data source becomes untrusted.
**Prevention:** Use `textContent`, `createElement`, and `appendChild` or other safe DOM APIs.
