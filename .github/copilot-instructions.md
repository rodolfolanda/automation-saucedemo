<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Playwright Python Test Automation Project

This project uses Playwright with Python for testing www.saucedemo.com. The codebase follows page object model patterns and pytest for test execution.

## Project Structure Guidelines
- Use page object model pattern for UI interactions
- Follow pytest conventions for test naming and organization
- Keep test data in separate JSON files
- Use async/await patterns for Playwright operations
- Implement proper error handling and logging

## Coding Standards
- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Add docstrings for classes and methods
- Use type hints where applicable
- Keep functions focused and testable

## Test Organization
- Group related tests in classes
- Use fixtures for setup and teardown
- Implement data-driven testing where appropriate
- Use assertions that provide clear failure messages