from app.gen_6 import value_6


def test_value_6():
    assert value_6(2) == 2 * 7 + 6
    assert value_6(0) == 6
