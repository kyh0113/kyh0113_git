import sys
sys.setrecursionlimit(1000000)
T = int(sys.stdin.readline())

def dfs(y,x): 
    if y < 0 or y >= N or x < 0 or x >= M or l[y][x] !=1:
        return
    
    l[y][x]=0 
    dfs(y-1, x)
    dfs(y, x+1)
    dfs(y+1, x)
    dfs(y, x-1)

for _ in range(T):
    #M:가로 N:세로 K:1의 개수
    M,N,K=map(int, sys.stdin.readline().split())
    l=[] 
    for _ in range(N): #세로길이만큼 돌면서
        l=[[0 for _ in range(M)] for _ in range(N)] # 0으로 채워진 2차원 배열을 만든다
    for j in range(K):
        x,y=map(int, sys.stdin.readline().split())
        l[y][x]=1
    cnt=0
    for i in range(N):
        for j in range(M):
           if l[i][j]==1:
                cnt+=1
                dfs(i,j)
            # 연결되어있는 1을 전부 제거하는 bfs를 작성!
    print(cnt)
