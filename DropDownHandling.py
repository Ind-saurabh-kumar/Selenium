import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


url='https://the-internet.herokuapp.com/dropdown'

driver = webdriver.Firefox()
driver.maximize_window()

driver.get(url)
time.sleep(4)

dropdown_element = driver.find_element(By.ID, value='dropdown')
select = Select(dropdown_element)

# Select the value by visible text
select.select_by_visible_text("Option 2")
time.sleep(2)

# select the value by Index
select.select_by_index(1)
time.sleep(2)

# select the value by Using a value
select.select_by_value("2")


option_count = len(select.options)
print(f"Total Options are available in dropdown: {option_count}")


target_value = "Option 1"

for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Seleted Option is {target_value}")
        break
    else:
        print(f"Option {target_value} not found")










time.sleep(3)
driver.close()