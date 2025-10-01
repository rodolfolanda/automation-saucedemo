"""
Logger configuration and utilities for test automation.
"""
import logging
import os
from datetime import datetime
from typing import Optional


class TestLogger:
    """Custom logger class for test automation."""
    
    def __init__(self, name: str = "test_automation", log_level: str = "INFO"):
        """
        Initialize the logger.
        
        Args:
            name: Logger name
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, log_level.upper()))
        
        # Prevent adding multiple handlers if logger already exists
        if not self.logger.handlers:
            self._setup_handlers()
    
    def _setup_handlers(self) -> None:
        """Set up console and file handlers for the logger."""
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # File handler
        log_dir = "test-results/logs"
        os.makedirs(log_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(log_dir, f"test_execution_{timestamp}.log")
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
    
    def debug(self, message: str) -> None:
        """Log debug message."""
        self.logger.debug(message)
    
    def info(self, message: str) -> None:
        """Log info message."""
        self.logger.info(message)
    
    def warning(self, message: str) -> None:
        """Log warning message."""
        self.logger.warning(message)
    
    def error(self, message: str) -> None:
        """Log error message."""
        self.logger.error(message)
    
    def critical(self, message: str) -> None:
        """Log critical message."""
        self.logger.critical(message)
    
    def test_start(self, test_name: str) -> None:
        """Log test start."""
        self.info(f"🚀 Starting test: {test_name}")
    
    def test_pass(self, test_name: str) -> None:
        """Log test pass."""
        self.info(f"✅ Test passed: {test_name}")
    
    def test_fail(self, test_name: str, error_message: str = "") -> None:
        """Log test failure."""
        self.error(f"❌ Test failed: {test_name}")
        if error_message:
            self.error(f"Error details: {error_message}")
    
    def test_skip(self, test_name: str, reason: str = "") -> None:
        """Log test skip."""
        self.warning(f"⏭️ Test skipped: {test_name}")
        if reason:
            self.warning(f"Skip reason: {reason}")
    
    def action(self, action: str) -> None:
        """Log user action."""
        self.info(f"🎬 Action: {action}")
    
    def verification(self, verification: str, result: bool) -> None:
        """Log verification step."""
        status = "✅" if result else "❌"
        self.info(f"{status} Verification: {verification} - {'PASS' if result else 'FAIL'}")


# Global logger instance
logger = TestLogger()


def get_logger(name: Optional[str] = None) -> TestLogger:
    """
    Get logger instance.
    
    Args:
        name: Optional logger name
        
    Returns:
        TestLogger instance
    """
    if name:
        return TestLogger(name)
    return logger