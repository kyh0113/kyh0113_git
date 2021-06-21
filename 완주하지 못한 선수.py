def solution(participant, completion):
    participant.sort() # 참여자
    completion.sort() # 완주자
    
    # 완주하지 못한 선수의 이름을 return
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[i+1]