from collections import deque
import sys

def queue_push(queue, value):
    queue.append(value)

def queue_pop(queue):
    front=queue.popleft()
    return front

N,K=list(map(int, sys.stdin.readline().split()))

queue=deque()
for i in range(1, N+1):
    queue_push(queue,i) #queue에 숫자 정렬

print("<", end="")
while len(queue)>1:
    for i in range(K-1):
        front=queue_pop(queue)
        queue_push(queue, front)
    front=queue_pop(queue)
    print(front, end=", ")


front=queue_pop(queue)
print(front, end="")
print(">")


