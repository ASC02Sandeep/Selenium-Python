# conftest.py
# --- Very small driver fixture with headless toggle + Chrome/Edge choice ---

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://demowebshop.tricentis.com/"

def pytest_addoption(parser):
    # --browser: chrome or edge | --headless: true/false
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store", default="false")

@pytest.fixture(scope="session")
def config(request):
    """Tiny config object pulled from CLI flags."""
    return {
        "browser": request.config.getoption("--browser").lower(),
        "headless": request.config.getoption("--headless").lower() == "true",
        "base_url": BASE_URL
    }

@pytest.fixture
def driver(config):
    """Create WebDriver with headless toggle + implicit wait."""
    if config["browser"] == "edge":
        options = EdgeOptions()
        if config["headless"]:
            options.add_argument("--headless=new")
        drv = webdriver.Edge(options=options)
    else:
        options = ChromeOptions()
        if config["headless"]:
            options.add_argument("--headless=new")
        drv = webdriver.Chrome(options=options)

    drv.maximize_window()
    drv.implicitly_wait(5)   # implicit wait (basic)
    yield drv
    drv.quit()

@pytest.fixture
def wait(driver):
    """Explicit wait helper used in tests/pages when needed."""
    return WebDriverWait(driver, 10)

@pytest.fixture
def base_url(config):
    """Base URL to keep things DRY."""
    return config["base_url"]
