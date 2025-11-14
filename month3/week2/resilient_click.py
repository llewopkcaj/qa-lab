from collections.abc import Callable
from time import sleep

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = tuple[str, str]


def resilient_click(
    driver: WebDriver,
    locator: Locator,
    attempts: int = 3,
    post_condition: Callable[[WebDriver], bool] | None = None,
) -> None:
    last_error: Exception | None = None
    for _ in range(1, attempts + 1):
        try:
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))  # type: ignore
            try:
                element.click()
            except ElementClickInterceptedException:
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
                sleep(0.3)
                element.click()
            if post_condition is not None:
                WebDriverWait(driver, 10).until(post_condition)
            return
        except (
            StaleElementReferenceException,
            ElementClickInterceptedException,
            ElementNotInteractableException,
            TimeoutException,
        ) as e:
            last_error = e
            sleep(0.3)
    raise last_error if last_error else RuntimeError
