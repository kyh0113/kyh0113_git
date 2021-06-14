import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

for i in range(len(data)):
    print(array.count(data[i]))
