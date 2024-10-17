from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://selenium.dev/")

browser.maximize_window()

title = browser.title
print(title)

assert "Selenium123" in title