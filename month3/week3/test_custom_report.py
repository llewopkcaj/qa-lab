import base64
import os

from pytest_html import extras


def test_custom_report_attachment(extra):
    extra.append(extras.text("Custom note from test", name="Note"))

    screenshot = "month3/week3/screenshots/day3/04_result_page.png"
    if os.path.exists(screenshot):
        with open(screenshot, "rb") as img_file:
            encoded_screenshot = base64.b64encode(img_file.read()).decode("ascii")
        extra.append(extras.image(encoded_screenshot, name="Example Screenshot"))

    assert True
