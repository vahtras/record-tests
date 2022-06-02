
from . import unit


def test_unit():
    actual = unit(*(22,), **{})
    expected = 22
    assert actual == expected
