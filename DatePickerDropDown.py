import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Firefox()
browser.maximize_window()

url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)

datePicker = browser.find_element(By.ID, value='datepicker2')
datePicker.click()

current_date = datetime.now()
currDate = datetime.now().day
currMon = datetime.now().month
print(currMon)
currYear = current_date.year
print(currDate, currMon, currYear)

nextday = datetime.now()-timedelta(days=20)
nextDate = str(nextday.day)
nextMonth = (currMon % 12)-8
nextMonthYear = f"{nextMonth}/{currYear}"
print(f"next month year....{nextMonthYear}")

Month_Dropdown = browser.find_element(By.CSS_SELECTOR, value='select[title="Change the month"]')
select = Select(Month_Dropdown)
select.select_by_value(str(nextMonthYear))

Year_Dropdown = browser.find_element(By.CSS_SELECTOR, value='select[title="Change the year"]')
select = Select(Year_Dropdown)
year_text = "2024"
select.select_by_visible_text(year_text)

browser.find_element(By.LINK_TEXT, nextDate).click()












time.sleep(5)
browser.quit()