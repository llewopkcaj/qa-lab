from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def open_page(driver):
    driver.get("https://www.w3schools.com/html/html_forms.asp")


def first_name(driver):
    first = driver.find_element(By.ID, "fname")
    first.clear()
    first.send_keys("Jack")


def last_name(driver):
    last = driver.find_element(By.ID, "lname")
    last.clear()
    last.send_keys("Powell")


def submit_button(driver):
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[-1])
    form = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.w3-container.w3-large.w3-border"))
    )
    return driver.current_url, form.text
