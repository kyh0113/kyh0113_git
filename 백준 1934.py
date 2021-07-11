import sys
from math import gcd
T=int(sys.stdin.readline())

for i in range(T):
    A, B=map(int, sys.stdin.readline().split())
    print(A*B//gcd(A,B))

            