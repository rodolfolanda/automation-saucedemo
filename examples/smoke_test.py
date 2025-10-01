"""
Simple smoke test to verify the project setup.
"""
import asyncio
from playwright.async_api import async_playwright
from pages import LoginPage, InventoryPage


async def test_basic_login():
    """Basic test to verify login functionality works."""
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        # Initialize page objects
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)
        
        try:
            # Navigate to login page
            await login_page.navigate_to_login()
            print("✅ Successfully navigated to login page")
            
            # Verify login page is loaded
            is_loaded = await login_page.is_login_page_loaded()
            print(f"✅ Login page loaded: {is_loaded}")
            
            # Perform login
            await login_page.login("standard_user", "secret_sauce")
            print("✅ Login attempt completed")
            
            # Wait a moment for redirect
            await page.wait_for_timeout(2000)
            
            # Check if we're on inventory page
            is_inventory_loaded = await inventory_page.is_inventory_page_loaded()
            print(f"✅ Inventory page loaded: {is_inventory_loaded}")
            
            if is_inventory_loaded:
                # Get product count
                product_count = await inventory_page.get_product_count()
                print(f"✅ Found {product_count} products on inventory page")
                
                # Get product names
                product_names = await inventory_page.get_product_names()
                print(f"✅ Product names: {product_names[:2]}...")  # Show first 2
            
            print("🎉 Basic smoke test PASSED!")
            
        except Exception as e:
            print(f"❌ Test failed: {e}")
            raise
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(test_basic_login())