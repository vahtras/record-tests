import pathlib
import textwrap

import pytest

from record_tests import record, save_tests
from . import unit, square


@pytest.fixture(scope='module')
def fix():
    pathlib.Path('tests/test_tests.py').unlink(missing_ok=True)
    record.records.clear()
    yield
    save_tests()


def test_unit(fix):

    record(unit)(11)
    record(unit)(22)

    expected_test_11 = textwrap.dedent(
        """
        def test_unit_0():
            actual = unit(*(11,), **{})
            expected = 11
            assert actual == expected
        """
    )

    expected_test_22 = textwrap.dedent(
        """
        def test_unit_1():
            actual = unit(*(22,), **{})
            expected = 22
            assert actual == expected
        """
    )

    assert expected_test_11 in record.records['tests']['unit'][0]
    assert expected_test_22 in record.records['tests']['unit'][1]


def test_square(fix):

    record(square)(11)

    expected_test = textwrap.dedent(
        """
        def test_square_0():
            actual = square(*(11,), **{})
            expected = 121
            assert actual == expected
        """
    )

    assert expected_test in record.records['tests']['square'][0]
