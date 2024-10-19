import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()

url = "https://www.globalsqa.com/demo-site/datepicker"
browser.get(url)






time.sleep(3)
browser.close()