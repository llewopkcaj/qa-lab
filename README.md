# qa-month1

This repository tracks my Python learning and automation projects as part of a 6–7 month **QA Automation roadmap**.  
It now contains completed work from **Weeks 1–5** (Python + Pandas) and **Month 2, Week 1** (PyTest foundations).

---

## Week 1 — Python Foundations (Variables, Lists, Dicts)
- **profile_card.py** — variables + f-strings.  
- **favorites.py** — list indexing, slicing, and updates.  
- **contact_book.py** — nested dictionaries and safe access.  
- **daily_dashboard.py** — combined project with variables, lists, dicts.  
- **poetry_generator.py** — ASCII poetry with random choice.  

---

## Week 2 — Loops, Functions, Exceptions
- **grade_classifier.py** — classify grades with if/elif/else.  
- **truth_table.py** — boolean logic outputs.  
- **loop_katas.py** — loop practice problems.  
- **math_utils.py** — add, mean, describe_person.  
- **scope_demo.py** — local vs global scope.  
- **safe_divide.py** — division with validation & errors.  
- **file_reader.py** — safe file handling.  
- **cli_calculator.py** — interactive calculator with exceptions + docstrings.  

---

## Week 3 — File Handling (Text, CSV, JSON)
- **file_basics.py** — open, write, append, and read text files.  
- **csv_contacts.py** — create and read CSV with `csv.DictWriter` and `DictReader`.  
- **json_profile.py** — save, reload, and update JSON profiles.  
- **file_renamer.py** — batch rename files in a folder.  
- **json_to_csv.py** — convert JSON → CSV with graceful key handling.  
- **week3_exercises/** — practice sets and optional challenges (Mockaroo/Faker).  

---

## Week 4 — CSV + JSON Automation
- **csv_missing.py** — handle inconsistent CSVs with `.get()`.  
- **json_pretty.py** — pretty-print vs minify JSON, compare file sizes.  
- **json_to_csv.py** — structured JSON → tabular CSV.  
- **csv_to_json.py** — CSV → JSON conversion with formatting.  
- **analyze_dataset.py** — analyze a large fake dataset (emails, ages).  
- **robust_loader.py** — load CSV/JSON with error handling.  
- **WEEK4.md** — documentation with notes and code snippets.  

---

## Week 5 — Pandas & Data Analysis
- **pandas_intro.py** — Series & DataFrame basics (`.head()`, `.shape`, `.dtypes`).  
- **pandas_io.py** — read CSV/JSON, write to copy files.  
- **pandas_filter.py** — filter rows (Age > 30), select specific columns, use `.iloc` / `.loc`.  
- **pandas_clean.py** — handle missing values (`.isnull().sum()`, `.fillna()`, `.dropna()`).  
- **pandas_analyze.py** — analyze dataset: count Gmail users, group by Country, average Age → export summary.csv.  
- **qa.dataset.explorer.py** — mini QA dataset explorer (shape, null counts, top values) → export report.json.  
- **contacts.json / contacts.copy.csv / MOCK_DATA-3.csv** — supporting datasets.  
- **week5.md** — notes, quiz reflection, and 3 code snippets.  

✅ **Outcome:** Pandas enables faster, cleaner handling of CSV/JSON compared to raw file ops, shifting the workflow toward *data analysis as QA*.  

---

## Month 2 — Week 1: PyTest Foundations
- **test_smoke_basics.py** — math, string, and list assertions.  
- **test_math_utils.py** — tests for add, mean, and describe_person.  
- **test_grade_classifier.py** — full grade range + out-of-range errors.  
- **test_truth_table.py** — boolean logic tests.  
- **test_loop_katas.py** — loops, enumerate, multiples of 7.  
- **test_file_basics.py** — temporary file I/O testing.  
- **test_csv_json_minis.py** — JSON and CSV mini-scripts.  
- **test_json_to_csv.py** — JSON→CSV converter with error handling.  
- **test_safe_divide_and_file_reader.py** — exception handling tests.  
- **pytest.ini** — global PyTest config (`-q`, `--maxfail=1`, hide warnings).  
- **README_tests.md** — documentation for running tests.  

✅ **Outcome:** By the end of this week, a complete PyTest suite (20+ passing tests) covers all core Python scripts from Weeks 1–3, building the foundation for fixtures, parametrization, and setup/teardown in Week 2.
