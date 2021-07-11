import sys
T= int(sys.stdin.readline())
for i in range(T):
    A=list(map(int, sys.stdin.readline().split()))
    A=sorted(A, reverse=True)
    print(A[2])


  