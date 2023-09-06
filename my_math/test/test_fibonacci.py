from my_math.fibonacci import fib

def test_always_passes():
    assert True

def test_always_fails():
    assert False

def test_fibonacci_positive():
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13

def test_fibonacci_negative():
    assert fib(-5) == 5
    assert fib(-6) == -8
    assert fib(-7) == 13
