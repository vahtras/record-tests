import pathlib
import textwrap
from record_tests import record

from . import unit


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
