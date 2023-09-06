'''
피보나치 수열 계산
input: 정수 n
output: 피보나치 수

참고: 다음 함수에는 오류가 있음
'''
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == -1:
        return 1

    a, b = 0, 1
    for i in range(2, abs(n) + 1):
        a, b = b, a + b

    # 음수 인덱스의 경우 부호를 조절
    if n < 0 and n % 2 == 0:
        return -b
    return b