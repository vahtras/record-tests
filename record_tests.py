from functools import wraps
import textwrap
from typing import Callable


def record(f: Callable):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return_value = f(*args, **kwargs)
        with open(f'tests/test_{f.__name__}.py', 'w') as tf:
            tf.write(textwrap.dedent(
                f'''
                from {f.__module__} import {f.__name__}


                def test_{f.__name__}():
                    actual = {f.__name__}(*{args}, **{kwargs})
                    expected = {return_value}
                    assert actual == expected
                '''
            ))
        return return_value
    return wrapper
