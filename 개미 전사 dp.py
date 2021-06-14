import sys
N = int(sys.stdin.readline()) # 4
array = list(map(int, sys.stdin.readline().split())) # 1 3 1 5

d = [0] * 101
 
d[0] = array[0] # 1
d[1] = max(d[0], array[1]) # 3

for i in range(2, N):
    d[i] = max(d[i-1], d[i-2]+array[i]) # max(현 숫자의 1칸 앞의 수, 현 숫자 + 2칸 앞의 수)
    # print(d[i])

print(d[N-1])
