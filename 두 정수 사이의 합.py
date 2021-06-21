def solution(a, b):
    if a>b:
        b, a = a, b
    answer=0
    for i in range(a, b+1):
        answer += i
    return answer