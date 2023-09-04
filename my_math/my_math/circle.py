def circumference(n):
    return 2 * 3.14 * n

def area_of_circle(n):
    return n**2 * 3.14

def test_main(): # 함수명에 test_를 붙여줘야 테스트할 대상으로 인식 
    print('Running circle')
    print(circumference(2), area_of_circle(2))
    assert circumference(0) == 4, '바보래요~'