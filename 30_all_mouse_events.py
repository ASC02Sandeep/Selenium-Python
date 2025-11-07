from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def mouse_actions_demo():
    driver = webdriver.Chrome()
    driver.maximize_window()

    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 10)

    #  move_to_element, click, double_click, context_click
    driver.get("https://demoqa.com/buttons")

    double_btn = wait.until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))
    right_btn = wait.until(EC.element_to_be_clickable((By.ID, "rightClickBtn")))
    click_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click Me']")))

    # move_to_element + click
    actions.move_to_element(click_btn).click().perform()
    time.sleep(1)

    # double_click
    actions.double_click(double_btn).perform()
    time.sleep(1)

    # context_click (right-click)
    actions.context_click(right_btn).perform()
    time.sleep(1)

    print("Click, double-click, and right-click performed successfully.")

    #  click_and_hold, release, drag_and_drop, drag_and_drop_by_offset, move_by_offset
    driver.get("https://demoqa.com/droppable")

    source = wait.until(EC.element_to_be_clickable((By.ID, "draggable")))
    target = wait.until(EC.element_to_be_clickable((By.ID, "droppable")))

    # click_and_hold + release
    actions.click_and_hold(source).pause(1).release().perform()
    print(" Click and hold + release demo done.")
    time.sleep(1)

    # drag_and_drop
    actions.drag_and_drop(source, target).perform()
    print("Drag and drop completed.")
    time.sleep(1)

    # drag_and_drop_by_offset (move 100px right, 50px down)
    actions.drag_and_drop_by_offset(source, 50, 30).perform()
    print("Drag and drop by offset completed safely.")

    time.sleep(1)

    # move_by_offset (move mouse pointer by x/y pixels)
    # move pointer to the element's center, then move by offset
    actions = ActionChains(driver)  # create fresh actions
    actions.move_to_element(source).move_by_offset(50, 30).release().perform()

    time.sleep(3)
    driver.quit()


mouse_actions_demo()