# import pytest
# from selenium import webdriver
#
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # IMPORTANT for GitHub Actions
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    yield driver
    driver.quit()

