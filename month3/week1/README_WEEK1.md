# 🌐 Month 3 – Week 1 : Selenium Setup + Locators

**Theme:** Web automation foundations — controlling browsers programmatically and learning how to locate elements precisely.  
**Goal:** Launch a browser, identify elements through multiple strategies, and validate them with PyTest.

---

## 📚 Study Materials
| Topic | Resource |
|:------|:----------|
| Selenium Getting Started | [docs.selenium.dev/webdriver/getting_started](https://www.selenium.dev/documentation/webdriver/getting_started/) |
| Locating Elements | [docs.selenium.dev/webdriver/elements/finders](https://www.selenium.dev/documentation/webdriver/elements/finders/) |
| HTML Basics | [W3Schools – HTML Intro](https://www.w3schools.com/html/html_intro.asp) |
| HTML Attributes | [W3Schools – HTML Attributes](https://www.w3schools.com/html/html_attributes.asp) |
| Real Python – Locators | [Modern Web Automation with Selenium](https://realpython.com/modern-web-automation-with-python-and-selenium/) |
| PyTest + Selenium | [Real Python – Testing with Selenium and PyTest](https://realpython.com/pytest-python-testing/#automated-ui-tests) |

---

## 🧩 Scripts & Outputs

| File | Purpose | Output / Notes |
|:-----|:---------|:---------------|
| **selenium_basics.py** | Opens a webpage and prints its title | Screenshot → `screenshots/first_run.png` |
| **locator_playground.py** | Demonstrates 3+ locator strategies (ID, Class, CSS, XPath) | Reference table in `LOCATORS.md` |
| **multi_locator_demo.py** | Collects all `<a>` links and exports to CSV | `page_links.csv` |
| **element_audit.py** | Counts buttons, links, and images on a page | `audit_summary.json` |
| **test_selenium_asserts.py** | 🔒 Full login + username verification suite for Chess.com | Uses `CHESS_USER` / `CHESS_PASS` env vars; asserts login success and visible username |
| **test_locators_headless.py** | Confirms headless execution works in CI/CD | `screenshot_headless.png` |

---

## 🧪 Test Reporting
```bash
pytest -v --html=reports/week1_final_report.html --self-contained-html
