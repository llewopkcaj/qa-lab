from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def make_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    drv.set_window_size(1280, 900)
    return drv


driver = make_driver()
driver.get("https://www.w3schools.com/html/html_forms.asp")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "fname")))


driver.find_element(By.XPATH, '//*[@id="fname"]').send_keys("Jack")
driver.find_element(By.XPATH, '//*[@id="lname"]').send_keys("Powell")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[-1])

print("URL:", driver.current_url)
print("Title:", driver.title)

driver.quit()
