import sys
import os
import pytest
from playwright.sync_api import sync_playwright

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="function")
def login(page):
    login_page = LoginPage(page)

    login_page.open_login_page()
    login_page.login("john.doe7@example.com", "StrongPass123!")

    return page