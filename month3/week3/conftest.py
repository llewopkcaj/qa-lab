import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")

    drv = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    yield drv

    # --- screenshot on failure ---
    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        os.makedirs("month3/week3/screenshots", exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"month3/week3/screenshots/FAIL_{ts}.png"
        drv.save_screenshot(path)

        # Will show up in pytest-html as an extra text section
        if hasattr(request.node, "add_report_section"):
            request.node.add_report_section("call", "screenshot", f"Saved screenshot: {path}")

    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Standard pytest pattern:
    - Get the TestReport via hookwrapper
    - Attach it to item as rep_setup/rep_call/rep_teardown
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
