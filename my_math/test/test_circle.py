from my_math.circle import circumference, area_of_circle

def test_circumference(): # 함수명에 test_를 붙여줘야 테스트할 대상으로 인식 
    print('Running circle')
    assert circumference(0) == 0, '바보래요~'
    assert circumference(1) == 6.28, '바보래요~'
    assert circumference(2) == 12.56, '바보래요~'
    assert circumference(-1) == None, '바보래요~'
        
def test_area():
    assert area_of_circle(1) == 3.14, '바보래요~'
    assert area_of_circle(2) == 12.56, '바보래요~'
    assert area_of_circle(0) == 0
    assert area_of_circle(-2) == None

