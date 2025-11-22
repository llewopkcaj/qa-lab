import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

os.makedirs("month3/week3/screenshots", exist_ok=True)


def make_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    drv.set_window_size(1280, 900)
    return drv


driver = make_driver()

driver.get("https://www.cnbc.com/quotes/.SPX")
screenshot_path = "month3/week3/screenshots/day1_chart.png"

try:
    chart = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.stx-holder.stx-panel-chart"))
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", chart)

    time.sleep(5)

except Exception as e:
    print("Warning: chart container never became visible:", e)

driver.save_screenshot(screenshot_path)
driver.quit()
