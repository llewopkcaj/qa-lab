def test_func1(func_resource, module_resource, first_connection):
    assert func_resource == "func"
    assert module_resource == "module"
    assert first_connection == 12345


def test_func2(func_resource, module_resource, first_connection):
    assert func_resource == "func"
    assert module_resource == "module"
    assert isinstance(first_connection, int)


class TestClassScope:
    def test_a(self, class_resource):
        assert class_resource == "class"

    def test_b(self, class_resource):
        assert isinstance(class_resource, str)
