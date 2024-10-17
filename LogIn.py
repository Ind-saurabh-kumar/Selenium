from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

username = "standard_user"
password = "secret_sauce"


login_url ="https://www.saucedemo.com/v1/"
driver.get(login_url)

username_field = driver.find_element(By.ID, value='user-name')
password_field = driver.find_element(By.ID, value='password')

username_field.send_keys(username)
password_field.send_keys(password)

login_button = driver.find_element(By.ID, value='login-button')

assert not login_button.get_attribute('disable')
login_button.click()

success_element = driver.find_element(By.CLASS_NAME, value='product_label')
print(success_element.text)
assert success_element.text == "Products"


