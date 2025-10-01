"""
Working inventory tests for SauceDemo application using pytest-playwright.
"""
import pytest


class TestInventoryWorking:
    """Test class for inventory page functionality that works with pytest-playwright."""
    
    def authenticated_session(self, page):
        """Helper to log in and get to inventory page."""
        page.goto("https://www.saucedemo.com/")
        page.locator("[data-test='username']").fill("standard_user")
        page.locator("[data-test='password']").fill("secret_sauce")
        page.locator("[data-test='login-button']").click()
        page.wait_for_url("**/inventory.html")
    
    def test_inventory_page_loads(self, page):
        """Test that inventory page loads correctly after authentication."""
        self.authenticated_session(page)
        
        # Verify inventory page is loaded
        assert page.locator(".inventory_container").is_visible(), "Inventory page should be loaded"
        
        # Verify products are displayed
        products = page.locator(".inventory_item")
        product_count = products.count()
        assert product_count > 0, "Products should be displayed on the page"
        print(f"✅ Found {product_count} products")
    
    def test_product_display(self, page):
        """Test that products are displayed with required information."""
        self.authenticated_session(page)
        
        # Get product information
        product_names = page.locator(".inventory_item_name").all_text_contents()
        product_prices = page.locator(".inventory_item_price").all_text_contents()
        
        # Verify products have names and prices
        assert len(product_names) > 0, "Product names should be displayed"
        assert len(product_prices) > 0, "Product prices should be displayed"
        assert len(product_names) == len(product_prices), "Each product should have a name and price"
        
        # Verify price format (should contain $)
        for price in product_prices:
            assert "$" in price, f"Price should contain $ symbol, got: {price}"
        
        print(f"✅ Found {len(product_names)} products with proper names and prices")
    
    def test_add_product_to_cart(self, page):
        """Test adding a product to the shopping cart."""
        self.authenticated_session(page)
        
        # Get initial cart count (should be 0 or empty)
        cart_badge = page.locator(".shopping_cart_badge")
        initial_count = 0
        if cart_badge.is_visible():
            initial_count = int(cart_badge.text_content())
        
        # Add first product to cart
        first_add_button = page.locator("button[id^='add-to-cart']").first
        first_add_button.click()
        
        # Verify cart count increased
        page.wait_for_selector(".shopping_cart_badge", timeout=5000)
        updated_count = int(page.locator(".shopping_cart_badge").text_content())
        assert updated_count == initial_count + 1, "Cart count should increase by 1"
        
        print(f"✅ Cart count increased from {initial_count} to {updated_count}")
    
    def test_remove_product_from_cart(self, page):
        """Test removing a product from the shopping cart."""
        self.authenticated_session(page)
        
        # Add a product first
        first_add_button = page.locator("button[id^='add-to-cart']").first
        first_add_button.click()
        
        # Wait for cart badge and get count
        page.wait_for_selector(".shopping_cart_badge")
        count_after_add = int(page.locator(".shopping_cart_badge").text_content())
        
        # Remove the product (button should change to "Remove")
        first_remove_button = page.locator("button[id^='remove']").first
        first_remove_button.click()
        
        # Verify cart count decreased or badge disappeared
        page.wait_for_timeout(1000)  # Wait for UI update
        
        cart_badge = page.locator(".shopping_cart_badge")
        if cart_badge.is_visible():
            count_after_remove = int(cart_badge.text_content())
            assert count_after_remove == count_after_add - 1, "Cart count should decrease by 1"
        else:
            # Badge disappeared, meaning cart is empty (count = 0)
            count_after_remove = 0
            assert count_after_remove == count_after_add - 1, "Cart should be empty after removing item"
        
        print(f"✅ Cart count decreased from {count_after_add} to {count_after_remove}")
    
    def test_product_sorting_name_az(self, page):
        """Test sorting products by name A-Z."""
        self.authenticated_session(page)
        
        # Sort products by name A-Z
        page.locator(".product_sort_container").select_option("az")
        
        # Get product names after sorting
        page.wait_for_timeout(1000)  # Wait for sorting to complete
        product_names = page.locator(".inventory_item_name").all_text_contents()
        
        # Verify products are sorted A-Z
        sorted_names = sorted(product_names)
        assert product_names == sorted_names, "Products should be sorted A-Z"
        
        print(f"✅ Products sorted A-Z: {product_names[:2]}...")
    
    def test_product_sorting_name_za(self, page):
        """Test sorting products by name Z-A."""
        self.authenticated_session(page)
        
        # Sort products by name Z-A
        page.locator(".product_sort_container").select_option("za")
        
        # Get product names after sorting
        page.wait_for_timeout(1000)  # Wait for sorting to complete
        product_names = page.locator(".inventory_item_name").all_text_contents()
        
        # Verify products are sorted Z-A
        sorted_names = sorted(product_names, reverse=True)
        assert product_names == sorted_names, "Products should be sorted Z-A"
        
        print(f"✅ Products sorted Z-A: {product_names[:2]}...")
    
    def test_shopping_cart_navigation(self, page):
        """Test navigation to shopping cart page."""
        self.authenticated_session(page)
        
        # Click shopping cart
        page.locator(".shopping_cart_link").click()
        
        # Verify navigation to cart page
        page.wait_for_url("**/cart.html")
        current_url = page.url
        assert "cart" in current_url, f"Should navigate to cart page, current URL: {current_url}"
        
        print("✅ Successfully navigated to cart page")
    
    def test_logout_functionality(self, page):
        """Test logout functionality from inventory page."""
        self.authenticated_session(page)
        
        # Open menu
        page.locator("#react-burger-menu-btn").click()
        
        # Wait for menu to open and click logout
        page.wait_for_selector("#logout_sidebar_link", state="visible")
        page.locator("#logout_sidebar_link").click()
        
        # Verify redirect to login page
        page.wait_for_url("https://www.saucedemo.com/")
        assert page.locator("[data-test='username']").is_visible(), "Should be redirected to login page after logout"
        
        # Verify URL is login page
        current_url = page.url
        assert "inventory" not in current_url, "Should not be on inventory page after logout"
        
        print("✅ Successfully logged out and returned to login page")
    
    @pytest.mark.parametrize("sort_option,expected_order", [
        ("az", "ascending"),
        ("za", "descending"),
        ("lohi", "price_ascending"),
        ("hilo", "price_descending")
    ])
    def test_product_sorting_options(self, page, sort_option, expected_order):
        """Test all sorting options."""
        self.authenticated_session(page)
        
        # Apply sorting
        page.locator(".product_sort_container").select_option(sort_option)
        page.wait_for_timeout(1000)
        
        if "price" in expected_order:
            # Test price sorting
            prices_text = page.locator(".inventory_item_price").all_text_contents()
            prices = [float(p.replace("$", "")) for p in prices_text]
            
            if "ascending" in expected_order:
                assert prices == sorted(prices), f"Prices should be sorted low to high"
            else:
                assert prices == sorted(prices, reverse=True), f"Prices should be sorted high to low"
        else:
            # Test name sorting
            names = page.locator(".inventory_item_name").all_text_contents()
            
            if expected_order == "ascending":
                assert names == sorted(names), f"Names should be sorted A-Z"
            else:
                assert names == sorted(names, reverse=True), f"Names should be sorted Z-A"
        
        print(f"✅ Sorting by {sort_option} works correctly")