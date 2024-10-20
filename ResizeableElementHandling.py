import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


browser = webdriver.Firefox()
browser.maximize_window()

url = "https://demo.automationtesting.in/Resizable.html"
browser.get(url)

resizable_ele = browser.find_element(By.XPATH, value='//div[@class="ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se"]')
Initial_ele_size = browser.find_element(By.XPATH, value="//div[@id ='resizable']")
initial_size = Initial_ele_size.size
print(initial_size)
time.sleep(5)
action_chains = ActionChains(browser)
action_chains.click_and_hold(resizable_ele).move_by_offset(100, 100).release().perform()
resized_ele_size = Initial_ele_size.size
print(f"Resized size is {resized_ele_size}")

time.sleep(5)
browser.quit()