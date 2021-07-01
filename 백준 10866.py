import sys
from collections import deque

N=int(sys.stdin.readline())
queue=deque()

for i in range(N):
    st = list(sys.stdin.readline().split())
    if st[0] == "push_back":
        queue.append(st[1])
    elif st[0] =="push_front":
        queue.appendleft(st[1])
    elif st[0] == "front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif st[0]=="back":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
    elif st[0] =="size":
        print(len(queue))
    elif st[0]=="empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif st[0]=="pop_front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif st[0]=="pop_back":
        if len(queue)==0:
            print(-1)
        else:print(queue.pop()) 


