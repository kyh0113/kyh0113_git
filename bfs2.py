import sys

from collections import deque


N,M=list(map(int, sys.stdin.readline().split())) #N:세로,y M:가로,x
graph=[]
for i in range(N):
    graph.append(list(map(int, input())))

def queue_push(q, value):
    q.append(value)

def queue_pop(q):
    return q.popleft()

def bfs(graph,y,x):
    q=deque()
    queue_push(q, [y,x])
    while len(q) !=0:
        front=queue_pop(q)
        graph[front[0]][front[1]]=1
        by=[-1,0,1,0]
        bx=[0,1,0,-1]
        for i in range(4):
            ny=front[0]+by[i]
            nx=front[1]+bx[i]
            if ny < 0 or ny >= len(graph) or nx < 0 or nx >= len(graph[0]):
                pass
            else:
                if graph[ny][nx]==0:
                    queue_push(q,[ny,nx])

cnt=0
for i in range(N): #세로(y)
    for j in range(M): #가로(x)
        if graph[i][j]==0:
            cnt+=1
            bfs(graph,i,j)

print(cnt)



"""
4 5
00110
00011
11111
00000
"""