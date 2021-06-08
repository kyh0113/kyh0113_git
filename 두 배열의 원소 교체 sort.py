import sys
N, K = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))


a = sorted(a) # [1, 2, 3, 4, 5]
b = sorted(b, reverse=True) # [6, 6, 5, 5, 5]

# 최대 K번 바꿔치기 가능
for i in range(K):
    if a[i] < b[i]:
        a[i] = b[i]
    else : 
        break
print(sum(a))