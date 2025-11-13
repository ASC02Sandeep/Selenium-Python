from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

print("🤖 Starting Ultra Simple Appium Test")

try:
    # Simple configuration
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Pixel_9_Pro"
    options.automation_name = "UiAutomator2"

    # Connect to Appium
    driver = webdriver.Remote("http://localhost:4723", options=options)

    print("✅ Connected to Small_Phone emulator!")

    # Just prove it works
    print(f"Device: {driver.capabilities.get('deviceName')}")

    # Take a screenshot
    driver.save_screenshot("proof_image.png")
    print("📸 Took screenshot: proof.png")

    # Keep it open for 5 seconds so you can see it working
    print("⏳ Waiting 5 seconds...")
    time.sleep(5)

    driver.quit()
    print("✅ Test completed!")

except Exception as e:
    print(f"❌ Error: {e}")