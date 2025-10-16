# Week 3 CLI Testing — Coverage Matrix

This matrix maps each testing concept to the exact file(s) in the unified suite.

## Summary
- **Files:** 4
- **Dimensions covered:** Functional, Negative/Error handling, UX/Output, Behavioral Flow (incl. input validation), Reliability/Import Safety, Integration (full run).
- **Status:** All passing locally.

---

## Concept ↔ Test Mapping

| Concept Area | File | Key Assertions / Checks | Outcome |
|---|---|---|---|
| **Core Function Validation** | `test_calculate_core.py` | Correct results for add/sub/mul/div/pow/sqrt; domain validation (divide by zero, sqrt of negative); invalid op raises | yes |
| **UX / Output Consistency** | `test_cli_output_format.py` | Numeric outputs fixed to 2 decimals; explicit “Result:” lines present; all error messages start with `Error:` | yes |
| **Behavioral Flow (End-to-End)** | `test_cli_behaviour.py` | Multi-step session (e.g., `add → multiply → q`); prompts and results appear in order; clean quit message | yes |
| **Input Validation (within Behavior)** | `test_cli_behaviour.py` | Invalid/empty inputs produce friendly `Error:` messages; **no** traceback; loop continues until `q` | yes |
| **Import Safety / Mocking** | `test_safe_import.py` | `input()` patched to return `q` on import; module loads without hanging; (optional) patched deps behave predictably | yes |
| **Integration (Unified Run)** | *(entire folder)* | Suite passes as a whole with `pytest -v month2/week3_full_suite` | yes |

---

## How to Run

```bash
pytest -v month2/week3_full_suite
# or quiet mode
pytest -q month2/week3_full_suite --disable-warnings
