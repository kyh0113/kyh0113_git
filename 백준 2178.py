import sys
from collections import deque

N,M=list(map(int, sys.stdin.readline().split()))
l=[]
for i in range(N):
    l.append(list(map(int, input())))

by=[-1,0,1,0]
bx=[0,1,0,-1]

b=[[0 for i in range(M)] for j in range(N)]
b[0][0]=1

q=deque()
q.append([0,0])
while len(q)!=0:
    front = q.popleft()
    for i in range(4):
        ny=front[0]+by[i]
        nx=front[1]+bx[i]
        if ny >= 0 and ny < N and nx >= 0 and nx < M:
            if(l[ny][nx]==1 and b[ny][nx]==0):
                b[ny][nx]=b[front[0]][front[1]]+1 #다음번으로 이동하는거는 이전까지 이동한거의 +1만큼 이동
                q.append([ny,nx])

print(b[N-1][M-1])

