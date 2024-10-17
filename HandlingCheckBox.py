import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.maximize_window()

url="https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
browser.get(url)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# checkBx1 = browser.find_element(By.XPATH, value='//label[normalize-space()="Sunday"]')
# time.sleep(3)
# checkBx1.click()
# time.sleep(3)
# checkBx1.click()
# time.sleep(3)


checkboxes = browser.find_elements(By.XPATH, value='//input[@type="checkbox"]')
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)
time.sleep(3)

checked_count=0
for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count+=1

expected_checked_count=7
if checked_count == expected_checked_count:
    print('Checkbox count verified')
else:
    print('Checkbox count missmatch')

time.sleep(3)



browser.close()





