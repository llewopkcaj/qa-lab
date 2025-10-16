## Manual vs AI: Coverage Matrix

| Area | Manual Tests | AI Tests | Notes |
|---|---|---|---|
| Core/interface separation (test `calculate` directly) | Yes/No | Yes/No | Do you test pure functions apart from CLI? |
| Friendly recovery (graceful errors) | Yes/No | Yes/No | Clear message + continue running |
| CLI user-interaction loop modeled | Yes/No | Yes/No | Multi-prompt sequence tested |
| Dispatch logic (all ops, invalid op) | Yes/No | Yes/No | add, sub, mul, div, power, sqrt, invalid |
| End-to-end integration (scripted session) | Yes/No | Yes/No | Feed inputs; assert final state/output |
| Domain validation (sqrt<0, div by zero) | Yes/No | Yes/No | Correct exception and message |
| CLI input validation (non-numeric, missing) | Yes/No | Yes/No | Error then re-prompt |
| Safe import (monkeypatch input -> 'q') | Yes/No | Yes/No | Import module without hanging |
| Output formatting (two decimals) | Yes/No | Yes/No | Assert formatted string, not just value |
| Human-readable error messages | Yes/No | Yes/No | Message wording asserted |
| Success feedback line present | Yes/No | Yes/No | e.g., "Result: 7.00" |
| Consistent "Error:" prefix | Yes/No | Yes/No | All error lines start with "Error:" |
| Parameterized functional tests | Yes/No | Yes/No | Table-driven inputs/expected |
| Behavioral flow (multiple inputs) | Yes/No | Yes/No | Sequence: op → args → repeat → quit |
| Captured-output assertions (`capsys`) | Yes/No | Yes/No | Check printed text |
| Monkeypatch-based input control | Yes/No | Yes/No | Control `input()` during tests |
