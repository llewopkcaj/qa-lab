from datetime import datetime

import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

try:
    from pytest_metadata.plugin import metadata_key
except Exception:  # pytest-metadata not installed or legacy version
    metadata_key = None


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

    drv.quit()


# --- Add metadata to pytest-html reports ---
def pytest_configure(config):
    if metadata_key is not None:
        metadata = config.stash.get(metadata_key, {})
        config.stash[metadata_key] = metadata
    else:
        metadata = getattr(config, "_metadata", None)
        if metadata is None:
            metadata = {}
            config._metadata = metadata

    metadata.update(
        {
            "Author": "Jack Powell",
            "Module": "Month 3 — Week 3",
            "Focus": "Screenshots + CI/CD",
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )


# --- Add custom text + image attachments ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Only modify reports for actual test phases
    if rep.when != "call":
        return

    # pytest-html plugin hook
    extra = getattr(rep, "extra", [])

    should_capture = rep.failed or rep.outcome == "xfailed"
    if should_capture:
        extra.append(
            extras.text(
                "Test failed — review screenshot below.",
                name="Failure Message",
            )
        )
        # Screenshot if driver present
        driver = item.funcargs.get("driver", None)
        if driver:
            encoded = driver.get_screenshot_as_base64()
            extra.append(extras.image(encoded, name="Failure Screenshot"))

    rep.extra = extra
