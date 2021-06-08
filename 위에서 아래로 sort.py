import sys
N = int(sys.stdin.readline())

data=[]
for i in range(N):
    data.append(int(sys.stdin.readline()))

data = sorted(data, reverse=True)

for i in range(len(data)):
    print(data[i], end=" ")