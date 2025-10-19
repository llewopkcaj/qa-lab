import builtins

import pytest

from month1.week2.cli_calculator import run_it


def fake_iterator(monkeypatch, sequence, fallback="q"):
    inputs = iter(sequence)
    monkeypatch.setattr(builtins, "input", lambda _=None: next(inputs, fallback))


@pytest.mark.smoke
def test_quit_immediate(monkeypatch, capsys):
    fake_iterator(monkeypatch, ["q"])
    run_it()
    out, _ = capsys.readouterr()
    assert "Goodbye!" in out


@pytest.mark.smoke
@pytest.mark.ux
def test_quit_after_function(monkeypatch, capsys):
    fake_iterator(monkeypatch, ["add", "4", "5", "q"])
    run_it()
    out, _ = capsys.readouterr()
    assert "Result:" in out
    assert "4.00 add 5.00 is 9.00" in out
    assert "Goodbye!" in out


@pytest.mark.regression
@pytest.mark.ux
def test_wrong_operation_and_quit(monkeypatch, capsys):
    fake_iterator(monkeypatch, ["wrong", "4", "7", "q"])
    run_it()
    out, _ = capsys.readouterr()
    assert "Error:" in out
    assert "invalid operation" in out.lower()
    assert "Goodbye!" in out


@pytest.mark.regression
@pytest.mark.ux
def test_incorrect_input_and_retry(monkeypatch, capsys):
    fake_iterator(monkeypatch, ["subtract", "eleven", "1en", "subtract", "11", "10", "q"])
    run_it()
    out, _ = capsys.readouterr()
    assert "Error:" in out
    assert "inputs must be numbers" in out.lower()
    assert "Result:" in out
    assert "11.00 subtract 10.00 is 1.00" in out
    assert "Goodbye!" in out


@pytest.mark.ux
def test_float_conversion_valid(monkeypatch, capsys):
    fake_iterator(monkeypatch, ["add", "3.5", "2.5", "q"])
    run_it()
    out, _ = capsys.readouterr()
    assert "Result:" in out
    assert ".00" in out
    assert "Goodbye!" in out


@pytest.mark.regression
def test_cli_arith_errors(monkeypatch, capsys):
    fake_iterator(monkeypatch, ["divide", "4", "0", "q"])
    run_it()
    out, _ = capsys.readouterr()
    assert "Error:" in out
    assert "cannot divide by zero" in out.lower()


@pytest.mark.regression
@pytest.mark.ux
def test_empty_operator(monkeypatch, capsys):
    fake_iterator(monkeypatch, ["divide", "20", " ", "q"])
    run_it()
    out, _ = capsys.readouterr()
    assert "Error:" in out
    assert "Traceback" not in out
    assert "Goodbye!" in out


@pytest.mark.regression
@pytest.mark.ux
def test_complete_flow(monkeypatch, capsys):
    fake_iterator(monkeypatch, ["multiply", "9", "9", "add", "888", "97", "q"])
    run_it()
    out, _ = capsys.readouterr()
    assert out.count("Result:") >= 2
    assert "9.00 multiply 9.00 is 81.00" in out
    assert "888.00 add 97.00 is 985.00" in out
    assert "Traceback" not in out
    assert "Goodbye!" in out
