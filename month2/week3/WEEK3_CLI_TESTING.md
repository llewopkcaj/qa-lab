# WEEK 3 — CLI Testing + Code Hygiene Integration  
**QA Lab · Month 2 · Week 3**

---

## 🧩 Overview  
This week bridged functional testing and engineering hygiene — moving from isolated function tests to full **CLI interaction coverage** and clean **continuous-integration-ready code**.  
I practiced *core/interface separation*, *user simulation*, and *style enforcement* (Ruff + Black + Mypy + Pre-Commit + CI).  
The goal was to end the week with a portfolio-ready, fully linted and formatted test suite.

---

## 🧪 Concept Coverage

| Concept Group | Description | Key Files |
|----------------|-------------|-----------|
| **Core Logic** | Parametrized tests verifying pure computational layer (`calculate`) and domain validation (divide by zero, sqrt of negative). | `test_calculate_core.py` |
| **CLI Input Validation** | Simulated invalid and missing inputs using `monkeypatch` + `capsys`; asserted friendly “Error:” messages and graceful loop continuation. | `test_cli_input_validation.py` |
| **Output & UX Formatting** | Captured stdout and enforced numeric precision (2 decimals) and consistent “Result:” / “Error:” conventions. | `test_cli_output_format.py` |
| **Behavioral Flow** | Full session simulation (`[add, 3, 5, multiply, 2, 4, q]`), confirming loop continuity and clean exit message. | `test_cli_behavioral_flow.py` |
| **Safe Import & Mocking** | Ensured importing `cli_calculator` never hangs; mocked `input()` → `q` to auto-quit on load. | `test_safe_import.py` |
| **Full Suite Integration** | Unified tests in `week3_full_suite/`; added `coverage_matrix.md` mapping 18 concepts → test files. | `coverage_matrix.md` |
| **AI Collaboration Logs** | Tracked prompts vs manual edits; documented where AI improved speed or produced context errors. | `notes_ai_testing.md`, `prompt_log.md` |

---

## 🧱 Hygiene Mini-Curriculum (Inserted Mid-Week)

| Day | Focus | Key File / Outcome |
|-----|--------|--------------------|
| **Day 1 – Ruff + Black Baseline** | Created `pyproject.toml`; cleaned repo with `ruff check . --fix` + `black .` | `pyproject.toml` |
| **Day 2 – Editor Integration + Rule Triage** | Added `.vscode/settings.json`; auto-format & lint on save; chose rules to silence locally with `# noqa:` | `.vscode/settings.json` |
| **Day 3 – Pre-Commit Hooks + UX Contract Test** | Installed `.pre-commit-config.yaml`; added strict UX-contract test verifying consistent CLI output. | `.pre-commit-config.yaml`, test in `week3_full_suite/test_ux_contract.py` |
| **Day 4 – CI Guardrail + Intro Typing** | Added GitHub Actions workflow to enforce lint/format/type; typed `calculate` and `run_it`; validated with `mypy .` | `.github/workflows/ci.yml` |

---

## 🧠 Insights & Reflections

- **Core vs Interface:** Splitting `calculate` from `run_it()` made testing cleaner; pure logic can be covered parametrically, while the CLI layer handles recovery and UX.  
- **Monkeypatch + Capsys:** Felt like simulating an actual user — a controlled dialogue between test and program.  
- **UX Contracts:** Locking output format enforced professionalism and reliability; small formatting details matter in QA output consistency.  
- **AI Assistance:** Useful for boilerplate and syntax hints, but mis-guessed fixture names and paths; documenting these mismatches clarified test scope.  
- **Hygiene Stack:** Ruff/Black/Mypy/Pre-Commit formed a self-correcting environment. My codebase now fails fast on style or typing violations before CI.  

---

## 🧰 Commands Snapshot

```bash
# Run full suite quietly
pytest --maxfail=1 --disable-warnings -q

# Verify hygiene and types
ruff check . --fix && black . && mypy .

# Commit and push
git add .
git commit -m "Add Week 3 CLI testing + hygiene integration (18 concepts)"
git push
```

---

## 🧾 Journal Prompt

> *“Which test made me feel closest to a real user?*  
> The behavioral flow test — it transformed abstract functions into lived experience. Seeing multiple operations and graceful exit happen exactly as intended felt like a user story passing acceptance.”

> *“Where did automation expose hidden assumptions?”*  
> In the UX-contract test: I discovered inconsistent spacing in output strings. Automation caught what eyes glossed over — subtle but user-visible defects.

---

## ✅ Deliverables Summary

- ✅ **All tests passing:** `pytest -q` → 0 failures  
- ✅ **Lint/format/type clean:** Ruff · Black · Mypy  
- ✅ **Pre-commit hooks active**  
- ✅ **CI pipeline green on main**  
- ✅ **WEEK3_CLI_TESTING.md committed**
