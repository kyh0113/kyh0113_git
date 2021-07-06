import sys
N = int(sys.stdin.readline())

result=[]
for i in range(N):
    num = list(map(int,sys.stdin.readline().split()))
    result.append(num)

result.sort(key=lambda x : (x[1], x[0]))

for i in result:
    print(i[0], i[1])

