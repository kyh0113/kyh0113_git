import sys
from collections import deque

N,M=map(int, sys.stdin.readline().split())

graph=[]
for i in range(N):
    graph.append(list(map(int, input())))

def queue_push(q, value):
    q.append(value)

def queue_pop(q):
    return q.popleft()

def bfs(graph,y,x): #0,0
    q=deque()
    queue_push(q,[y,x]) 
    while len(q) !=0:
        front = queue_pop(q) #front[0]=0, front[1]=0
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1] 
        for i in range(4): 
            ny = front[0] + dy[i]
            nx = front[1] + dx[i]
            if ny >= 0 and ny < N and nx >= 0 and nx < M: # 범위 안에 있으며
                if graph[ny][nx]==1: # 탐색한 위치가 1이면
                    graph[ny][nx]=graph[front[0]][front[1]] + 1 # graph[front[0]]graph[front[1]]은 현재 위치
                    queue_push(q, [ny,nx])
    return graph[N-1][M-1] # 마지막 위치까지 더해진 숫자 리턴, 행:0~N-1, 열:0~M-1

print(bfs(graph, 0,0))
"""
5 6
101010
111111
000001
111111
111111
"""