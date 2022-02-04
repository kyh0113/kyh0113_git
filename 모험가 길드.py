# 오름차순 정렬 이후에 공포도가 가장 낮은 모험가부터 하나씩 확인하기 (항상 최소한의 모험가의 수만 포함하여 그룹 결성)
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result +=1 # 총 그룹의 수 증가시키기
        count = 0 
print(result)