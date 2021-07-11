l=[]
answer=[]
for i in range(3):
    l.append(list(map(int, input().split())))
# l=[[5,5],[5,7],[7,5]]

for i in range(0,2): # 0~1
    if l[0][i] == l[1][i]:
        answer.append(l[2][i])
    elif l[0][i] == l[2][i]:
        answer.append(l[1][i])
    elif l[1][i] == l[2][i]:
        answer.append(l[0][i])

for i in range(len(answer)):
    print(answer[i], end=" ")