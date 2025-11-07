from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

folder = Path("month3/week1/screenshots")
folder.mkdir(parents=True, exist_ok=True)


def test_example_link(driver):
    driver.get("https://anyoneworldwide.com")
    title = driver.title
    meta = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'meta[name="description"]'))
    )
    content = meta.get_attribute("content")
    assert "Anyone" in title
    assert content is not None and "Made in USA" in content

    driver.save_screenshot(folder / "headless.png")
