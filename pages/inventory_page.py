"""
Inventory page object for SauceDemo application.
"""
from typing import List, Optional
from playwright.async_api import Page
from .base_page import BasePage


class InventoryPage(BasePage):
    """Inventory page object containing product browsing functionality."""
    
    def __init__(self, page: Page) -> None:
        """
        Initialize the inventory page.
        
        Args:
            page: Playwright page object
        """
        super().__init__(page)
        
        # Locators
        self.inventory_container = ".inventory_container"
        self.inventory_list = ".inventory_list"
        self.inventory_items = ".inventory_item"
        self.item_names = ".inventory_item_name"
        self.item_descriptions = ".inventory_item_desc"
        self.item_prices = ".inventory_item_price"
        self.add_to_cart_buttons = "button[id^='add-to-cart']"
        self.remove_buttons = "button[id^='remove']"
        self.shopping_cart_link = ".shopping_cart_link"
        self.shopping_cart_badge = ".shopping_cart_badge"
        self.product_sort_dropdown = ".product_sort_container"
        self.menu_button = "#react-burger-menu-btn"
        self.logout_link = "#logout_sidebar_link"
        
        # Inventory URL
        self.inventory_url = f"{self.base_url}/inventory.html"
    
    async def is_inventory_page_loaded(self) -> bool:
        """
        Check if inventory page is properly loaded.
        
        Returns:
            True if inventory page is loaded, False otherwise
        """
        return (
            await self.is_element_visible(self.inventory_container) and
            await self.is_element_visible(self.inventory_list)
        )
    
    async def get_product_names(self) -> List[str]:
        """
        Get all product names on the page.
        
        Returns:
            List of product names
        """
        names = await self.page.locator(self.item_names).all_text_contents()
        return names
    
    async def get_product_prices(self) -> List[str]:
        """
        Get all product prices on the page.
        
        Returns:
            List of product prices
        """
        prices = await self.page.locator(self.item_prices).all_text_contents()
        return prices
    
    async def get_product_count(self) -> int:
        """
        Get the number of products displayed.
        
        Returns:
            Number of products
        """
        return await self.page.locator(self.inventory_items).count()
    
    async def add_product_to_cart_by_name(self, product_name: str) -> None:
        """
        Add a product to cart by its name.
        
        Args:
            product_name: Name of the product to add
        """
        # Find the product item containing the name
        product_locator = self.page.locator(self.inventory_items).filter(
            has_text=product_name
        )
        
        # Click the add to cart button within that product
        add_button = product_locator.locator("button[id^='add-to-cart']")
        await add_button.click()
    
    async def remove_product_from_cart_by_name(self, product_name: str) -> None:
        """
        Remove a product from cart by its name.
        
        Args:
            product_name: Name of the product to remove
        """
        # Find the product item containing the name
        product_locator = self.page.locator(self.inventory_items).filter(
            has_text=product_name
        )
        
        # Click the remove button within that product
        remove_button = product_locator.locator("button[id^='remove']")
        await remove_button.click()
    
    async def get_cart_badge_count(self) -> int:
        """
        Get the shopping cart badge count.
        
        Returns:
            Cart badge count, 0 if no badge is visible
        """
        if await self.is_element_visible(self.shopping_cart_badge):
            badge_text = await self.get_text(self.shopping_cart_badge)
            return int(badge_text) if badge_text.isdigit() else 0
        return 0
    
    async def click_shopping_cart(self) -> None:
        """Click the shopping cart link."""
        await self.click_element(self.shopping_cart_link)
    
    async def sort_products(self, sort_option: str) -> None:
        """
        Sort products using the dropdown.
        
        Args:
            sort_option: Sort option value (za, az, lohi, hilo)
        """
        await self.page.locator(self.product_sort_dropdown).select_option(sort_option)
    
    async def open_menu(self) -> None:
        """Open the hamburger menu."""
        await self.click_element(self.menu_button)
    
    async def logout(self) -> None:
        """Logout from the application."""
        await self.open_menu()
        await self.wait_for_element(self.logout_link)
        await self.click_element(self.logout_link)
    
    async def get_product_details_by_name(self, product_name: str) -> dict:
        """
        Get product details (name, price, description) by product name.
        
        Args:
            product_name: Name of the product
            
        Returns:
            Dictionary with product details
        """
        product_locator = self.page.locator(self.inventory_items).filter(
            has_text=product_name
        )
        
        name = await product_locator.locator(self.item_names).text_content()
        price = await product_locator.locator(self.item_prices).text_content()
        description = await product_locator.locator(self.item_descriptions).text_content()
        
        return {
            "name": name or "",
            "price": price or "",
            "description": description or ""
        }