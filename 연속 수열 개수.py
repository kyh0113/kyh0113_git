# 합이 5인 부분 연속 수열의 개수 구하기
N, M =5, 5
data = [1, 2, 3, 2, 5]

result=0
summary=0
end=0

# start를 끝까지 갈 때까지 차례대로 증가시키며 반복
for start in range(N): # 0~4
    
    # summary가 M보다 작고 end가 끝까지 갈때까지 반복
    while summary < M and end < N: 
        summary +=data[end]
        end+=1 # while문 반복하다가 조건에 안맞으면 summary -=data[start]
    
    # 부분 합이 M일 때 카운트 증가 
    if summary == M:
        result+=1
    summary -= data[start]

print(result)
    
