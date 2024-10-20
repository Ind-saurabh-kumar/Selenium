import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

browser = webdriver.Firefox()
browser.maximize_window()

url = "https:the-internet.herokuapp.com/drag_and_drop"
browser.get(url)

source_ele = browser.find_element(By.ID, value="column-a")
time.sleep(2)
destination = browser.find_element(By.ID, value="column-b")
actions = ActionChains(browser)
actions.drag_and_drop(source_ele, destination).perform()


time.sleep(5)
browser.close()
