import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.maximize_window()


username = 'admin'
password = 'admin'

# https://username:password@domain/path
url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
browser.get(url)

time.sleep(5)
browser.close()