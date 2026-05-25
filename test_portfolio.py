import pytest
import re
from playwright.sync_api import Page, expect

# To run these tests:
# 1. Start a local server: python3 -m http.server 8000
# 2. Run: pytest test_portfolio.py

BASE_URL = "http://localhost:8000"

def test_page_load(page: Page):
    response = page.goto(BASE_URL)
    assert response.status == 200
    expect(page).to_have_title("Dasuni Nuwanika- portfolio")

def test_navigation_links(page: Page):
    page.goto(BASE_URL)
    nav_links = ["education", "skills", "experience", "profiles", "portfolio", "contact"]
    for link in nav_links:
        selector = f"a[href='#{link}']"
        expect(page.locator(selector)).to_be_visible()

def test_images_load(page: Page):
    page.goto(BASE_URL)
    # Check all images have a non-empty src
    images = page.locator("img")
    count = images.count()
    for i in range(count):
        img = images.nth(i)
        # Use regex to ensure src is not empty
        expect(img).to_have_attribute("src", re.compile(r".+"))

def test_no_console_errors(page: Page):
    errors = []
    page.on("pageerror", lambda exc: errors.append(exc))
    page.goto(BASE_URL)
    assert len(errors) == 0, f"Console errors detected: {errors}"

def test_resume_download_link(page: Page):
    page.goto(BASE_URL)
    resume_link = page.get_by_role("link", name="download resume")
    expect(resume_link).to_be_visible()
    expect(resume_link).to_have_attribute("href", "assets/M.G Dasuni Nuwanika.pdf")
    expect(resume_link).to_have_attribute("download", "")
