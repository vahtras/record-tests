import pathlib
import textwrap
from record_tests import record

from . import unit, square


def test_unit():

    record(unit)(22)

    expected_test = textwrap.dedent(
        """
        from . import unit


        def test_unit():
            actual = unit(*(22,), **{})
            expected = 22
            assert actual == expected
        """
    )

    assert pathlib.Path('tests/test_unit.py').exists()
    actual_test = open('tests/test_unit.py').read()
    assert actual_test == expected_test


def test_square():

    record(square)(11)

    expected_test = textwrap.dedent(
        """
        from . import square


        def test_square():
            actual = square(*(11,), **{})
            expected = 121
            assert actual == expected
        """
    )

    assert pathlib.Path('tests/test_square.py').exists()
    actual_test = open('tests/test_square.py').read()
    assert actual_test == expected_test
