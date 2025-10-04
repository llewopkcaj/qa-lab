# QA-Month1 — PyTest Test Suite (Week 1, Month 2)

This folder contains the PyTest test suite for all Python scripts completed in Month 1 of the curriculum.  
During **Month 2, Week 1** we learned the foundations of PyTest: assertions, discovery, error handling, and configuration.  
By the end of this week, we have **20+ passing tests** across multiple scripts.

---

## 🔹 How to Run Tests

From the project root (`qa-month1/`):

```bash
pytest
```

PyTest will automatically pick up configuration from `pytest.ini` and run all tests in **week6/** by default.

Useful options:

- `pytest -v` → verbose output (show each test name)  
- `pytest -q` → quiet mode (default via `pytest.ini`)  
- `pytest --maxfail=1` → stop after the first failure (default via `pytest.ini`)  
- `pytest -k "json"` → run only tests with `"json"` in the name  
- `pytest -m "markername"` → run only tests marked with a specific marker  

---

## 🔹 What’s Covered

### Week 1–3 Scripts
- Variables, strings, lists, dicts  
- File handling (open/read/write)  
- CSV + JSON converters  

### Week 6 (Test Practice)
- `test_smoke_basics.py` — math/string/list assertions  
- `test_math_utils.py` — add, mean, describe_person  
- `test_grade_classifier.py` — grade logic with range & error cases  
- `test_truth_table.py` — boolean expressions  
- `test_loop_katas.py` — loops, enumerate, multiples of 7  
- `test_file_basics.py` — temporary file I/O tests  
- `test_csv_json_minis.py` — JSON and CSV mini-scripts  
- `test_json_to_csv.py` — JSON→CSV converter, error handling  
- `test_safe_divide_and_file_reader.py` — exception handling tests  

---

## 🔹 Notes

- **Config:**  
  `pytest.ini` sets default options:  
  ```ini
  [pytest]
  addopts = -q --maxfail=1 --disable-warnings
  testpaths = week6
  ```

- **Test Count:** Currently 20+ tests, all passing.  
- **Style:** Tests consistently use `pytest.raises` for errors and plain `assert` for checks.  

---

## ✅ Outcome

By the end of Week 1 (Month 2), we have:
- A working PyTest suite with 20+ passing tests  
- Central configuration (`pytest.ini`)  
- Clear test coverage across all major Python basics from Month 1  
- Ready to expand into fixtures, parametrization, and setup/teardown in Week 2
