import pytest
from playwright.sync_api import BrowserContext

@pytest.fixture(scope="function")
def context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},  # Pantalla completa
        storage_state=None  # Evita almacenar cookies/sesión (modo incógnito)
    )
    return context
