"""
Login page object for SauceDemo application.
"""
from typing import Optional
from playwright.async_api import Page
from .base_page import BasePage


class LoginPage(BasePage):
    """Login page object containing login functionality."""
    
    def __init__(self, page: Page) -> None:
        """
        Initialize the login page.
        
        Args:
            page: Playwright page object
        """
        super().__init__(page)
        
        # Locators
        self.username_input = "[data-test='username']"
        self.password_input = "[data-test='password']"
        self.login_button = "[data-test='login-button']"
        self.error_message = "[data-test='error']"
        self.error_button = ".error-button"
        
        # Login URL
        self.login_url = f"{self.base_url}/"
    
    async def navigate_to_login(self) -> None:
        """Navigate to the login page."""
        await self.navigate_to(self.login_url)
    
    async def enter_username(self, username: str) -> None:
        """
        Enter username in the username field.
        
        Args:
            username: Username to enter
        """
        await self.fill_input(self.username_input, username)
    
    async def enter_password(self, password: str) -> None:
        """
        Enter password in the password field.
        
        Args:
            password: Password to enter
        """
        await self.fill_input(self.password_input, password)
    
    async def click_login(self) -> None:
        """Click the login button."""
        await self.click_element(self.login_button)
    
    async def login(self, username: str, password: str) -> None:
        """
        Perform complete login action.
        
        Args:
            username: Username for login
            password: Password for login
        """
        await self.enter_username(username)
        await self.enter_password(password)
        await self.click_login()
    
    async def get_error_message(self) -> str:
        """
        Get the error message text.
        
        Returns:
            Error message text or empty string if no error
        """
        if await self.is_element_visible(self.error_message):
            return await self.get_text(self.error_message)
        return ""
    
    async def is_error_displayed(self) -> bool:
        """
        Check if login error is displayed.
        
        Returns:
            True if error is displayed, False otherwise
        """
        return await self.is_element_visible(self.error_message)
    
    async def dismiss_error(self) -> None:
        """Dismiss the error message by clicking the error button."""
        if await self.is_element_visible(self.error_button):
            await self.click_element(self.error_button)
    
    async def is_login_page_loaded(self) -> bool:
        """
        Check if login page is properly loaded.
        
        Returns:
            True if login page is loaded, False otherwise
        """
        return (
            await self.is_element_visible(self.username_input) and
            await self.is_element_visible(self.password_input) and
            await self.is_element_visible(self.login_button)
        )
    
    async def get_login_button_text(self) -> str:
        """
        Get the login button text.
        
        Returns:
            Login button text
        """
        return await self.get_text(self.login_button)