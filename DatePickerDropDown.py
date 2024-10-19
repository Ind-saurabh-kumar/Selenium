import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.maximize_window()

url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)





time.sleep(5)
browser.quit()