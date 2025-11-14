from selenium import webdriver
from selenium.webdriver import ActionChains
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

wait = WebDriverWait(driver, 10)

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_ondblclick")

wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframeResult")))

element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p")))
ActionChains(driver).double_click(element).perform()
result = wait.until(EC.visibility_of_element_located((By.ID, "demo"))).text
print(result)

driver.switch_to.default_content()
driver.get("https://demoqa.com/tool-tips")
button = wait.until(EC.visibility_of_element_located((By.ID, "toolTipButton")))
ActionChains(driver).move_to_element(button).perform()

revealed = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.tooltip-inner")))
print(revealed.text)
