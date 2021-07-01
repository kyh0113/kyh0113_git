import sys
N=int(sys.stdin.readline())

def factorial(x):
    if x==1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(N))