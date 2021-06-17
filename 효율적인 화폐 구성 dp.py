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
        d[j] = min(d[j], d[j - array[i]]+1) # 누적된 계산횟수에 1씩 더함


if d[m] == 10001:
    print(-1)
else:
    print(d[m])