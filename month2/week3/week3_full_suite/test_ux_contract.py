import builtins

from month1.week2.cli_calculator import run_it


def test_contract(monkeypatch, capsys):
    it = iter(["add", "3.5", "2.5", "q"])
    monkeypatch.setattr(builtins, "input", lambda _=None: next(it, "q"))

    run_it()
    out, _ = capsys.readouterr()

    assert "Result: 3.50 add 2.50 is 6.00" in out
    assert "Goodbye!" in out
