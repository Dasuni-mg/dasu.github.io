import asyncio
from playwright.async_api import async_playwright
import os

async def test_portfolio():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        errors = []
        page.on("pageerror", lambda exc: errors.append(f"Page Error: {exc}"))
        page.on("console", lambda msg: errors.append(f"Console {msg.type}: {msg.text}") if msg.type == "error" else None)

        await page.goto("http://localhost:3000", wait_until="networkidle")

        print(f"Title: {await page.title()}")

        # Check navigation
        nav_links = ["education", "skills", "experience", "profiles", "portfolio", "contact"]
        for link in nav_links:
            try:
                await page.click(f"text={link}", timeout=5000)
                await page.wait_for_timeout(500)
                is_visible = await page.is_visible(f"#{link}")
                print(f"Link '{link}' works: {is_visible}")
            except Exception as e:
                print(f"Link '{link}' failed: {e}")

        # Check Day/Night toggle
        toggle = page.locator(".day-night input")
        if await toggle.count() > 0:
            print("Day/Night toggle found.")
            initial_checked = await toggle.is_checked()
            print(f"Initial toggle checked: {initial_checked}")

            # Try to click it (using dispatch_event to avoid interception)
            await toggle.dispatch_event("click")
            await page.wait_for_timeout(500)

            body_class = await page.evaluate("document.body.className")
            print(f"Body class after toggle: '{body_class}'")

            # Check if it actually changed colors (vars)
            bg_color = await page.evaluate("getComputedStyle(document.body).getPropertyValue('--background-color')")
            print(f"Background color var: {bg_color}")
        else:
            print("Day/Night toggle NOT found.")

        # Check for broken images
        images = await page.evaluate("""
            () => {
                const imgs = Array.from(document.querySelectorAll('img'));
                return imgs.map(img => ({
                    src: img.src,
                    complete: img.complete,
                    naturalWidth: img.naturalWidth,
                    visible: img.offsetWidth > 0 && img.offsetHeight > 0
                })).filter(img => !img.complete || img.naturalWidth === 0);
            }
        """)
        if images:
            print(f"Broken images found: {len(images)}")
            for img in images:
                print(f"  - {img['src']}")
        else:
            print("No broken images found.")

        # Check for 404s in network
        # (Already handled by console errors mostly, but can be explicit)

        if errors:
            print("Errors found:")
            for err in errors:
                print(f"  - {err}")
        else:
            print("No significant errors found.")

        await page.screenshot(path="test_result.png", full_page=True)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_portfolio())
