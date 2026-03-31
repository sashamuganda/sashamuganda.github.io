## 2025-05-15 - [Keyboard Accessibility for Portfolio Grid]
**Learning:** In static portfolio sites that use `div` elements as gallery triggers, visual-only cues (hover effects) often mask a complete lack of keyboard accessibility. Interactive `div` elements must be explicitly converted to buttons using `role="button"` and `tabindex="0"`, with `keydown` listeners for both `Enter` and `Space`.
**Action:** Always verify that interactive grid elements are focusable and use `:focus-visible` to provide high-contrast outlines that match the design system's accent colors.
