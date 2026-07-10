from app.gen_12 import value_12


def test_value_12():
    assert value_12(2) == 2 * 2 + 5
    assert value_12(0) == 5
