from my_math.fibonacci import fib

def test_always_passes():
    assert True

# def test_always_fails():
#     assert False

def test_fibonacci_general():
    assert fib(-1) == 0
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
    assert fib(9) == 34

