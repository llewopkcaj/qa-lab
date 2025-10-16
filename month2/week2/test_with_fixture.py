def test_eloise_val(sample_data):
    assert sample_data["Eloise"] == "learned"


def test_dtype(sample_data):
    assert all(isinstance(k, str) for k in sample_data.keys())
    assert all(isinstance(v, str) for v in sample_data.values())
