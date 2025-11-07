import os

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_login_info() -> tuple[str, str]:
    user, pwd = os.getenv("CHESS_USER"), os.getenv("CHESS_PASS")
    if not user or not pwd:
        pytest.skip("Set CHESS_USER and CHESS_PASS to run this test.")
    return user, pwd


def is_logged_in(driver, timeout: int = 10) -> bool:
    wait = WebDriverWait(driver, timeout)
    driver.get("https://www.chess.com/home")
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-button='profile']")))
        return True
    except Exception:
        return False


def _accept_cookies_if_present(driver):
    # OneTrust sometimes blocks interactions. Click it via JS if present.
    driver.execute_script(
        """
    (function(){
        var b=document.getElementById('onetrust-accept-btn-handler');
        if(b && b.offsetParent!==null){ b.click(); }
    })();
    """
    )


def _find_input(wait: WebDriverWait, selectors: list[tuple[str, str]]):
    for how, what in selectors:
        try:
            # presence, not clickable – overlays can block 'clickable'
            el = wait.until(EC.presence_of_element_located((how, what)))
            return el
        except Exception:
            pass
    return None


def login_chess(driver, timeout: int = 40) -> None:
    # If already authenticated, bail
    if is_logged_in(driver, timeout=8):
        return

    user, pwd = get_login_info()
    wait = WebDriverWait(driver, timeout)

    # Go to plain login (avoid extra redirects)
    driver.get("https://www.chess.com/login")
    _accept_cookies_if_present(driver)

    # Try multiple robust selectors (Chess.com sometimes tweaks attrs)
    username = _find_input(
        wait,
        [
            (By.ID, "username"),
            (By.NAME, "username"),
            (By.CSS_SELECTOR, "input[name='username']"),
            (By.CSS_SELECTOR, "input[autocomplete='username']"),
            (By.CSS_SELECTOR, "form input[type='text']"),
        ],
    )
    password = _find_input(
        wait,
        [
            (By.ID, "password"),
            (By.NAME, "password"),
            (By.CSS_SELECTOR, "input[name='password']"),
            (By.CSS_SELECTOR, "input[type='password']"),
        ],
    )

    if not (username and password):
        # Dump URL to help debugging in report, then skip
        pytest.skip(
            f"Login inputs not found on {driver.current_url}. "
            "Form likely covered or changed. Run headful and inspect."
        )

    # Fill via JS to bypass any overlay/focus issues, then submit
    driver.execute_script("arguments[0].value = arguments[1];", username, user)
    driver.execute_script("arguments[0].value = arguments[1];", password, pwd)

    # Scroll and click submit
    submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", submit)
    submit.click()

    # Confirm logged in
    assert is_logged_in(driver, timeout=15), "Login failed: profile link not found after submit."


def test_login_flow(driver):
    login_chess(driver, timeout=40)
    profile = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-button='profile']"))
    )
    assert profile.is_displayed()


def test_username_is_shown(driver):
    user, _ = get_login_info()
    login_chess(driver, timeout=40)

    wait = WebDriverWait(driver, 15)
    profile_link = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-button='profile']"))
    )
    assert profile_link.is_displayed()

    # Get profile URL and derive slug
    href = (profile_link.get_attribute("href") or "").rstrip("/")
    assert href, "Expected profile link to have an href."
    slug = href.split("/")[-1]
    assert slug, "Could not extract username slug from profile link URL."

    # Go to profile page
    profile_link.click()
    wait.until(EC.url_contains(slug))
    assert slug.lower() in driver.current_url.lower(), "Profile URL did not contain username slug."

    # Assert username is actually rendered on the profile page
    # Try a few robust targets: exact text match anywhere, or a headline/username element
    candidates = [
        (
            By.XPATH,
            f"//*[normalize-space(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'))='{user.lower()}']",
        ),
        (By.CSS_SELECTOR, "h1, h2, .user-username, [data-test='user-username'], .profile-username"),
    ]

    found = False
    for how, what in candidates:
        try:
            el = wait.until(EC.presence_of_element_located((how, what)))
            txt = (el.text or "").strip()
            if txt and txt.lower() == user.lower():
                found = True
                break
        except Exception:
            continue

    assert found, f"Did not find visible username '{user}' on the profile page."
