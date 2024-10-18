import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://the-internet.herokuapp.com/iframe"
browser = webdriver.Firefox()
browser.maximize_window()

browser.get(url)

iframe = browser.find_element(By.ID, value='mce_0_ifr')
browser.switch_to.frame(iframe)

text_editor = browser.find_element(By.ID, value='tinymce')
text_editor.clear()

text_editor.send_keys("This is Saurabh Kumar here ")

time.sleep(5)

browser.switch_to.default_content()
Selenium_link = browser.find_element(By.XPATH,value="//a[normalize-space()='Elemental Selenium']")
Selenium_link.click()


