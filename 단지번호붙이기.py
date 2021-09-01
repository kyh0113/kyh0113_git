import sys
n=int(sys.stdin.readline())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

result=[]
def dfs(data, y, x):
    global nums
    if data[y][x]==1:
        nums+=1
    data[y][x]=0
    by=[-1,0,1,0]
    bx=[0,1,0,-1]
    for i in range(4):
        ny = y + by[i]
        nx = x + bx[i] 
        if ny < 0 or ny>=n or nx < 0 or nx >=n:
            pass
        else:
            if data[ny][nx]==1:
                dfs(data, ny, nx)           

cnt=0
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt+=1 # 몇덩이인지 확인
            nums=0 # 몇개인지 확인
            dfs(graph, i, j)
            result.append(nums)
            
print(cnt)
result.sort()
for i in result:
    print(i)