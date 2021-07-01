import sys
N=int(sys.stdin.readline())

d=[0]*21
def fibo(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    d[n] = fibo(n-1)+fibo(n-2)
    return d[n]
print(fibo(N))