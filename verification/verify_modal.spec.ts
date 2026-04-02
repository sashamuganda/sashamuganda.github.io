import { test, expect } from '@playwright/test';

test('modal opens without console errors', async ({ page }) => {
  const errors: Error[] = [];
  page.on('pageerror', (error) => errors.push(error));

  await page.goto('http://localhost:8000/index.html');

  // Click on the first panel
  await page.click('[data-panel-id="brand"]');

  // Check if modal is visible
  const modal = page.locator('#portfolioModal');
  await expect(modal).toHaveClass(/show/);

  // Check if title is correct
  const title = page.locator('#modal-title');
  await expect(title).toHaveText('Brand Identity');

  // Check for console errors
  expect(errors).toHaveLength(0);
});
