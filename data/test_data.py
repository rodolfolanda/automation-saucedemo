"""
Test data for SauceDemo application tests.
"""

# Valid user credentials
VALID_USERS = {
    "standard_user": {
        "username": "standard_user",
        "password": "secret_sauce",
        "description": "Standard user with normal functionality"
    },
    "performance_glitch_user": {
        "username": "performance_glitch_user", 
        "password": "secret_sauce",
        "description": "User that experiences performance issues"
    },
    "problem_user": {
        "username": "problem_user",
        "password": "secret_sauce", 
        "description": "User that experiences various UI issues"
    },
    "error_user": {
        "username": "error_user",
        "password": "secret_sauce",
        "description": "User that experiences errors"
    }
}

# Invalid user credentials for negative testing
INVALID_USERS = {
    "locked_out": {
        "username": "locked_out_user",
        "password": "secret_sauce",
        "expected_error": "Sorry, this user has been locked out."
    },
    "invalid_username": {
        "username": "invalid_user",
        "password": "secret_sauce",
        "expected_error": "Username and password do not match"
    },
    "invalid_password": {
        "username": "standard_user",
        "password": "wrong_password",
        "expected_error": "Username and password do not match"
    },
    "empty_username": {
        "username": "",
        "password": "secret_sauce",
        "expected_error": "Username is required"
    },
    "empty_password": {
        "username": "standard_user", 
        "password": "",
        "expected_error": "Password is required"
    },
    "empty_both": {
        "username": "",
        "password": "",
        "expected_error": "Username is required"
    }
}

# Expected product information
EXPECTED_PRODUCTS = [
    {
        "name": "Sauce Labs Backpack",
        "price": "$29.99",
        "id": "sauce-labs-backpack"
    },
    {
        "name": "Sauce Labs Bike Light",
        "price": "$9.99", 
        "id": "sauce-labs-bike-light"
    },
    {
        "name": "Sauce Labs Bolt T-Shirt",
        "price": "$15.99",
        "id": "sauce-labs-bolt-t-shirt"
    },
    {
        "name": "Sauce Labs Fleece Jacket",
        "price": "$49.99",
        "id": "sauce-labs-fleece-jacket"
    },
    {
        "name": "Sauce Labs Onesie",
        "price": "$7.99",
        "id": "sauce-labs-onesie"
    },
    {
        "name": "Test.allTheThings() T-Shirt (Red)",
        "price": "$15.99",
        "id": "test.allthethings()-t-shirt-(red)"
    }
]

# Sort options for product sorting tests
SORT_OPTIONS = {
    "name_az": "az",
    "name_za": "za", 
    "price_low_high": "lohi",
    "price_high_low": "hilo"
}

# Error messages
ERROR_MESSAGES = {
    "locked_out": "Sorry, this user has been locked out.",
    "invalid_credentials": "Username and password do not match any user in this service",
    "empty_username": "Username is required",
    "empty_password": "Password is required"
}

# URLs
URLS = {
    "base_url": "https://www.saucedemo.com",
    "login": "https://www.saucedemo.com/",
    "inventory": "https://www.saucedemo.com/inventory.html",
    "cart": "https://www.saucedemo.com/cart.html",
    "checkout_step_one": "https://www.saucedemo.com/checkout-step-one.html",
    "checkout_step_two": "https://www.saucedemo.com/checkout-step-two.html",
    "checkout_complete": "https://www.saucedemo.com/checkout-complete.html"
}

# Test timeouts (in milliseconds)
TIMEOUTS = {
    "default": 5000,
    "short": 3000,
    "long": 10000,
    "performance_glitch": 15000
}