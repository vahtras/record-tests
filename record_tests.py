import collections
import functools
import textwrap
from typing import Callable


def record(f: Callable):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return_value = f(*args, **kwargs)
        i = len(record.records[f.__module__][f.__name__])
        body = textwrap.dedent(
                f'''
                def test_{f.__name__}_{i}():
                    actual = {f.__name__}(*{args}, **{kwargs})
                    expected = {return_value!r}
                    assert actual == expected
                '''
            )
        record.records[f.__module__][f.__name__].append(body)
        return return_value
    return wrapper


# A nested dict with {'module': {'testfunc': ['testcase1', 'testcase2'...]}}
record.records = collections.defaultdict(lambda: collections.defaultdict(list))


def save_tests(testdir='tests'):
    for mod, funcs in record.records.items():
        with open(f'{testdir}/test_{mod}.py', 'w') as tf:
            tf.write(f'from {mod} import {", ".join(funcs)}\n')
            for func, cases in funcs.items():
                tf.write("\n" + "\n".join(cases))
