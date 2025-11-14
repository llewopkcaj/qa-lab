# Week 2 — Selenium Actions & Waits (Overview)

This week focused on making browser automation feel reliable, human-like, and production-ready.  
I learned how to control pages through clicks, typing, navigation, waiting for conditions, and handling unstable elements.

---

## What I Learned
- How to use `click()`, `send_keys()`, and form submissions.
- The difference between implicit, explicit, and forced waits.
- How to synchronize tests using `WebDriverWait` + `expected_conditions`.
- How to use ActionChains for hover and multi-step interactions.
- How to build retry logic (`resilient_click`) for flaky elements.
- How to automate a complete form: fill → submit → verify.
- How to capture screenshots and generate HTML reports.

---

## Completed Scripts
- `actions_demo.py` — basic click + type automation.  
- `waits_demo.py` — explicit waits vs sleep.  
- `action_chains_demo.py` — hover, double-click, keyboard actions.  
- `form_filler.py` — full form automation + screenshot.  
- `resilient_click.py` — retry-based click helper.  
- `test_form_flow.py` — verifies form submission.  
- `test_resilient_click.py` — verifies retry click works.  
- Reports saved in `month3/week2/reports/`.

---

## Key Skill Gains
- Synchronizing automation with dynamic content.
- Handling flaky UI elements safely.
- Designing repeatable, stable automated flows.
- Combining Selenium + PyTest into a real test suite.

---

## End of Week Status
All Week 2 scripts, tests, and reports are complete.  
Next step: **Week 3 — Screenshots + CI Integration**.
