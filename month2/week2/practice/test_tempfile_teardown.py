import os
import tempfile

import pytest


@pytest.fixture
def temp_file():
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(b"hello")
    f.close()
    yield f.name
    os.remove(f.name)


def test_tempfile_content(temp_file):
    with open(temp_file) as f:
        assert f.read() == "hello"
