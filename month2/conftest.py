import platform
import sys
from collections.abc import Generator
from typing import Any

import pytest

try:
    from pytest_html import extras
except Exception:
    extras = None


def pytest_configure(config: Any) -> None:
    if not hasattr(config, "_metadata") or config._metadata is None:
        config._metadata = {}
    config._metadata.update(
        {
            "Author": "Jack Powell",
            "Project": "QA Lab – PyTest Reporting",
            "Python Version": sys.version.split()[0],
            "Operating System": platform.system(),
            "OS Version": platform.release(),
            "Test Scope": "Month 2 – Week 4 – Day 2 Metadata Customization",
        }
    )

    marker_expression = getattr(config.option, "markexpr", None)
    if marker_expression:
        config._metadata["Report Type"] = marker_expression.upper()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Any, call: Any) -> Generator[None]:
    outcome = yield
    if outcome is None:
        return
    report = outcome.get_result()
    if report.when != "call":
        return
    if report.failed:
        print(f"[Hook] {item.name} failed")
        if extras is not None:
            extra = getattr(report, "extra", [])
            note = "Failure captured by pytest_runtest_makereport (curriculum demo)."
            extra.append(extras.text(note, name="Failure Note"))
            report.extra = extra
