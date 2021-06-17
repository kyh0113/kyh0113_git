import sys
n, m = map(int, sys.stdin.readline().split()) 
array = [] 
for i in range(n):
    array.append(int(sys.stdin.readline()))

d = [10001] * (m+1)

d[0] = 0
for i in range(len(array)):
    d[array[i]] = 1

for i in range(n): 
    for j in range(array[i], m+1): 
        d[j] = min(d[j], d[j - array[i]]+1) 
        # 현재의 수에 각 화폐를 빼면 그 전까지 계산된 누적된 최소 횟수가 나옴 

if d[m] == 10001:
    print(-1)
else:
    print(d[m])