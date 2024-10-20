import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

browser = webdriver.Firefox()
browser.maximize_window()

url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)

action = ActionChains(browser)

hover_element = browser.find_element(By.XPATH, value="//a[normalize-space()='SwitchTo']")


action.move_to_element(hover_element).perform()

ele = browser.find_element(By.XPATH, value="//a[normalize-space()='Frames']")
time.sleep(3)
ele.click()




time.sleep(5)
browser.close()