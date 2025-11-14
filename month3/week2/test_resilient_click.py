import pytest
from resilient_click import resilient_click
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.external
@pytest.mark.actions
def test_resilient_click_navigates_after_submit(driver):
    driver.get("https://www.w3schools.com/html/html_forms.asp")

    driver.find_element(By.ID, "fname").send_keys("Jack")
    driver.find_element(By.ID, "lname").send_keys("Powell")

    submit = (By.CSS_SELECTOR, "input[type='submit']")

    resilient_click(driver, submit, post_condition=EC.number_of_windows_to_be(2))

    driver.switch_to.window(driver.window_handles[-1])

    WebDriverWait(driver, 10).until(EC.url_contains("action_page.php"))
    assert "action_page.php" in driver.current_url
