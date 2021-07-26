import sys
from collections import deque

n,m,v=list(map(int, sys.stdin.readline().split()))
d=[[] for i in range(n+1)] # 0~4인덱스까지 리스트 만들기
for i in range(m): # 간선 연결
    s,e=list(map(int, sys.stdin.readline().split()))
    d[s].append(e)
    d[e].append(s)
print(d) # [[], [2,3,4], [1,4], [1,4], [1,2,3]]

for i in range(1, n+1): #연결되어있는 정점 중 작은거부터 보라고
    d[i].sort()     #정렬

def dfs(d, pos, vis): # d,v,vis
    if vis[pos]==True:
        return # 반환값 없이 함수를 도중에 종료
    print(pos, end=" ")
    vis[pos]=True
    for i in range(len(d[pos])): # len(d[pos]): len(현재 탐색하는 정점의 연결리스트)
    # d[pos][i]: 현재 보고있는 pos정점의 연결되어있는 정점들
        dfs(d,d[pos][i],vis)

vis=[False for i in range(n+1)]

dfs(d,v,vis)
print()

def bfs(n,d):
    vis=[False for i in range(n+1)]
    q=deque()
    q.append(v)
    vis[v]=True
    while len(q) !=0:
        front=q.popleft()
        print(front, end=" ")
        for i in range(len(d[front])): # len(d[front]): len(현재 탐색하는 정점의 연결리스트)
            if vis[d[front][i]]==False:
                q.append(d[front][i])
                vis[d[front][i]]=True

bfs(n,d)
