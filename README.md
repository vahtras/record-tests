# Recording tests

Generate unit tests for an existing function automatically by running a code in production
with the function decorated 

Decorate the function
~~~
# foo.py
from record_tests import record


@record
def bar():
    return 'baz'
~~~

Run code that calls the function
~~~
# demo.py
import record_tests

import foo
print(foo.bar())

record_tests.save_tests('tests')
~~~

~~~
$ python demo.py
baz
~~~

A test file is generated
~~~
from foo import bar


def test_bar_0():
    actual = bar(*(), **{})
    expected = 'baz'
    assert actual == expected
~~~

Run the test
~~~
$ pytest -v -k foo                                                                                                                                                                                   148 ↵
============================= test session starts ==============================
platform linux -- Python 3.9.0, pytest-7.1.2, pluggy-1.0.0 -- /home/olav/.venvs/record-tests/bin/python3
cachedir: .pytest_cache
rootdir: /home/olav/dev/py/record-tests
collecting ... collected 6 items / 5 deselected / 1 selected

tests/test_foo.py::test_bar_0 PASSED                                     [100%]

======================= 1 passed, 5 deselected in 0.01s ========================
~~~
    
