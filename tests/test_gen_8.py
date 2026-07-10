from app.gen_8 import value_8


def test_value_8():
    assert value_8(2) == 2 * 9 + 1
    assert value_8(0) == 1
