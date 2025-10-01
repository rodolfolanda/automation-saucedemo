"""
Utility functions for test automation.
"""
import os
import json
from datetime import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path


class TestUtils:
    """Utility class containing helper methods for test automation."""
    
    @staticmethod
    def get_timestamp() -> str:
        """
        Get current timestamp as string.
        
        Returns:
            Formatted timestamp string
        """
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    @staticmethod
    def create_directory(path: str) -> None:
        """
        Create directory if it doesn't exist.
        
        Args:
            path: Directory path to create
        """
        Path(path).mkdir(parents=True, exist_ok=True)
    
    @staticmethod
    def save_test_results(results: Dict[str, Any], filename: str = None) -> str:
        """
        Save test results to JSON file.
        
        Args:
            results: Test results dictionary
            filename: Optional filename, if not provided uses timestamp
            
        Returns:
            Path to saved file
        """
        if not filename:
            filename = f"test_results_{TestUtils.get_timestamp()}.json"
        
        results_dir = "test-results"
        TestUtils.create_directory(results_dir)
        
        filepath = os.path.join(results_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        return filepath
    
    @staticmethod
    def load_test_data(filepath: str) -> Dict[str, Any]:
        """
        Load test data from JSON file.
        
        Args:
            filepath: Path to JSON file
            
        Returns:
            Loaded test data dictionary
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    @staticmethod
    def generate_screenshot_name(test_name: str, status: str = "failure") -> str:
        """
        Generate screenshot filename.
        
        Args:
            test_name: Name of the test
            status: Status of the test (failure, success, etc.)
            
        Returns:
            Screenshot filename
        """
        timestamp = TestUtils.get_timestamp()
        clean_test_name = test_name.replace(" ", "_").replace("/", "_")
        return f"{clean_test_name}_{status}_{timestamp}.png"
    
    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """
        Sanitize filename by removing invalid characters.
        
        Args:
            filename: Original filename
            
        Returns:
            Sanitized filename
        """
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        return filename
    
    @staticmethod
    def format_price(price_str: str) -> float:
        """
        Convert price string to float value.
        
        Args:
            price_str: Price string (e.g., "$29.99")
            
        Returns:
            Price as float value
        """
        return float(price_str.replace('$', ''))
    
    @staticmethod
    def wait_for_condition(condition_func, timeout: int = 5000, interval: int = 100) -> bool:
        """
        Wait for a condition to be true with polling.
        
        Args:
            condition_func: Function that returns boolean
            timeout: Maximum wait time in milliseconds
            interval: Polling interval in milliseconds
            
        Returns:
            True if condition met, False if timeout
        """
        import asyncio
        import time
        
        start_time = time.time()
        while (time.time() - start_time) * 1000 < timeout:
            if condition_func():
                return True
            time.sleep(interval / 1000)
        return False


class EnvironmentUtils:
    """Utility class for environment and configuration management."""
    
    @staticmethod
    def get_env_var(var_name: str, default: str = None) -> Optional[str]:
        """
        Get environment variable value.
        
        Args:
            var_name: Environment variable name
            default: Default value if variable not found
            
        Returns:
            Environment variable value or default
        """
        return os.getenv(var_name, default)
    
    @staticmethod
    def is_headless_mode() -> bool:
        """
        Check if tests should run in headless mode.
        
        Returns:
            True if headless mode, False otherwise
        """
        return EnvironmentUtils.get_env_var('HEADLESS', 'true').lower() == 'true'
    
    @staticmethod
    def get_browser_name() -> str:
        """
        Get browser name from environment.
        
        Returns:
            Browser name (chromium, firefox, webkit)
        """
        return EnvironmentUtils.get_env_var('BROWSER', 'chromium').lower()
    
    @staticmethod
    def get_base_url() -> str:
        """
        Get base URL for testing.
        
        Returns:
            Base URL for the application
        """
        return EnvironmentUtils.get_env_var('BASE_URL', 'https://www.saucedemo.com')
    
    @staticmethod
    def get_timeout() -> int:
        """
        Get default timeout value.
        
        Returns:
            Timeout value in milliseconds
        """
        return int(EnvironmentUtils.get_env_var('TIMEOUT', '30000'))


class ReportUtils:
    """Utility class for test reporting functionality."""
    
    @staticmethod
    def generate_test_summary(results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate test execution summary.
        
        Args:
            results: List of test result dictionaries
            
        Returns:
            Summary dictionary with statistics
        """
        total_tests = len(results)
        passed_tests = len([r for r in results if r.get('status') == 'passed'])
        failed_tests = len([r for r in results if r.get('status') == 'failed'])
        skipped_tests = len([r for r in results if r.get('status') == 'skipped'])
        
        return {
            'total_tests': total_tests,
            'passed_tests': passed_tests,
            'failed_tests': failed_tests,
            'skipped_tests': skipped_tests,
            'pass_rate': (passed_tests / total_tests * 100) if total_tests > 0 else 0,
            'execution_time': datetime.now().isoformat(),
            'results': results
        }
    
    @staticmethod
    def create_html_report(summary: Dict[str, Any], output_path: str = "test_report.html") -> str:
        """
        Create basic HTML test report.
        
        Args:
            summary: Test summary dictionary
            output_path: Output file path
            
        Returns:
            Path to generated HTML report
        """
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Execution Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .summary {{ background-color: #f5f5f5; padding: 15px; border-radius: 5px; }}
                .passed {{ color: green; }}
                .failed {{ color: red; }}
                .skipped {{ color: orange; }}
                table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>Test Execution Report</h1>
            <div class="summary">
                <h2>Summary</h2>
                <p><strong>Total Tests:</strong> {summary['total_tests']}</p>
                <p><strong class="passed">Passed:</strong> {summary['passed_tests']}</p>
                <p><strong class="failed">Failed:</strong> {summary['failed_tests']}</p>
                <p><strong class="skipped">Skipped:</strong> {summary['skipped_tests']}</p>
                <p><strong>Pass Rate:</strong> {summary['pass_rate']:.2f}%</p>
                <p><strong>Execution Time:</strong> {summary['execution_time']}</p>
            </div>
        </body>
        </html>
        """
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_template)
        
        return output_path