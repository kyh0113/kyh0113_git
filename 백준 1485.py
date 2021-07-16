# import sys
# N= int(sys.stdin.readline())

# dot=[]
# for i in range(N):
#     for _ in range(4): #dot=[list(map(int, input().split()))for _ in range(4)]
#         dot.append(list(map(int, input().split())))
#     l=[]
#     for j in range(3): # 0,1,2
#         for k in range(j+1,4): # 1,2,3
#             l.append(((dot[j][0]-dot[k][0])**2)+((dot[j][1]-dot[k][1])**2))
#     l.sort() # 각 변의 길이와 대각선 길이가 정렬됨
#     if l[0]==l[1] and l[0]==l[2] and l[0]==l[3] and l[4]==l[5]:
#         print(1)
#     else:
#         print(0)
import sys
line=sys.stdin.readline

N=int(line())

dot=[]
for i in range(N):
    for j in range(4):
        dot.append(list(map(int, input().split())))
    L=list()
    for i in range(3):
        for j in range(i+1,4):
            L.append((dot[i][0]-dot[j][0])*(dot[i][0]-dot[j][0])+(dot[i][1]-dot[j][1])*(dot[i][1]-dot[j][1]))
    L.sort()
    if L[0]==L[1] and L[0]==L[2] and L[0]==L[3] and L[4]==L[5]:
        print(1)
        dot.clear()
    else:
        print(0)
        dot.clear()