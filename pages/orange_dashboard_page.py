from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrangeDashboardPage:
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")

    def is_dashboard_displayed(self, driver):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(self.DASHBOARD_HEADER)
        )
        return True
