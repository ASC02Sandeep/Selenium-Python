import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = 'Pixel 7a'
options.app = 'C:/Users/sandeep.reddi/Downloads/KWADemo.apk'
options.app_package = 'com.code2lead.kwad'
options.app_activity = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("TAB ACTIVITY")'))
ele.click()

time.sleep(5)

######Right to Left#######
hometab = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("HomeFragment")'))
time.sleep(5)
driver.execute_script("mobile: swipeGesture", {'elementId': hometab, 'direction': 'left', "percent": 0.98})

time.sleep(5)
###### Left to Right    #######
sporttab = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("SportFragment")'))

driver.execute_script("mobile: swipeGesture", {'elementId': sporttab, 'direction': 'right', "percent": 0.98})

time.sleep(3)

driver.quit()