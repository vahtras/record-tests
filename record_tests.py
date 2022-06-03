import collections
import functools
import textwrap
from typing import Callable


def record(f: Callable):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return_value = f(*args, **kwargs)
        body = textwrap.dedent(
                f'''
                from {f.__module__} import {f.__name__}


                def test_{f.__name__}():
                    actual = {f.__name__}(*{args}, **{kwargs})
                    expected = {return_value!r}
                    assert actual == expected
                '''
            )
        record.records[f.__module__].append(body)
        return return_value
    return wrapper


record.records = collections.defaultdict(list)


def save_tests(testdir='tests'):
    for mod, cases in record.records.items():
        with open(f'{testdir}/test_{mod}.py', 'w') as tf:
            for case in cases:
                tf.write(case)
