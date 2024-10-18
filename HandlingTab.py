import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()

url = "https://www.selenium.dev/"
browser.get(url)

browser.switch_to.new_window()

url2 = "https://playwright.dev/"
browser.get(url2)

number_of_tabs = len(browser.window_handles)
print(number_of_tabs)

tabs_value = browser.window_handles
print(tabs_value)

curr_tab = browser.current_window_handle
print(curr_tab)

time.sleep(2)
btn = browser.find_element(By.CSS_SELECTOR, value=".getStarted_Sjon")
btn.click()

FirstTab = browser.window_handles[0]

if curr_tab != FirstTab:
    browser.switch_to.window(FirstTab)

download = browser.find_element(By.XPATH, value="//span[normalize-space()='Downloads']")

download.click()


