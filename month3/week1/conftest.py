# conftest.py
import os
from pathlib import Path

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # Reuse a dedicated test profile so Google/Chess.com stay logged in
    profile_dir = os.getenv("CHROME_PROFILE_DIR") or str(
        Path.home() / "Documents/qa-lab/.chrome-profile"
    )
    Path(profile_dir).mkdir(parents=True, exist_ok=True)
    options.add_argument(f"--user-data-dir={profile_dir}")

    # Headless toggle (first run should be headful to complete Google SSO)
    if os.getenv("HEADLESS", "1") == "1":
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    drv.set_window_size(1280, 900)
    yield drv
    drv.quit()
