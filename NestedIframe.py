
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()

url = "https://the-internet.herokuapp.com/nested_frames"
driver.get(url)

driver.switch_to.frame("frame-top")
# switching to middle frame
driver.switch_to.frame("frame-middle")

content = driver.find_element(By.ID, value="content").text
print("Content in middle frame", content)

# switch to Default content
driver.switch_to.default_content()
# switch to bottom frame
driver.switch_to.frame("frame-bottom")

content_bottom = driver.find_element(By.TAG_NAME, value="body").text
print("Content in bottom frame ", content_bottom)









driver.close()