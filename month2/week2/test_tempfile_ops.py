import pytest

def test_file_yield(file_yield):
    assert file_yield.read_text() == "purple"

def test_file_finalizer(file_finalizer):
    assert file_finalizer.read_text() == "yellow"
