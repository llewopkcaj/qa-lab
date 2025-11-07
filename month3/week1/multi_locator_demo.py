import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://wikipedia.org")

links = driver.find_elements(By.TAG_NAME, "a")

print(f"Total links found: {len(links)}")
for link in links:
    text = link.text.strip() or "(no text)"
    href = link.get_attribute("href")
    print(f"{text} -> {href}")

with open("page_links.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "url"])
    for link in links:
        writer.writerow([link.text.strip(), link.get_attribute("href")])
driver.quit()
print("Exported to page_links.csv")
