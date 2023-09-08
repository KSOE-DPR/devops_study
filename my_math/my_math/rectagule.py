def area(a, b):
    return a*b

def long_check(a, b):
    return max(a, b)

def square_check(a, b):
    c = ""
    if a==b:
        c = "square"
    else:
    	c = "rectangule"
    return c
 
def test_rec():
    print(area(2, 3), long_check(2, 3), square_check(2, 3))
    assert area(2, 3) == 6, square_check(2, 3) == "rectangule"
