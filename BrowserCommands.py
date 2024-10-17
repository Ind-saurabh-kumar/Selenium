import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()


url='https://opensource-demo.orangehrmlive.com/'
driver.get(url)

driver.minimize_window()
driver.fullscreen_window()

time.sleep(5)
forget_password = driver.find_element(By.CSS_SELECTOR, value=".oxd-text.oxd-text--p.orangehrm-login-forgot-header")
forget_password.click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()

driver.close()





