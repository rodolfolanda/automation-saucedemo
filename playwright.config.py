from typing import Dict, Any

# Playwright configuration
config: Dict[str, Any] = {
    "use": {
        "headless": True,
        "viewport": {"width": 1280, "height": 720},
        "ignoreHTTPSErrors": True,
        "screenshot": "only-on-failure",
        "video": "retain-on-failure",
        "trace": "retain-on-failure",
    },
    "projects": [
        {
            "name": "chromium",
            "use": {"browserName": "chromium"},
        },
        {
            "name": "firefox",
            "use": {"browserName": "firefox"},
        },
        {
            "name": "webkit",
            "use": {"browserName": "webkit"},
        },
    ],
    "timeout": 30000,
    "expect": {"timeout": 5000},
    "fullyParallel": True,
    "forbidOnly": True,
    "retries": 2,
    "workers": 4,
    "reporter": [
        ["html", {"outputFolder": "playwright-report"}],
        ["junit", {"outputFile": "test-results.xml"}],
    ],
    "outputDir": "test-results/",
}