from app.gen_19 import value_19


def test_value_19():
    assert value_19(2) == 2 * 9 + 7
    assert value_19(0) == 7
