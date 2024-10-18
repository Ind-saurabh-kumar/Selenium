from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://cosmocode.io/automation-practice-webtable/"
browser = webdriver.Firefox()
browser.maximize_window()

browser.get(url)

browser.execute_script("window.scrollTo(0, 700)")

table = browser.find_element(By.ID, value='countries')
rows = table.find_elements(By.TAG_NAME, value='tr')
row_count = len(rows)
print(row_count)

target_value = "India"
found = False

for row in rows:
    cells = row.find_elements(By.TAG_NAME, value='td')
    for cell in cells:
        if target_value in cell.text:
            print(f"The country is found..")
            found = True
            break

    if found:
        break
if not found:
    print(f"Target Value {target_value} not found")




browser.close()





