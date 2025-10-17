import pytest

from month2.week2.calculator import Calculator


@pytest.fixture
def sample_data():
    return {"Columbia": "main", "Eloise": "learned", "Safiya": "undone", "Reggie": "following"}


@pytest.fixture(scope="session")
def first_connection():
    print("setting up")
    elmo = 12345
    yield elmo
    print("it worked!")


@pytest.fixture
def run_calc():
    """function-scope: fresh calculator per test"""
    return Calculator()


@pytest.fixture(scope="function")
def func_resource():
    print("FUNCTION: setup")
    yield "func"
    print("FUNCTION: teardown")


@pytest.fixture(scope="module")
def module_resource():
    print("MODULE: setup")
    yield "module"
    print("MODULE: teardown")


@pytest.fixture(scope="class")
def class_resource():
    print("CLASS: setup")
    yield "class"
    print("CLASS: teardown")


@pytest.fixture
def file_yield(tmp_path):
    path = tmp_path / "purple.txt"
    path.write_text("purple")
    yield path
    if path.exists():
        path.unlink()


@pytest.fixture
def file_finalizer(request, tmp_path):
    path = tmp_path / "yellow.txt"
    path.write_text("yellow")

    def clean():
        if path.exists():
            path.unlink()

    request.addfinalizer(clean)
    return path
