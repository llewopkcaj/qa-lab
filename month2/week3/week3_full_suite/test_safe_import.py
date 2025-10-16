import builtins
import importlib

import pytest


@pytest.mark.smoke
def test_safe_import(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _=None: "q")
    module = importlib.import_module("month1.week2.cli_calculator")
    assert hasattr(module, "run_it") and callable(module.run_it)
