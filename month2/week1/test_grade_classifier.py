from month1.week2.grade_classifier import grade_classifier


# --- Basic buckets ---
def test_grade_a():
    assert grade_classifier(95) == "A"


def test_grade_b():
    assert grade_classifier(71) == "B"


def test_grade_c():
    assert grade_classifier(50) == "C"


def test_grade_d():
    assert grade_classifier(30) == "D"


def test_grade_f():
    assert grade_classifier(10) == "F"


# --- Boundary edges ---
def test_boundary_a():
    assert grade_classifier(80) == "A"
    assert grade_classifier(100) == "A"


def test_boundary_b():
    assert grade_classifier(60) == "B"
    assert grade_classifier(79) == "B"


def test_boundary_c():
    assert grade_classifier(40) == "C"
    assert grade_classifier(59) == "C"


def test_boundary_d():
    assert grade_classifier(20) == "D"
    assert grade_classifier(39) == "D"


def test_boundary_f():
    assert grade_classifier(0) == "F"
    assert grade_classifier(19) == "F"


# --- Out-of-range ---
def test_extreme_high():
    assert grade_classifier(101) == "Invalid number (out of range)"


def test_extreme_low():
    assert grade_classifier(-1) == "Invalid number (out of range)"
