def solution(n):
    answer=[]
    n=list(str(n))
    n.reverse() # 뒤집는건 문자열만 가능
    for i in n:
        answer.append(int(i))
    return answer