import sys
from collections import deque
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
ans=0

d=[[]for i in range(n+1)]
for i in range(m):
    s, e=list(map(int, sys.stdin.readline().split()))
    d[s].append(e)
    d[e].append(s)

q=deque()
q.append(1)
vis=[False for i in range(n+1)]
vis[1]=True
while len(q)!=0:
    ans+=1
    front=q.popleft()
    for i in range(len(d[front])):
        if vis[d[front][i]]==False:
            vis[d[front][i]]=True
            q.append(d[front][i])
      
print(ans-1)