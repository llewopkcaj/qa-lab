from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://example.com")

print("Page title:", driver.title)

driver.save_screenshot("month3/screenshots/first_run.png")

driver.quit()
