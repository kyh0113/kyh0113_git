N= int(input())
result=[]
# 숫자 분해하기
for i in range(10, N): # 10부터 숫자 쪼갤 수 있음
    total=0 # 쪼갠 수 더해질 변수
    for j in range(len(str(i))): # 길이만큼
        total += int(str(i)[j])
    if total+i==N:
        result.append(i)

if len(result)==0:
    answer=0
else:
    answer=min(result)

print(answer)
