from my_math.calculator import add, subtract, multiply, divide, sin, cos, tan

def test_always_passes():
    assert True

# def test_always_fails():
#     assert False

def test_calculator_add():
    assert add(1, 5) == 6
    assert add(2, -6) == -4
    assert add(7, 10) == 17

def test_calculator_subtract():
    assert subtract(5, 1) == 4
    assert subtract(5, -1) == 6
    assert subtract(-7, 9) == -16

def test_calculator_multiply():
    assert multiply(5, 1) == 5
    assert multiply(2, 4) == 8
    assert multiply(5, -3) == -15

def test_calculator_divide():
    assert divide(5, 2) == 2.5
    assert divide(6, 3) == 2
    assert divide(10, 2) == 5

def test_calculator_sin():
    assert sin(5) == -0.9589242746631385
    assert sin(6) == -0.27941549819892586
    assert sin(7) == 0.6569865987187891

def test_calculator_cos():
    assert cos(5) == 0.28366218546322625
    assert cos(6) == 0.960170286650366
    assert cos(7) == 0.7539022543433046

def test_calculator_tan():
    assert tan(5) == -3.380515006246586
    assert tan(6) == -0.29100619138474915
    assert tan(7) == 0.8714479827243188

