"""
Base page class containing common functionality for all page objects.
"""
from typing import Optional
from playwright.async_api import Page, Locator


class BasePage:
    """Base page class with common methods and properties."""
    
    def __init__(self, page: Page) -> None:
        """
        Initialize the base page.
        
        Args:
            page: Playwright page object
        """
        self.page = page
        self.base_url = "https://www.saucedemo.com"
    
    async def navigate_to(self, url: str) -> None:
        """
        Navigate to a specific URL.
        
        Args:
            url: The URL to navigate to
        """
        await self.page.goto(url)
    
    async def get_title(self) -> str:
        """
        Get the page title.
        
        Returns:
            The page title
        """
        return await self.page.title()
    
    async def wait_for_element(self, locator: str, timeout: int = 5000) -> Locator:
        """
        Wait for an element to be visible.
        
        Args:
            locator: Element selector
            timeout: Timeout in milliseconds
            
        Returns:
            Playwright Locator object
        """
        element = self.page.locator(locator)
        await element.wait_for(state="visible", timeout=timeout)
        return element
    
    async def click_element(self, locator: str) -> None:
        """
        Click on an element.
        
        Args:
            locator: Element selector
        """
        await self.page.locator(locator).click()
    
    async def fill_input(self, locator: str, text: str) -> None:
        """
        Fill an input field with text.
        
        Args:
            locator: Element selector
            text: Text to fill
        """
        await self.page.locator(locator).fill(text)
    
    async def get_text(self, locator: str) -> str:
        """
        Get text content of an element.
        
        Args:
            locator: Element selector
            
        Returns:
            Text content
        """
        return await self.page.locator(locator).text_content() or ""
    
    async def is_element_visible(self, locator: str) -> bool:
        """
        Check if an element is visible.
        
        Args:
            locator: Element selector
            
        Returns:
            True if element is visible, False otherwise
        """
        try:
            await self.page.locator(locator).wait_for(state="visible", timeout=3000)
            return True
        except Exception:
            return False
    
    async def take_screenshot(self, name: str) -> str:
        """
        Take a screenshot of the current page.
        
        Args:
            name: Name for the screenshot file
            
        Returns:
            Path to the screenshot file
        """
        screenshot_path = f"test-results/screenshots/{name}.png"
        await self.page.screenshot(path=screenshot_path)
        return screenshot_path