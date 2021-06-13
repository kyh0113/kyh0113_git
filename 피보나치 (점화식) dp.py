# N번째 피보나치 수 = (N-1)번째 피보나치 수 + (N-2)번째 피보나치 수
# 단, 1번째와 2번째 피보나치 수는 1
import sys
N = int(sys.stdin.readline())

def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

print(fibo(N))

"""
1 1 2 3 5 8 13 21 ~~~
"""