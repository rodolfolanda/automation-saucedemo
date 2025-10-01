# SauceDemo Test Automation Project

A comprehensive test automation framework for testing [www.saucedemo.com](https://www.saucedemo.com) using Python, Playwright, and pytest. This project implements the Page Object Model pattern and follows best practices for maintainable test automation.

## 🚀 Features

- **Page Object Model**: Clean separation of page logic and test logic
- **Async/Await Support**: Modern asynchronous testing with Playwright
- **Cross-Browser Testing**: Support for Chromium, Firefox, and WebKit
- **Parallel Execution**: Run tests in parallel for faster execution
- **Rich Reporting**: HTML reports, screenshots, and videos on failure
- **CI/CD Ready**: GitHub Actions workflow included
- **Data-Driven Testing**: Parametrized tests with external test data
- **Comprehensive Logging**: Detailed logging with multiple levels
- **Utility Functions**: Helper functions for common operations

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/automation-saucedemo.git
   cd automation-saucedemo
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\\Scripts\\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

## 📁 Project Structure

```
automation-saucedemo/
├── .github/
│   ├── workflows/
│   │   └── ci.yml                 # GitHub Actions CI/CD workflow
│   └── copilot-instructions.md    # GitHub Copilot instructions
├── data/
│   ├── __init__.py
│   └── test_data.py               # Test data and constants
├── pages/
│   ├── __init__.py
│   ├── base_page.py               # Base page class
│   ├── login_page.py              # Login page object
│   └── inventory_page.py          # Inventory page object
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # Pytest fixtures and configuration
│   ├── test_login.py              # Login functionality tests
│   └── test_inventory.py          # Inventory page tests
├── utils/
│   ├── __init__.py
│   ├── test_utils.py              # Utility functions
│   └── logger.py                  # Logging configuration
├── .gitignore                     # Git ignore file
├── playwright.config.py           # Playwright configuration
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

## 🧪 Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Test File
```bash
pytest tests/test_login.py
```

### Run Tests by Marker
```bash
# Run smoke tests only
pytest -m smoke

# Run login tests only
pytest -m login

# Run inventory tests only  
pytest -m inventory
```

### Run Tests in Specific Browser
```bash
# Run in Firefox
pytest --browser firefox

# Run in WebKit (Safari)
pytest --browser webkit
```

### Run Tests in Parallel
```bash
# Run with 4 workers
pytest -n 4

# Run with auto-detection of CPU cores
pytest -n auto
```

### Run Tests with Live Browser (Non-headless)
```bash
pytest --headed
```

### Generate HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

## 🎯 Test Markers

The project uses pytest markers to categorize tests:

- `@pytest.mark.smoke` - Critical smoke tests
- `@pytest.mark.regression` - Regression test suite  
- `@pytest.mark.login` - Login functionality tests
- `@pytest.mark.inventory` - Inventory page tests
- `@pytest.mark.checkout` - Checkout process tests

## 📊 Test Data

Test data is centralized in the `data/test_data.py` file and includes:

- **Valid Users**: Standard users for successful login tests
- **Invalid Users**: Test data for negative login scenarios
- **Expected Products**: Product information for inventory validation
- **Error Messages**: Expected error messages for validation
- **URLs**: Application URLs for navigation
- **Timeouts**: Configurable timeout values

## 🔧 Configuration

### Playwright Configuration
The `playwright.config.py` file contains:
- Browser settings (Chromium, Firefox, WebKit)
- Viewport settings
- Screenshot and video capture settings
- Timeout configurations
- Retry settings

### Pytest Configuration  
The `pytest.ini` file configures:
- Test discovery patterns
- HTML report generation
- Test markers
- Output settings

### Environment Variables
You can customize test execution using environment variables:

```bash
# Set headless mode
export HEADLESS=false

# Set browser
export BROWSER=firefox

# Set base URL
export BASE_URL=https://www.saucedemo.com

# Set timeout
export TIMEOUT=60000
```

## 📝 Writing Tests

### Basic Test Structure
```python
import pytest
from pages import LoginPage, InventoryPage

class TestExample:
    @pytest.mark.smoke
    async def test_example(self, login_page: LoginPage):
        await login_page.navigate_to_login()
        await login_page.login("standard_user", "secret_sauce")
        # Add assertions here
```

### Using Page Objects
```python
# Access page elements and methods
await login_page.enter_username("standard_user")
await login_page.enter_password("secret_sauce") 
await login_page.click_login()

# Or use the combined method
await login_page.login("standard_user", "secret_sauce")
```

### Data-Driven Tests
```python
@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
])
async def test_multiple_users(self, login_page, username, password):
    await login_page.login(username, password)
    # Add assertions
```

## 🔍 Debugging Tests

### Debug Mode
Run tests with verbose output and disable capture:
```bash
pytest -v -s
```

### Debug Single Test
```bash
pytest tests/test_login.py::TestLogin::test_successful_login_standard_user -v -s
```

### View Test Results
- **Screenshots**: Saved in `test-results/` on failure
- **Videos**: Recorded on failure (if enabled)
- **Logs**: Available in `test-results/logs/`
- **HTML Reports**: Generated in `reports/` directory

## 📈 Continuous Integration

The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that:
- Runs on push and pull requests
- Tests across multiple Python versions
- Executes tests in parallel
- Generates and uploads test reports
- Stores test artifacts (screenshots, videos, logs)

### Manual CI Trigger
You can manually trigger the CI workflow from the GitHub Actions tab in your repository.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following the coding standards
4. Add tests for new functionality
5. Run the test suite (`pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Coding Standards
- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Add docstrings for classes and methods
- Use type hints where applicable
- Write comprehensive tests for new features

## 📋 Available Test Scenarios

### Login Tests
- ✅ Successful login with valid credentials
- ❌ Login with invalid credentials
- ❌ Login with empty username/password
- ❌ Login with locked out user
- ⚠️ Error message validation and dismissal

### Inventory Tests  
- ✅ Inventory page loading and product display
- 🛒 Add/remove products to/from cart
- 🔄 Product sorting (name A-Z, Z-A, price low-high, high-low)
- 📦 Cart badge count validation
- 🔍 Product details retrieval
- 🚪 Logout functionality

## 🐛 Troubleshooting

### Common Issues

**Issue: `playwright` module not found**
```bash
pip install playwright
playwright install
```

**Issue: Browser launch fails**
```bash
# Install system dependencies (Linux)
playwright install-deps

# Or install specific browser
playwright install chromium
```

**Issue: Tests timing out**
- Increase timeout values in `playwright.config.py`
- Check network connectivity to saucedemo.com
- Run tests with `--headed` to see browser actions

**Issue: Import errors**
- Ensure you're in the project root directory
- Activate your virtual environment
- Check Python path: `python -c "import sys; print(sys.path)"`

## 📞 Support

For questions or issues:
1. Check the [troubleshooting section](#-troubleshooting)
2. Review existing [GitHub Issues](https://github.com/yourusername/automation-saucedemo/issues)
3. Create a new issue with detailed information
4. Include error messages, logs, and steps to reproduce

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Playwright](https://playwright.dev/) - Modern web testing framework
- [pytest](https://pytest.org/) - Testing framework for Python
- [SauceDemo](https://www.saucedemo.com) - Demo application for testing
- Contributors and maintainers

---

**Happy Testing! 🎉**