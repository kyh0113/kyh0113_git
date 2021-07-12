import sys
n=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
x=int(sys.stdin.readline())

count=0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if (a[i]+a[j])==x:
            count+=1
print(count)



    