import platform
import sys


def pytest_configure(config):
    config._metadata = {
        "Author": "Jack Powell",
        "Project": "QA Lab – PyTest Reporting",
        "Python Version": sys.version.split()[0],
        "Operating System": platform.system(),
        "OS Version": platform.release(),
        "Test Scope": "Month 2 – Week 4 – Day 2 Metadata Customization",
    }
