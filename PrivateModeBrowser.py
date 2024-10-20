import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


firefox_options = Options()
firefox_options.add_argument("--Private browsing")

driver = webdriver.Firefox(options=firefox_options)
driver.maximize_window()
time.sleep(15)
url = "https://wikipedia.com/"
driver.get(url)


time.sleep(5)
driver.close()
