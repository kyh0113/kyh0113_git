import sys
a,b=map(int, sys.stdin.readline().split())

def gcd(a,b):
    x=min(a,b)
    while 1:
        if a%x==0 and b%x==0:
            return x
        else:
            x-=1
    
result=gcd(a,b)
print(result)
print((a//result)*(b//result)*result)
