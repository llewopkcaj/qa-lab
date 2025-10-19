import builtins
import re

import pytest

from month1.week2.cli_calculator import run_it


def _numbers_in(s: str):
    return re.findall(r"-?\d+(?:\.\d+)?", s)


@pytest.mark.smoke
@pytest.mark.regression
def test_all_numbers_have_two_decimals(monkeypatch, capsys):
    seq = iter(["add", "2", "3", "multiply", "-4", "5", "sqrt", "16", "q"])
    monkeypatch.setattr(builtins, "input", lambda _=None: next(seq))
    run_it()
    out, _ = capsys.readouterr()

    nums = set(_numbers_in(out))
    for n in nums:
        assert f"{float(n):.2f}" in out


@pytest.mark.ux
@pytest.mark.regression
def test_every_error_line_prefixed(monkeypatch, capsys):
    seq = iter(["divide", "5", "0", "wrong", "1", "2", "sqrt", "-9", "q"])
    monkeypatch.setattr(builtins, "input", lambda _=None: next(seq))
    run_it()
    out, _ = capsys.readouterr()

    error_lines = [line for line in out.splitlines() if "Error:" in line]
    assert error_lines, "Expected at least one Error: line"
    assert all(line.startswith("Error:") for line in error_lines)


@pytest.mark.regression
def test_success_line_present_and_goodbye(monkeypatch, capsys):
    seq = iter(["power", "3", "2", "q"])
    monkeypatch.setattr(builtins, "input", lambda _=None: next(seq))
    run_it()
    out, _ = capsys.readouterr()
    assert "Result:" in out
    assert "Goodbye!" in out
