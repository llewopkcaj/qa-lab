import pytest


@pytest.mark.xfail(reason="Intentional failure demo for Selenium CI", strict=False)
def test_force_fail(driver):
    driver.get("https://example.com")

    assert False  # noqa: B011


# pytest month3/week3/test_fail_demo.py -v --html=month3/week3/report_fail_demo.html --self-contained-html
