## 2025-04-01 - [Image Lazy Loading Optimization]
**Learning:** For portfolio websites with many large images, the `loading="lazy"` attribute on `<img>` tags is a high-impact, low-effort optimization. It prevents the browser from loading images that are not yet in the viewport, significantly reducing initial page load weight and memory usage. This is especially critical for modals that inject dozens of images into the DOM at once.
**Action:** Always check if image-heavy components (like galleries and modals) are using native lazy loading to prioritize critical assets.
