
from tests import square


def test_square():
    actual = square(*(11,), **{})
    expected = 121
    assert actual == expected
