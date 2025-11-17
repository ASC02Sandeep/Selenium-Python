from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
# Step 1 : Create "Desired Capabilities"
from selenium.common import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait

options = UiAutomator2Options()
options.platform_name = 'Android'
options.platform_version = '16'
options.device_name = 'Pixel 7a'
options.app = 'C:/Users/sandeep.reddi/Downloads/KWADemo.apk'
options.app_package = 'com.code2lead.kwad'
options.app_activity = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                          'new UiScrollable(new UiSelector()).scrollIntoView(text("LOGIN"))'))

driver.execute_script('mobile: clickGesture', {'x': 640, 'y': 2074})

""" 
actions = TouchAction(driver)
#actions.tap(None,700,1990,1)
actions.tap(ele,940,2400,1)
actions.perform()"""

time.sleep(2)
driver.quit()
