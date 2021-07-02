import sys
T=int(sys.stdin.readline())

for i in range(T):
    H, W, N=list(map(int,sys.stdin.readline().split()))
    A = N%H # 층 수
    B = (N//H)+1 # 호 수

    if A==0:
        A=H
        B=N//H
    print((A*100)+B)