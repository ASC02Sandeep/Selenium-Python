# pages/home_page.py
# Covers: LOCATORS (id/name/class/link_text/partial_link/css/xpath), search, newsletter (AJAX), actions

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
    """Home page: search bar, newsletter, top menu interactions."""
    URL = "https://demowebshop.tricentis.com/"

    # --- Locators ---
    SEARCH_INPUT = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.button-1.search-box-button")
    NEWSLETTER_EMAIL = (By.ID, "newsletter-email")
    NEWSLETTER_BUTTON = (By.ID, "newsletter-subscribe-button")
    NEWSLETTER_RESULT = (By.ID, "newsletter-result-block")
    HEADER_LOGO = (By.CSS_SELECTOR, "div.header-logo")
    BOOKS_LINK = (By.LINK_TEXT, "Books")
    COMPUTERS_LINK = (By.PARTIAL_LINK_TEXT, "Comput")

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    # def open(self, base_url):
    #     self.driver.get(base_url)

    def open(self, base_url):
        """Open home page."""
        self.driver.get(base_url)

        #  Force a complete reload to avoid stale DOM when running full suite
        self.driver.refresh()

    def search(self, keyword):
        self.driver.find_element(*self.SEARCH_INPUT).clear()
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(keyword)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def subscribe_newsletter(self, email):
        self.driver.find_element(*self.NEWSLETTER_EMAIL).clear()
        self.driver.find_element(*self.NEWSLETTER_EMAIL).send_keys(email)
        self.driver.find_element(*self.NEWSLETTER_BUTTON).click()

    def hover_header(self):
        logo = self.driver.find_element(*self.HEADER_LOGO)
        self.actions.move_to_element(logo).perform()

    # THIS IS THE MISSING METHOD FOR YOUR TEST
    def go_to_books(self):
        """Navigate to 'Books' category using LINK_TEXT."""
        self.driver.find_element(*self.BOOKS_LINK).click()

    # Existing alternative method (kept untouched)
    def go_to_books_category(self):
        self.driver.find_element(*self.BOOKS_LINK).click()

    def go_to_computers(self):
        self.driver.find_element(*self.COMPUTERS_LINK).click()



#
