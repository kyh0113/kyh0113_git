import sys
N = int(sys.stdin.readline())
array = set(map(int, sys.stdin.readline().split())) # {2, 3, 7, 8, 9}
M = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

for i in data: # 5, 7, 9
    if i in array: # 8, 3, 7, 9, 2
        print("yes", end=" ")
    else:
        print("no", end=" ")