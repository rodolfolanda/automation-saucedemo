"""
Pytest configuration and fixtures.
"""
import pytest
from typing import Generator, AsyncGenerator
from playwright.async_api import Page, BrowserContext
from pages import LoginPage, InventoryPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Create a LoginPage instance."""
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    """Create an InventoryPage instance."""
    return InventoryPage(page)


@pytest.fixture
async def authenticated_page(login_page: LoginPage) -> Page:
    """
    Create an authenticated page session.
    Logs in with standard user and returns the page object.
    """
    await login_page.navigate_to_login()
    await login_page.login("standard_user", "secret_sauce")
    return login_page.page


# Test data fixtures
@pytest.fixture
def valid_users() -> dict:
    """Valid user credentials for testing."""
    return {
        "standard_user": "secret_sauce",
        "performance_glitch_user": "secret_sauce",
        "problem_user": "secret_sauce"
    }


@pytest.fixture
def invalid_users() -> dict:
    """Invalid user credentials for testing."""
    return {
        "invalid_user": "wrong_password",
        "locked_out_user": "secret_sauce",
        "": "",
        "standard_user": ""
    }