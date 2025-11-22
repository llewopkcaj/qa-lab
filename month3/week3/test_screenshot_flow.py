import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

SCREENSHOT_DIR = "month3/week3/screenshots/day3"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def test_screenshot_flow(driver):
    driver.get("https://www.w3schools.com/html/html_forms.asp")

    wait = WebDriverWait(driver, 10)

    # --- locate fields ---
    fname = wait.until(EC.visibility_of_element_located((By.ID, "fname")))
    lname = wait.until(EC.visibility_of_element_located((By.ID, "lname")))

    # 1) Screenshot BEFORE clear (shows the default 'John' / 'Doe' etc.)
    before_clear_path = f"{SCREENSHOT_DIR}/01_before_clear.png"
    driver.save_screenshot(before_clear_path)

    # --- clear the fields completely ---
    fname.clear()
    lname.clear()

    # 2) Screenshot AFTER clear (empty fields)
    after_clear_path = f"{SCREENSHOT_DIR}/02_after_clear.png"
    driver.save_screenshot(after_clear_path)

    # --- type new values ---
    fname.send_keys("Jack")
    lname.send_keys("Powell")

    # 3) Screenshot with new name filled in
    filled_path = f"{SCREENSHOT_DIR}/03_filled_new_name.png"
    driver.save_screenshot(filled_path)

    # --- submit the form ---
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Wait for new tab to open (W3Schools behavior)
    wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[-1])

    # Wait for result page to load
    wait.until(EC.url_contains("action_page.php"))

    # 4) Screenshot of the result page (shows Jack / Powell)
    result_path = f"{SCREENSHOT_DIR}/04_result_page.png"
    driver.save_screenshot(result_path)

    # Basic sanity checks
    for path in (before_clear_path, after_clear_path, filled_path, result_path):
        assert os.path.exists(path)

    # Optional: confirm our new values made it to the result page
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Jack" in body_text
    assert "Powell" in body_text


"""pytest month3/week3/test_screenshot_flow.py \
  --html=month3/week3/reports/report_week3_flow.html \
  --self-contained-html -q"""
