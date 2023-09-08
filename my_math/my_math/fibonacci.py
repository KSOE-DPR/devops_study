'''
피보나치 수열 계산
input: 정수 n
output: 피보나치 수

참고: 다음 함수에는 오류가 있음
'''
def fib(n):
    if n == 0:
        return 0
    elif n==1 or n==2:
    	return 1
    else:
        return fib(n-1) + fib(n-2)
