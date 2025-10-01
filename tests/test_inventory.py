"""
Inventory page functionality tests for SauceDemo application.
"""
import pytest
from pages import InventoryPage


class TestInventory:
    """Test class for inventory page functionality."""
    
    @pytest.mark.smoke
    @pytest.mark.inventory
    async def test_inventory_page_loads(self, authenticated_page, inventory_page: InventoryPage):
        """Test that inventory page loads correctly after authentication."""
        # Verify inventory page is loaded
        assert await inventory_page.is_inventory_page_loaded(), "Inventory page should be loaded"
        
        # Verify products are displayed
        product_count = await inventory_page.get_product_count()
        assert product_count > 0, "Products should be displayed on the page"
    
    @pytest.mark.inventory
    async def test_product_display(self, authenticated_page, inventory_page: InventoryPage):
        """Test that products are displayed with required information."""
        # Get product information
        product_names = await inventory_page.get_product_names()
        product_prices = await inventory_page.get_product_prices()
        
        # Verify products have names and prices
        assert len(product_names) > 0, "Product names should be displayed"
        assert len(product_prices) > 0, "Product prices should be displayed"
        assert len(product_names) == len(product_prices), "Each product should have a name and price"
        
        # Verify price format (should contain $)
        for price in product_prices:
            assert "$" in price, f"Price should contain $ symbol, got: {price}"
    
    @pytest.mark.inventory
    async def test_add_product_to_cart(self, authenticated_page, inventory_page: InventoryPage):
        """Test adding a product to the shopping cart."""
        # Get initial cart count
        initial_cart_count = await inventory_page.get_cart_badge_count()
        
        # Add first product to cart
        product_names = await inventory_page.get_product_names()
        first_product = product_names[0]
        await inventory_page.add_product_to_cart_by_name(first_product)
        
        # Verify cart count increased
        updated_cart_count = await inventory_page.get_cart_badge_count()
        assert updated_cart_count == initial_cart_count + 1, "Cart count should increase by 1"
    
    @pytest.mark.inventory
    async def test_remove_product_from_cart(self, authenticated_page, inventory_page: InventoryPage):
        """Test removing a product from the shopping cart."""
        # Add a product first
        product_names = await inventory_page.get_product_names()
        first_product = product_names[0]
        await inventory_page.add_product_to_cart_by_name(first_product)
        
        # Get cart count after adding
        cart_count_after_add = await inventory_page.get_cart_badge_count()
        
        # Remove the product
        await inventory_page.remove_product_from_cart_by_name(first_product)
        
        # Verify cart count decreased
        cart_count_after_remove = await inventory_page.get_cart_badge_count()
        assert cart_count_after_remove == cart_count_after_add - 1, "Cart count should decrease by 1"
    
    @pytest.mark.inventory
    async def test_add_multiple_products_to_cart(self, authenticated_page, inventory_page: InventoryPage):
        """Test adding multiple products to cart."""
        # Get initial cart count
        initial_cart_count = await inventory_page.get_cart_badge_count()
        
        # Add multiple products
        product_names = await inventory_page.get_product_names()
        products_to_add = product_names[:3]  # Add first 3 products
        
        for product in products_to_add:
            await inventory_page.add_product_to_cart_by_name(product)
        
        # Verify cart count
        final_cart_count = await inventory_page.get_cart_badge_count()
        expected_count = initial_cart_count + len(products_to_add)
        assert final_cart_count == expected_count, f"Cart should contain {expected_count} items"
    
    @pytest.mark.inventory
    async def test_product_sorting_name_az(self, authenticated_page, inventory_page: InventoryPage):
        """Test sorting products by name A-Z."""
        # Sort products by name A-Z
        await inventory_page.sort_products("az")
        
        # Get product names after sorting
        product_names = await inventory_page.get_product_names()
        
        # Verify products are sorted A-Z
        sorted_names = sorted(product_names)
        assert product_names == sorted_names, "Products should be sorted A-Z"
    
    @pytest.mark.inventory
    async def test_product_sorting_name_za(self, authenticated_page, inventory_page: InventoryPage):
        """Test sorting products by name Z-A."""
        # Sort products by name Z-A
        await inventory_page.sort_products("za")
        
        # Get product names after sorting
        product_names = await inventory_page.get_product_names()
        
        # Verify products are sorted Z-A
        sorted_names = sorted(product_names, reverse=True)
        assert product_names == sorted_names, "Products should be sorted Z-A"
    
    @pytest.mark.inventory
    async def test_product_sorting_price_low_high(self, authenticated_page, inventory_page: InventoryPage):
        """Test sorting products by price low to high."""
        # Sort products by price low to high
        await inventory_page.sort_products("lohi")
        
        # Get product prices after sorting
        product_prices = await inventory_page.get_product_prices()
        
        # Convert prices to float for comparison (remove $ and convert)
        price_values = []
        for price in product_prices:
            price_value = float(price.replace("$", ""))
            price_values.append(price_value)
        
        # Verify prices are sorted low to high
        sorted_prices = sorted(price_values)
        assert price_values == sorted_prices, "Products should be sorted by price low to high"
    
    @pytest.mark.inventory
    async def test_shopping_cart_navigation(self, authenticated_page, inventory_page: InventoryPage):
        """Test navigation to shopping cart page."""
        # Click shopping cart
        await inventory_page.click_shopping_cart()
        
        # Verify navigation to cart page
        current_url = inventory_page.page.url
        assert "cart" in current_url, f"Should navigate to cart page, current URL: {current_url}"
    
    @pytest.mark.inventory
    async def test_product_details_retrieval(self, authenticated_page, inventory_page: InventoryPage):
        """Test retrieving detailed product information."""
        # Get product names
        product_names = await inventory_page.get_product_names()
        first_product = product_names[0]
        
        # Get detailed product information
        product_details = await inventory_page.get_product_details_by_name(first_product)
        
        # Verify product details structure
        assert "name" in product_details, "Product details should include name"
        assert "price" in product_details, "Product details should include price"
        assert "description" in product_details, "Product details should include description"
        
        # Verify details are not empty
        assert product_details["name"], "Product name should not be empty"
        assert product_details["price"], "Product price should not be empty"
        assert product_details["description"], "Product description should not be empty"
    
    @pytest.mark.inventory
    async def test_logout_functionality(self, authenticated_page, inventory_page: InventoryPage, login_page):
        """Test logout functionality from inventory page."""
        # Perform logout
        await inventory_page.logout()
        
        # Verify redirect to login page
        await login_page.page.wait_for_timeout(1000)  # Wait for redirect
        assert await login_page.is_login_page_loaded(), "Should be redirected to login page after logout"
        
        # Verify URL is login page
        current_url = inventory_page.page.url
        assert "inventory" not in current_url, "Should not be on inventory page after logout"