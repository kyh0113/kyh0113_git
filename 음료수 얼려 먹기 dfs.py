import sys
n, m=map(int, sys.stdin.readline().split())

data=[]
for i in range(n):
    data.append(list(map(int, input())))

# 0을 1로 바꿔주는 함수
def dfs(data,y,x):
    data[y][x]=1 # 0인걸 일단 1로 바꿔줌
    dy=[-1, 0, 1, 0] # 상 오 아 왼
    dx=[0, 1, 0, -1] # 상 오 아 왼
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        # 공간을 벗어나는 경우 무시
        if ny < 0 or ny>=n or nx<0 or nx>=m:
            pass
        else:
            if data[ny][nx]==0: # 상하좌우로 탐색한 결과 0이 나오면 
                dfs(data,ny,nx) # 재귀함수를 이용하여 0을 1로 바꾸러감
cnt=0
# 0이 발견되는 순간 카운트에 1 더하기
for i in range(n):
    for j in range(m): # 2중 for문 돌면서 값이 0인 위치를 찾아다님
        if data[i][j]==0: 
            cnt+=1
            dfs(data,i,j)

print(cnt)
"""
4 5
00110
00011
11111
00000
"""
