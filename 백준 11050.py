import sys
from math import factorial

N, K=map(int, sys.stdin.readline().split())
result=factorial(N)//(factorial(K)*factorial(N-K))
print(result)