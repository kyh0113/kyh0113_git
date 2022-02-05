def solution(participant, completion):
    participant.sort() # 참여자
    completion.sort() # 완주자
    
    # 완주하지 못한 선수의 이름을 return
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[i+1] # 참여자가 완주자보다 한명 더 많고 앞에사람들이 모두 완주를 했다면 맨 마지막에 남은 사람이 완주 못한 사람