# Testing Instructions

This project includes an automated test suite using [Playwright](https://playwright.dev/python/) and [pytest](https://docs.pytest.org/).

## Prerequisites

- Python 3.7+
- A local web server (e.g., Python's built-in `http.server`)

## Setup

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Install the Playwright browsers:
   ```bash
   playwright install chromium
   ```

## Running Tests

1. Start the local development server in the root directory:
   ```bash
   python3 -m http.server 8000
   ```

2. In a separate terminal, run the tests using `pytest`:
   ```bash
   pytest test_portfolio.py
   ```

## What is tested?

- **Page Load:** Ensures the site returns a 200 OK status and has the correct title.
- **Navigation Links:** Verifies that all main sections (Education, Skills, etc.) have visible navigation links.
- **Image Integrity:** Checks that all `<img>` tags have valid `src` attributes.
- **Console Errors:** Monitors the browser console for any JavaScript errors during page load.
- **Resume Download:** Confirms the "download resume" link is present and correctly configured.
