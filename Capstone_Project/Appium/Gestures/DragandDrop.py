from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

# Set Appium options
options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = 'Pixel 7a'
options.app = 'C:/Users/sandeep.reddi/Downloads/KWADemo.apk'
options.app_package = 'com.code2lead.kwad'
options.app_activity = 'com.code2lead.kwad.MainActivity'

# Start driver
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
time.sleep(3)

# Scroll and click on DRAGANDDROP
dragdrop_button = driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'
)
time.sleep(2)
dragdrop_button.click()

time.sleep(2)

# Find source and target elements
source = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ingvw")
target = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/layout2")

# Get element centers
start = source.rect
end = target.rect
start_x = start['x'] + start['width'] // 2
start_y = start['y'] + start['height'] // 2
end_x = end['x'] + end['width'] // 2
end_y = end['y'] + end['height'] // 2

# Create pointer input for touch
finger = PointerInput("touch", "finger")
action_builder = ActionBuilder(driver, mouse=finger)  # <- Correct way
pointer = action_builder.pointer_action

pointer.move_to_location(start_x, start_y)
pointer.pointer_down()
pointer.pause(0.5)
pointer.move_to_location(end_x, end_y)
pointer.pointer_up()
action_builder.perform()

time.sleep(3)
print("Drag and drop successfully executed")
driver.quit()
