from app.gen_21 import value_21


def test_value_21():
    assert value_21(2) == 2 * 4 + 4
    assert value_21(0) == 4
