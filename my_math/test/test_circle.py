from my_math.circle import circumference, area_of_circle

def test_main(): # 함수명에 test_를 붙여줘야 테스트할 대상으로 인식 
    print('Running circle')
    print(circumference(2), area_of_circle(2))
    assert circumference(0) == 0, '바보래요~'
    assert area_of_circle(1) == 3.14, '바보래요~'
    assert area_of_circle(2) == 5, '바보래요~'
