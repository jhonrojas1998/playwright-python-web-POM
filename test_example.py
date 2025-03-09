import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function")
def navigate_to_playwright(page: Page):
    """Fixture para navegar a la página antes de cada test."""
    page.goto("https://playwright.dev/")
    return page

def test_has_title(navigate_to_playwright: Page):
    expect(navigate_to_playwright).to_have_title(re.compile("Playwright"))

def test_get_started_link(navigate_to_playwright: Page):
    page = navigate_to_playwright
    with page.expect_navigation():
        page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
