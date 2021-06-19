import sys
data = list(map(int, sys.stdin.readline().split()))
array=[]
for i in range(len(data)):
    array.append(data[i]*data[i])

result=sum(array)%10
print(result)
