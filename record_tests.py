import textwrap
from typing import Callable


def record(f: Callable):
    def wrapper(*args, **kwargs):
        return_value = f(*args, **kwargs)
        with open(f'tests/test_{f.__name__}.py', 'w') as tf:
            tf.write(textwrap.dedent(
                f'''
                from . import {f.__name__}


                def test_{f.__name__}():
                    actual = {f.__name__}(*{args}, **{kwargs})
                    expected = {return_value}
                    assert actual == expected
                '''
            ))
        return return_value
    return wrapper
