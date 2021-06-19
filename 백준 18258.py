import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
queue=deque()

for i in range(N):
    st = input().split()
    if st[0]=='push':
        queue.append(st[1])
    elif st[0]=='front':
        if not queue: # 비었다면
            print(-1)
        else:
            print(queue[0])
    elif st[0]=='back':
        if not queue: # 비었다면
            print(-1)
        else:
            print(queue[-1])
    elif st[0]=='size':
        print(len(queue))
    elif st[0]=='empty':
        if not queue: # 비었다면
            print(1)
        else:
            print(0)
    elif st[0]=='pop':
        if not queue: # 비었다면
            print(-1)
        else:
            print(queue.popleft())