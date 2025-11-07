import json
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

base_dir = Path.home() / "Documents" / "qa-lab" / "month3" / "week1"
base_dir.mkdir(parents=True, exist_ok=True)
file_path = base_dir / "audit_summary.json"


def web_audit(driver):
    driver.get("https://bandcamp.com")
    links = driver.find_elements(By.TAG_NAME, "a")
    link_count = len(links)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    button_count = len(buttons)
    images = driver.find_elements(By.TAG_NAME, "img")
    image_count = len(images)

    data = {
        "url": "https://bandcamp.com",
        "links": link_count,
        "buttons": button_count,
        "images": image_count,
    }

    with file_path.open("w") as f:
        json.dump(data, f, indent=4, sort_keys=True)

    print(f"Saved audit summary to {file_path}")


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    driver.set_window_size(1280, 900)

    try:
        web_audit(driver)
    finally:
        driver.quit()
