import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By



url = "https://jqueryui.com/"

driver = webdriver.Firefox()
driver.maximize_window()

driver.get(url)

all_links = driver.find_elements(By.TAG_NAME, value='a')

print(f"Total number of links present in the website : {len(all_links)}")


for link in all_links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"Broken link: {href} (Status Code :{response.status_code})")



time.sleep(5)

driver.quit()
