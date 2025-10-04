# Week 2 — PyTest Fixtures & Structure (Summary)

**Goal:** Build a professional, modular test suite using fixtures, parametrization, and setup/teardown.
 
**Environment**
- Python: 3.13.5  
- pytest: 8.4.2  
- Folder: `month2/week2/`  
- Result: **All tests passing (42/42)**

---

## Folder Structure
```
week2/
├── calculator.py
├── conftest.py
├── test_calculator_suite.py
├── test_math_ops.py
├── test_tempfile_ops.py
├── test_with_fixture.py
├── test_scoped.py
└── pytest.ini
```

---

## Fixtures Overview (`conftest.py`)

| Fixture Name | Scope | Purpose |
|---------------|--------|----------|
| `sample_data` | function | Provides a small dictionary for data-based tests. |
| `first_connection` | session | Demonstrates one-time setup/teardown using `yield`. |
| `run_calc` | function | Returns a fresh `Calculator` instance for arithmetic tests. |
| `func_resource` | function | Logs setup/teardown at function level for scope demo. |
| `module_resource` | module | Logs setup/teardown once per module. |
| `class_resource` | class | Logs setup/teardown once per test class. |
| `file_yield` | function | Creates a temporary file (`purple.txt`), deletes it afterward. |
| `file_finalizer` | function | Creates a temporary file (`yellow.txt`), cleans up via `addfinalizer`. |

**Key Patterns**
- Used both `yield` and `request.addfinalizer()` for teardown demonstrations.  
- Combined multiple fixture scopes to show lifetime differences.  
- Fixtures are automatically discovered by all test files (no import statements needed).

---

## Parametrization & Error Handdling Examples

**Arithmetic Tests**
```python
@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 5),
    (9, -1, 8)
])
def test_add(run_calc, a, b, expected):
    assert run_calc.add_(a, b) == expected
```

**Error Handling**
```python
def test_failure(run_calc):
    with pytest.raises(ZeroDivisionError):
        run_calc.div_(5, 0)
```

**Type Validation**
```python
@pytest.mark.parametrize("a, b", [
    (5, []),
    ("elo", 7),
    (None, 8)
])
def test_input(run_calc, a, b):
    with pytest.raises(TypeError):
        run_calc.add_(a, b)
```

---

## Setup/Teardown Flow (Scope Diagram)

```
pytest session start
└─ first_connection (session) setup
   ├─ module_resource (per module)
   │   ├─ class_resource (per class)
   │   │   ├─ func_resource (per test)
   │   │   ├─ run_calc (per test)
   │   │   ├─ file_yield (per test)
   │   │   └─ file_finalizer (per test)
   │   └─ class_resource teardown
   └─ module_resource teardown
└─ first_connection teardown
pytest session end
```

---

## Commands

**Run suite quietly**
```bash
pytest -q
```

**Verbose (show test names)**
```bash
pytest -v
```

**Collect test discovery only**
```bash
pytest --collect-only
```

---

## Quality Checklist

- [x] Centralized fixtures in `conftest.py`
- [x] Multiple fixture scopes demonstrated (`function`, `module`, `class`, `session`)
- [x] File fixtures properly teardown temporary files
- [x] Both `yield` and `request.addfinalizer` patterns used
- [x] Parametrization includes valid and error paths
- [x] All tests isolated and reproducible

---

## Notes / Next Steps

- Structure now mirrors real-world QA frameworks (shared fixtures + modular test files).  
- You’re ready for **Month 2 / Week 3 — AI-Assisted Test Writing**, which builds on this foundation.

---

## Commit

```bash
git add WEEK2_TESTS.md conftest.py calculator.py
git commit -m "Week2 Day7: finalized multi-scope fixtures and summary documentation"
git push
```
