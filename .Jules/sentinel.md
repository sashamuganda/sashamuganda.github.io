## 2026-03-27 - [DOM Injection and Tabnabbing Vulnerabilities]
**Vulnerability:** The use of `innerHTML` to inject content into the portfolio modal and the use of `target="_blank"` without `rel="noopener"`.
**Learning:** Even with static data, `innerHTML` is a risky pattern that can lead to XSS if data sources ever become dynamic. Using `target="_blank"` without `rel="noopener"` allows the opened page to access the original page via `window.opener`.
**Prevention:** Use `textContent` and `createElement` for DOM manipulation. Always add `rel="noopener noreferrer"` to external links.
