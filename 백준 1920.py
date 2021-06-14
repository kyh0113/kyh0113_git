import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

for i in data:
    if i in A:
        print(1)
    else:
        print(0)