"""
Pytest configuration and fixtures.
"""
import pytest
from playwright.sync_api import Page as SyncPage
from playwright.async_api import Page as AsyncPage
from pages import LoginPage, InventoryPage


@pytest.fixture
def login_page(page) -> LoginPage:
    """Create a LoginPage instance."""
    return LoginPage(page)


@pytest.fixture
def inventory_page(page) -> InventoryPage:
    """Create an InventoryPage instance."""
    return InventoryPage(page)


@pytest.fixture
async def authenticated_page(page):
    """
    Create an authenticated page session.
    Logs in with standard user and returns the page object.
    """
    login_page = LoginPage(page)
    await login_page.navigate_to_login()
    await login_page.login("standard_user", "secret_sauce")
    return page


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