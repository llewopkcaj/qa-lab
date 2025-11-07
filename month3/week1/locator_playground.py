from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://example.com")

header = driver.find_element(By.TAG_NAME, "h1")
print("Header text:", header.text)

paragraph = driver.find_element(By.CSS_SELECTOR, "p")
print("Paragraph:", paragraph.text)

link = driver.find_element(By.XPATH, "//a")
print("Link URL:", link.get_attribute("href"))

driver.quit()
