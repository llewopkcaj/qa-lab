# WEEK3.md — Month 3 Week 3 Summary

## Overview
Month 3 Week 3 focused on screenshots, pytest-html reporting, and full CI/CD integration with headless Chrome.  
The goal was to build evidence-based UI automation: tests that produce visual artifacts and run reliably both locally and in GitHub Actions.

---

## Key Scripts Completed
### Selenium & Screenshot Automation
- test_screenshot_flow.py — end-to-end Selenium flow test with multiple screenshots.
- take_screenshot.py — utility script for simple screenshot capture.
- conftest.py — includes:
  - WebDriver fixture (headless Chrome)
  - Automatic screenshot-on-failure hook
  - pytest-html metadata injection

### Additional Tests
- test_custom_report.py — demonstrates custom metadata and embedded artifacts.
- test_fail_demo.py — intentional failure test to validate screenshot handling.

### Notes
- DAY6_NOTES.md — CI artifact verification notes.
- NOTES_CI_DAY4.md — early workflow debugging notes.

---

## Screenshot Assets
All screenshots live under:

month3/week3/screenshots/

### Flow screenshots (Day 3)
- day3/01_before_clear.png  
- day3/02_after_clear.png  
- day3/03_filled_new_name.png  
- day3/04_result_page.png  

These represent the full flow from initial state → cleared form → newly filled form → results page.

### Other screenshots
- test_force_fail_20251115_183803.png — produced by failure test.
- day1_chart.png — early sample screenshot.

These confirm that screenshot logic works at multiple points in the flow.

---

## HTML Reports Generated
Located in:

month3/week3/reports/

- week3_final_report.html — the official Day 7 final run.
- report_week3_flow.html — main flow report (with screenshots embedded).
- day4_selenium_report-2.html — GitHub Actions artifact.
- day6_selenium_report-3.html — CI verification artifact.
- report_fail_demo.html — contains expected failure with screenshot.
- test_custom_report.html — metadata + custom attachment demonstration.


---

## CI/CD Integration Summary
GitHub Actions workflow successfully:
1. Installed Python, Chrome, and ChromeDriver  
2. Ran Selenium tests in headless mode  
3. Generated pytest-html reports  
4. Uploaded screenshot + report artifacts  

Documented in:
- NOTES_CI_DAY4.md  
- DAY6_NOTES.md  

### Issues solved:
- Matching Chrome + chromedriver versions  
- Correct screenshot path initialization  
- Fixing artifact upload paths  
- Adjusting headless Chrome flags (`--headless=new`)  


---

## What Worked Well
- Headless Selenium ran consistently in GitHub Actions  
- pytest-html generated clean, readable reports  
- Screenshot-on-failure was reliable  
- Custom metadata enhanced debugging info  
- Tests stabilized after selector/wait adjustments  

---

## What Required Debugging
- Missing screenshots in early CI runs due to bad directory init  
- Incorrect artifact paths in initial selenium.yml  
- A Chrome headless flag mismatch caused failures  
- Some screenshot attachments needed path corrections  


---

## Lessons Learned
- Screenshots turn failures into actionable insights  
- CI/CD validates that tests work in clean environments  
- pytest-html is essential for professional QA communication  
- Headless runs surface timing issues  
- Stable automation relies on well-designed fixtures and environment setup  

---

## Final Deliverables for Week 3
- Selenium screenshot flow test (test_screenshot_flow.py)  
- Automatic screenshot-on-failure in conftest.py  
- take_screenshot.py utility  
- Full HTML report set in month3/week3/reports/  
- Screenshot assets saved and verified  
- GitHub Actions CI pipeline operational  
- WEEK3.md (this document)  
- Final run output (week3_final_report.html)


