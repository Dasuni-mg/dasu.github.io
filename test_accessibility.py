import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="module", autouse=True)
def setup_server():
    import subprocess
    import time
    process = subprocess.Popen(["python3", "-m", "http.server", "8000"])
    time.sleep(2)  # Wait for server to start
    yield
    process.terminate()

def test_skip_link(page: Page):
    page.goto("http://localhost:8000")

    # Check if skip link exists
    skip_link = page.locator(".skip-link")
    expect(skip_link).to_have_text("Skip to main content")

    # Verify it's not visible initially (it's off-screen)
    # We check the top position. We use to_have_css which waits if needed,
    # but here we want to ensure it's NOT 0px initially.
    top = skip_link.evaluate("el => getComputedStyle(el).top")
    assert top == "-100px"

    # Focus the skip link
    page.keyboard.press("Tab")

    # Wait for the transition to finish
    expect(skip_link).to_have_css("top", "0px")

def test_mobile_menu_aria(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("http://localhost:8000")

    hamburger = page.locator("#hamburger")
    expect(hamburger).to_have_attribute("aria-expanded", "false")
    expect(hamburger).to_have_attribute("aria-controls", "navLinks")

    # Open menu
    hamburger.click()
    expect(hamburger).to_have_attribute("aria-expanded", "true")

    # Verify first link is focused (async after timeout in JS)
    # The JS has a 400ms timeout
    page.wait_for_timeout(600)
    focused_text = page.evaluate("document.activeElement.innerText")
    assert focused_text == "Home"

    # Close with Escape
    page.keyboard.press("Escape")
    expect(hamburger).to_have_attribute("aria-expanded", "false")

    # Verify hamburger is focused after Escape
    is_hamburger_focused = hamburger.evaluate("el => document.activeElement === el")
    assert is_hamburger_focused
