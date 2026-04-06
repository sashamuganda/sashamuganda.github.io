## 2025-04-01 - [Image Lazy Loading Optimization]
**Learning:** For portfolio websites with many large images, the `loading="lazy"` attribute on `<img>` tags is a high-impact, low-effort optimization. It prevents the browser from loading images that are not yet in the viewport, significantly reducing initial page load weight and memory usage. This is especially critical for modals that inject dozens of images into the DOM at once.
**Action:** Always check if image-heavy components (like galleries and modals) are using native lazy loading to prioritize critical assets.

## 2026-04-04 - [Critical Path & Modal Rendering Optimization]
**Learning:** Applying `loading="lazy"` to above-the-fold content is a performance anti-pattern that delays Largest Contentful Paint (LCP). Critical assets should instead use `fetchpriority="high"` and `decoding="async"`. Furthermore, when dynamically populating large galleries in modals, using `DocumentFragment` to batch DOM construction significantly reduces layout thrashing compared to multiple `appendChild` calls or `innerHTML` overwrites.
**Action:** Audit "above-the-fold" assets for incorrect lazy loading and prefer `DocumentFragment` for non-trivial DOM injections.

## 2026-04-05 - [JS Preloading vs Native Lazy Loading]
**Learning:** Using `new Image()` in JavaScript to "manually" handle lazy loading (e.g., loading a high-res version over a placeholder) can inadvertently bypass the browser's native `loading="lazy"` optimization. Since the JS execution happens immediately upon element creation, the browser initiates the fetch regardless of viewport proximity.
**Action:** Prefer native `loading="lazy"` by setting `img.src` directly and using CSS `background-image` for low-res placeholders to maintain "blur-up" effects without triggering premature downloads.

## 2026-05-15 - [SPA Initialization & Home Flash Anti-pattern]
**Learning:** Hardcoding the `active` class on a primary view in a hash-based SPA, combined with `window.addEventListener('load', ...)` for routing, creates a "Home Flash" where the default content is displayed briefly before the router can redirect to the correct hash. This increases perceived latency and creates a jarring UX.
**Action:** Remove default `active` classes from SPA views and trigger routing logic on `DOMContentLoaded` or immediate execution to ensure the correct view is rendered from the first frame.
