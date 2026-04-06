## 2025-05-15 - [Keyboard Accessibility for Portfolio Grid]
**Learning:** In static portfolio sites that use `div` elements as gallery triggers, visual-only cues (hover effects) often mask a complete lack of keyboard accessibility. Interactive `div` elements must be explicitly converted to buttons using `role="button"` and `tabindex="0"`, with `keydown` listeners for both `Enter` and `Space`.
**Action:** Always verify that interactive grid elements are focusable and use `:focus-visible` to provide high-contrast outlines that match the design system's accent colors.

## 2025-05-15 - [Accessible Image Attributes and Keyboard Discoverability]
**Learning:** For images inside interactive links that already contain descriptive text (e.g., a brand logo next to a title), using `alt=""` is more accessible than repeating the text. Redundant `alt` text causes screen readers to announce the label twice, leading to a cluttered user experience. Furthermore, specialized navigation features (like arrow keys for cycling categories) are effectively invisible to users unless paired with a visual hint.
**Action:** Use empty `alt` attributes for redundant decorative images and provide a small keyboard-hint (e.g., using `<kbd>`) within modals to improve feature discoverability.

## 2026-04-05 - [Comprehensive Modal Accessibility and Focus Management]
**Learning:** Dynamic gallery content and modal focus management are critical for an accessible SPA experience. Interactive elements generated via JavaScript (like gallery images) must be explicitly assigned `tabIndex="0"` and `role="button"` with `keydown` listeners. Furthermore, a robust focus trap is necessary to contain keyboard navigation within the modal, preventing "focus leaks" to the background.
**Action:** Always implement a focus trap for modals and ensure all dynamically created interactive elements are keyboard-accessible and visually highlighted via `:focus-visible`.

## 2026-04-06 - [Integrated Form Feedback and Focus Discovery]
**Learning:** Micro-UX improvements for static forms significantly reduce user anxiety. Providing immediate "Sending..." feedback on submission prevents duplicate actions, while restoring the button on error ensures the app remains usable. Additionally, when using "hover-to-reveal" patterns for CTAs (like "Explore" buttons), using `:focus-visible` or `:focus-within` on the parent ensures keyboard users can discover and interact with the same elements as mouse users.
**Action:** Ensure CTAs are revealed for keyboard users and implement robust state handling for async form submissions to provide clear progress and error recovery.
