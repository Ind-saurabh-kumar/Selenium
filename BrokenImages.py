import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url="https://the-internet.herokuapp.com/broken_images"
driver = webdriver.Firefox()
driver.maximize_window()

driver.get(url)

images = driver.find_elements(By.TAG_NAME, value='img')

broken_img = []

for img in images:
    src = img.get_attribute('src')
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_img.append(src)
            print(f"Broken Images found")

if broken_img:
    print("list of broken images:")
    for broken_image in broken_img:
        print(broken_image)
else:
    print("No broken images")




time.sleep(5)
driver.close()