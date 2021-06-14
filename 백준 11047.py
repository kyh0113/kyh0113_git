import sys
N, K = map(int,sys.stdin.readline().split())
count = 0

coin = []
for i in range(N):
    coin.append(int(sys.stdin.readline()))

for i in range(N-1, -1, -1):
    count += K // coin[i] # count=4
    K %= coin[i] # K=200

print(count)
    