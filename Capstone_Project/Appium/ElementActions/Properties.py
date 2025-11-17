from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

options = UiAutomator2Options()
options.platform_name = 'Android'
options.platform_version = '16'
options.device_name = 'Pixel 7a'
options.app = 'C:/Users/sandeep.reddi/Downloads/KWADemo.apk'
options.app_package = 'com.code2lead.kwad'
options.app_activity = 'com.code2lead.kwad.MainActivity'
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
element = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")

print("Is Displayed : ", element.is_displayed())
print("Is Enabled : ", element.is_enabled())
print("Is selected : ", element.is_selected())
print("Size : ", element.size)
print("Location : ", element.location)