from appium import webdriver
from appium.options.android import UiAutomator2Options
# from appium.webdriver.common import touch_action
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time

options = UiAutomator2Options()
options.platform_name = 'Android'
options.platform_version = '16'
options.device_name = 'Pixel 7a'
options.app = 'C:/Users/sandeep.reddi/Downloads/KWADemo.apk'
options.app_package = 'com.code2lead.kwad'
options.app_activity = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# list of Selenium Exceptions
# https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html
wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele_scroll = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                 'new UiScrollable(new UiSelector()).scrollIntoView(text("LONG CLICK"))'))
# actions=touch_action(driver)
# actions.long_press()

# TouchAction is depriciated

action = ActionChains(driver)
action.click_and_hold(ele_scroll).perform()

time.sleep(4)
driver.quit()
