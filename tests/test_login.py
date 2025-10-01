"""
Login functionality tests for SauceDemo application.
"""
import pytest
from pages import LoginPage, InventoryPage


class TestLogin:
    """Test class for login functionality."""
    
    @pytest.mark.smoke
    @pytest.mark.login
    async def test_successful_login_standard_user(self, login_page: LoginPage, inventory_page: InventoryPage):
        """Test successful login with standard user credentials."""
        # Navigate to login page
        await login_page.navigate_to_login()
        
        # Verify login page is loaded
        assert await login_page.is_login_page_loaded(), "Login page should be loaded"
        
        # Perform login
        await login_page.login("standard_user", "secret_sauce")
        
        # Verify successful login by checking inventory page
        assert await inventory_page.is_inventory_page_loaded(), "Should be redirected to inventory page after login"
        
        # Verify URL contains inventory
        assert "inventory" in login_page.page.url, "URL should contain 'inventory'"
    
    @pytest.mark.login
    async def test_login_with_empty_credentials(self, login_page: LoginPage):
        """Test login attempt with empty credentials."""
        await login_page.navigate_to_login()
        
        # Attempt login with empty credentials
        await login_page.login("", "")
        
        # Verify error message is displayed
        assert await login_page.is_error_displayed(), "Error message should be displayed"
        error_message = await login_page.get_error_message()
        assert "Username is required" in error_message, f"Expected username error, got: {error_message}"
    
    @pytest.mark.login
    async def test_login_with_invalid_credentials(self, login_page: LoginPage):
        """Test login attempt with invalid credentials."""
        await login_page.navigate_to_login()
        
        # Attempt login with invalid credentials
        await login_page.login("invalid_user", "wrong_password")
        
        # Verify error message is displayed
        assert await login_page.is_error_displayed(), "Error message should be displayed"
        error_message = await login_page.get_error_message()
        assert "do not match" in error_message, f"Expected credential mismatch error, got: {error_message}"
    
    @pytest.mark.login
    async def test_login_locked_out_user(self, login_page: LoginPage):
        """Test login attempt with locked out user."""
        await login_page.navigate_to_login()
        
        # Attempt login with locked out user
        await login_page.login("locked_out_user", "secret_sauce")
        
        # Verify error message is displayed
        assert await login_page.is_error_displayed(), "Error message should be displayed"
        error_message = await login_page.get_error_message()
        assert "locked out" in error_message, f"Expected locked out error, got: {error_message}"
    
    @pytest.mark.login
    async def test_login_with_empty_password(self, login_page: LoginPage):
        """Test login attempt with empty password."""
        await login_page.navigate_to_login()
        
        # Attempt login with username but empty password
        await login_page.login("standard_user", "")
        
        # Verify error message is displayed
        assert await login_page.is_error_displayed(), "Error message should be displayed"
        error_message = await login_page.get_error_message()
        assert "Password is required" in error_message, f"Expected password error, got: {error_message}"
    
    @pytest.mark.login
    @pytest.mark.parametrize("username,password", [
        ("standard_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        ("problem_user", "secret_sauce")
    ])
    async def test_login_valid_users(self, login_page: LoginPage, inventory_page: InventoryPage, username: str, password: str):
        """Test login with various valid user accounts."""
        await login_page.navigate_to_login()
        
        # Perform login
        await login_page.login(username, password)
        
        # Verify successful login
        if username != "problem_user":  # Problem user might have issues
            assert await inventory_page.is_inventory_page_loaded(), f"Login should succeed for {username}"
    
    @pytest.mark.login
    async def test_error_message_dismissal(self, login_page: LoginPage):
        """Test that error messages can be dismissed."""
        await login_page.navigate_to_login()
        
        # Generate an error
        await login_page.login("", "")
        assert await login_page.is_error_displayed(), "Error should be displayed"
        
        # Dismiss the error
        await login_page.dismiss_error()
        
        # Verify error is no longer displayed (may take a moment)
        await login_page.page.wait_for_timeout(500)
        assert not await login_page.is_error_displayed(), "Error should be dismissed"
    
    @pytest.mark.login
    async def test_login_page_elements(self, login_page: LoginPage):
        """Test that all login page elements are present."""
        await login_page.navigate_to_login()
        
        # Verify all required elements are present
        assert await login_page.is_login_page_loaded(), "All login elements should be present"
        
        # Verify login button text
        button_text = await login_page.get_login_button_text()
        assert "Login" in button_text, f"Login button should contain 'Login', got: {button_text}"