
from undertest import FunctionUnderTest

def test_FunctionUnderTest__with_no_args():

    def f():
        f.was_called = True
        return 'f result'

    f_undertest = FunctionUnderTest(f)
    result = f_undertest.call()

    assert f.was_called
    assert f_undertest.result == 'f result'

def test_FunctionUnderTest__with_args():

    def f(*args):
        f.was_called = True
        f.args_given = args
        return 'f result'

    f_undertest = FunctionUnderTest(f, 1, 2)
    result = f_undertest.call()

    assert f.was_called
    assert f.args_given == (1, 2)
    assert f_undertest.result == 'f result'

def test_FunctionUnderTest__with_more_args_added_after_creation():

    def f(*args):
        f.was_called = True
        f.args_given = args
        return 'f result'

    f_undertest = FunctionUnderTest(f, 1, 2)
    f_undertest.add_args(3, 4)
    result = f_undertest.call()

    assert f.was_called
    assert f.args_given == (1, 2, 3, 4)
    assert f_undertest.result == 'f result'

def test_FunctionUnderTest__with_kwargs():

    def f(*args, **kwargs):
        f.was_called = True
        f.args_given = args
        f.kwargs_given = kwargs
        return 'f result'

    f_undertest = FunctionUnderTest(f, a=1, b=2)
    result = f_undertest.call()

    assert f.was_called
    assert f.args_given == ()
    assert f.kwargs_given == {'a': 1, 'b': 2}
    assert f_undertest.result == 'f result'

def test_FunctionUnderTest__with_kwargs_added_later():

    def f(*args, **kwargs):
        f.was_called = True
        f.args_given = args
        f.kwargs_given = kwargs
        return 'f result'

    f_undertest = FunctionUnderTest(f, a=1, b=2)
    f_undertest.add_args(b=3, c=4)
    result = f_undertest.call()

    assert f.was_called
    assert f.kwargs_given == {'a': 1, 'b': 3, 'c': 4}
    assert f_undertest.result == 'f result'

def test_FunctionUnderTest__with_args_and_kwargs():

    def f(*args, **kwargs):
        f.was_called = True
        f.args_given = args
        f.kwargs_given = kwargs
        return 'f result'

    f_undertest = FunctionUnderTest(f, 1, 2, a='x', b='y')
    result = f_undertest.call()

    assert f.was_called
    assert f.args_given == (1, 2)
    assert f.kwargs_given == {'a': 'x', 'b': 'y'}
    assert f_undertest.result == 'f result'

def test_FunctionUnderTest__with_args_and_kwargs_added_later():

    def f(*args, **kwargs):
        f.was_called = True
        f.args_given = args
        f.kwargs_given = kwargs
        return 'f result'

    f_undertest = FunctionUnderTest(f, 1, 2, a='x', b='y')
    f_undertest.add_args(3, 4, b='z', c='w')
    result = f_undertest.call()

    assert f.was_called
    assert f.args_given == (1, 2, 3, 4)
    assert f.kwargs_given == {'a': 'x', 'b': 'z', 'c': 'w'}
    assert f_undertest.result == 'f result'
