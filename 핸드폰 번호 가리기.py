def solution(phone_number):
    answer=[]
    answer.append("*"*len(phone_number[0:-4]))
    answer.append(phone_number[-4:])
    answer="".join(answer) # 문자열 합치기
    return answer