import pytest
from form_filler import first_name, last_name, open_page, submit_button


@pytest.mark.external
def test_submission(driver):
    open_page(driver)
    first_name(driver)
    last_name(driver)
    url, text = submit_button(driver)
    assert "Jack" in text and "Powell" in text
    assert "action_page" in url
    assert driver.save_screenshot("form_result.png")
