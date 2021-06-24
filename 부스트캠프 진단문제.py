
def solution(arr):
    answer = []
    count = [0]*101

    for i in range(len(arr)):
        count[arr[i]] += 1
    
    # 0과 1을 제외한 나머지 리스트 출력
    for i in range(len(count)):
        if count[i] ==0:
            pass
        elif count[i] ==1:
            pass
        else:
            answer.append(count[i])

    if answer==[]:
        answer.append(-1)

    return answer
   
arr=[3, 5, 7, 9, 1] 
print(solution(arr))


