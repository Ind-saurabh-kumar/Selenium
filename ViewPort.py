import time
from selenium import webdriver 
from selenium.webdriver.common.by import By


viewport = [(1024, 764), (768,1024), (375,667), (414, 896)]

driver = webdriver.Firefox()
driver.maximize_window()

url="https://www.google.com/"
driver.get(url)
time.sleep(3)

try:
    for width, height in viewport:
        driver.set_window_size(width, height)
        time.sleep(4)
except Exception as e:
    print(e)


driver.close()
