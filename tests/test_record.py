import pathlib
import textwrap

import pytest

from record_tests import record, save_tests
from . import unit, square


@pytest.fixture(scope='module')
def fix():
    pathlib.Path('tests/test_tests.py').unlink()
    record.records.clear()
    yield
    save_tests()


def test_unit(fix):

    record(unit)(22)

    expected_test = textwrap.dedent(
        """
        from tests import unit


        def test_unit():
            actual = unit(*(22,), **{})
            expected = 22
            assert actual == expected
        """
    )

    assert expected_test in record.records['tests']


def test_square(fix):

    record(square)(11)

    expected_test = textwrap.dedent(
        """
        from tests import square


        def test_square():
            actual = square(*(11,), **{})
            expected = 121
            assert actual == expected
        """
    )

    assert expected_test in record.records['tests']
