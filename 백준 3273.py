import sys
n=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
x=int(sys.stdin.readline())

a.sort()
start=0
end=n-1
result=0

while start<end:
    tmp=a[start]+a[end]
    if tmp==x:
        result+=1
        start+=1
    elif tmp < x:
        start+=1
    else:
        end-=1
print(result)