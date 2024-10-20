import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

browser = webdriver.Firefox()
browser.maximize_window()

url = "https://the-internet.herokuapp.com/horizontal_slider"
browser.get(url)

slider = browser.find_element(By.XPATH, value="//input[@type='range']")
actions = ActionChains(browser)
actions.click_and_hold(slider).move_by_offset(25, 0).release().perform()



time.sleep(5)
browser.quit()