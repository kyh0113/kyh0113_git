import sys
N, M=list(map(int, sys.stdin.readline().split())) # 5 3

data=list(map(int, sys.stdin.readline().split())) # 5 4 3 2 1

summary = 0
prefix_sum=[0] 
for i in data:
    summary+=i
    prefix_sum.append(summary) # prefix_sum=[5, 9, 12, 14, 15]

for i in range(M):
    ll=list(map(int, sys.stdin.readline().split())) # 1 3, 2 4, 5 5
    left=ll[0]
    right=ll[1]
    print(prefix_sum[right]-prefix_sum[left-1])
    ll.clear()
    
   