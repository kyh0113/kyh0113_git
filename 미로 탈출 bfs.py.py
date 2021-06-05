import sys
from collections import deque

N, M =map(int, sys.stdin.readline().split())
graph=[]

for i in range(N):
    graph.append(list(map(int, input())))

def queue_push(q, value):
    q.append(value)

def queue_pop(q):
    return q.popleft()

def bfs(graph, y,x):
    q=deque() # 넓이 우선 탐색으로 가장 가까운 노드부터 탐색
    queue_push(q,[y,x])
    while len(q)!=0:
        front=queue_pop(q)
        by = [-1, 0, 1, 0]
        bx = [0, 1, 0, -1]
        for i in range(4):
            ny = front[0] + by[i]
            nx = front[1] + bx[i]
            if ny >= 0 and ny < N and nx >= 0 and nx < M: # 범위에 있으며
                if graph[ny][nx]==1: # 탐색한 위치가 1일때
                    graph[ny][nx]=graph[front[0]][front[1]] + 1 # graph[front[0]][front[1]]는 1임
                    queue_push(q, [ny,nx])
    return graph[N-1][M-1] # 행:0~N-1 열:0~M-1

print(bfs(graph,0,0))

"""
5 6
101010
111111
000001
111111
111111
"""