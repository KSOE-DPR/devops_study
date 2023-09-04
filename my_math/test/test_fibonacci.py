from my_math.fibonacci import fib

def test_always_passes():
    assert True

# def test_always_fails():
#     assert False

def test_fibonacci_general():
    assert fib(7) == 13
    assert fib(8) == 21
