def solution(s):
    answer=[]
    s=s.split(" ") # s[0]=try s[1]= hello s[2]=world
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j%2==0: # 짝수면
                answer.append(s[i][j].upper())
            else: 
                answer.append(s[i][j].lower())
        answer.append(" ")
    answer="".join(answer)
    return answer[:-1] # 뒤에 공백 빼고 출력