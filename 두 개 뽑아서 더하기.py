def solution(numbers):
    answer = []
    result=[]
    for i in range(len(numbers)-1) :
        for j in range(i+1,len(numbers)) :
            answer.append(numbers[i]+numbers[j])
    answer = set(answer) # {}
    return list(sorted(answer))