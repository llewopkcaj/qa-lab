import json

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


class ActionLogger:
    def __init__(self, driver):
        self.driver = driver
        self.actions = {
            "clicks": 0,
            "moves": 0,
            "navigations": 0,
            "events": [],
        }

    def nav(self, url):
        self.driver.get(url)
        self.actions["navigations"] += 1
        self.actions["events"].append({"type": "nav", "url": url})

    def click(self, locator):
        wait = WebDriverWait(self.driver, 10)
        el = wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).double_click(el).perform()
        self.actions["clicks"] += 2
        self.actions["events"].append({"type": "click"})

    def move_to(self, locator):
        wait = WebDriverWait(self.driver, 10)
        el = wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(el).perform()
        self.actions["moves"] += 1
        self.actions["events"].append(
            {
                "type": "moves",
            }
        )


logger = ActionLogger(driver)
logger.nav("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_ondblclick")
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframeResult")))
logger.click((By.TAG_NAME, "p"))
driver.switch_to.default_content()
logger.nav("https://demoqa.com/tool-tips")
logger.move_to((By.ID, "toolTipButton"))
print(logger.actions)

with open("audit_actions.json", "w") as f:
    json.dump(logger.actions, f, indent=4)

driver.quit()
