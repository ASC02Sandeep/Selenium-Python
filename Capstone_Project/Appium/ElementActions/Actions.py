from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

options = UiAutomator2Options()
options.platform_name = 'Android'
options.platform_version = '16'
options.device_name = 'Pixel 7a'
options.app = 'C:/Users/sandeep.reddi/Downloads/KWADemo.apk'
options.app_package = 'com.code2lead.kwad'
options.app_activity = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)



ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
print("Text on the Button ", ele_id.text)
print("Text on the Button ", ele_id.get_attribute("text"))
print("Content Des  of the Button ", ele_id.get_attribute("content-desc"))
ele_id.click()

time.sleep(2)

ele_class = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_class.send_keys("Skill2Lead")
time.sleep(2)
ele_class.clear()
time.sleep(2)
ele_class.send_keys("Skill2Lead")
ele_submit=driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/Btn1")
ele_submit.click()

time.sleep(2)
driver.quit()