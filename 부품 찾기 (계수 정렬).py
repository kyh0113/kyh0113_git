import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

count = [0] * (max(array) + 1) 

for i in range(len(array)):
    count[array[i]] = 1

for i in data:
    if count[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")



