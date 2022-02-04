# h시 59분 59초 안에 3이라는 숫자가 몇번 들어가는지 개수 세기
h = int(input()) 

count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1

print(count)
            