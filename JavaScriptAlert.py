import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()

url = "https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)

AlertButton = browser.find_element(By.XPATH, value="//button[normalize-space()='Click for JS Alert']")

AlertButton.click()

alertText = browser.switch_to.alert
alert_txt = alertText.text

print(alert_txt)

time.sleep(5)
alertText.accept()
time.sleep(5)

# second button


cnfBtn = browser.find_element(By.XPATH, value="//button[normalize-space()='Click for JS Confirm']")
cnfBtn.click()
cnfAlert = browser.switch_to.alert
cnfAlert_txt = cnfAlert.text
print(cnfAlert_txt)
time.sleep(5)
cnfAlert.dismiss()
time.sleep(5)

# prompt btn

proBtn = browser.find_element(By.XPATH, value="//button[normalize-space()='Click for JS Prompt']")
proBtn.click()

proAlert = browser.switch_to.alert
proAlert_txt = proAlert.text
print(proAlert_txt)

time.sleep(5)
proAlert.send_keys("Hi, My name is Saurabh Kumar.")
proAlert.accept()






time.sleep(5)
browser.close()
