import sys
from math import sqrt
M, N=map(int, sys.stdin.readline().split())

def sosu(x):
    if x==1:
        return False
    else:
        for i in range(2, int(sqrt(x))+1):
            if x%i==0:
                return False
        return True

for i in range(M,N+1):
    if sosu(i)==True:
        print(i)