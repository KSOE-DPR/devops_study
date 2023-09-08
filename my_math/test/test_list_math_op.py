from my_math.list_math_op import add_lists, multiply_lists, get_larger_elements

def test_always_passes():
    assert True

def test_always_fails():
    assert False

def test_list_math_op_general():
    list1 = [1, 4, 7, 2]
    list2 = [3, 2, 8, 6]
    assert add_lists(list1, list2) == [4, 6, 15, 8]
    assert multiply_lists(list1, list2) == [3, 8, 56, 12]
    assert get_larger_elements(list1, list2)[0] == [3, 4, 8, 6]
    assert get_larger_elements(list1, list2)[1] == [1, 2, 7, 2]
