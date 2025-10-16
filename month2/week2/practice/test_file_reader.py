import os
import tempfile

import pytest


@pytest.fixture
def file_setup_teardown():
    path = tempfile.NamedTemporaryFile(delete=False).name
    with open(path, "w") as f:
        f.write("QA Automation Rocks")
    yield path
    os.remove(path)


def test_file_contains_phrase(file_setup_teardown):
    with open(file_setup_teardown) as f:
        text = f.read()
    assert "Automation" in text
