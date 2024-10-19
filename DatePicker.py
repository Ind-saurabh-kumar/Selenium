import time
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


browser = webdriver.Firefox()
browser.maximize_window()

url = "https://www.globalsqa.com/demo-site/datepicker"
browser.get(url)


date = browser.find_element(By.XPATH, value='//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//a[@class="close_img"]')
date.click()

frameLo = browser.find_element(By.XPATH, value='//iframe[@class="demo-frame lazyloaded"]')
browser.switch_to.frame(frameLo)
time.sleep(5)


datePick = browser.find_element(By.CSS_SELECTOR, value="#datepicker")
datePick.click()

currDate = datetime.now()
next_date = currDate + timedelta(days=5)

date_formate = currDate.strftime("%m/%d/%y")
browser.find_element(By.CSS_SELECTOR, value="#datepicker").send_keys(date_formate + Keys.TAB)


time.sleep(3)
browser.quit()