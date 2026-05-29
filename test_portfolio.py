import pytest
from playwright.sync_api import Page, expect

def test_skip_link_exists(page: Page):
    page.goto("http://localhost:8000")
    skip_link = page.locator(".skip-link")
    expect(skip_link).to_have_text("Skip to Content")
    expect(skip_link).to_have_attribute("href", "#home")

    # Check if it's off-screen initially
    top_value = skip_link.evaluate("el => getComputedStyle(el).top")
    assert top_value == "-100px"

def test_skip_link_visible_on_focus(page: Page):
    page.goto("http://localhost:8000")
    page.keyboard.press("Tab")
    skip_link = page.locator(".skip-link")

    # Wait for the transition to complete
    page.wait_for_timeout(500)

    # Check if it's visible (top should be 0)
    top_value = skip_link.evaluate("el => getComputedStyle(el).top")
    assert top_value == "0px"

def test_skip_link_navigation(page: Page):
    page.goto("http://localhost:8000")
    page.keyboard.press("Tab")
    page.keyboard.press("Enter")

    # Check if focus shifted to #home
    hero_section = page.locator("#home")
    expect(hero_section).to_be_focused()
