def solution(n):
    a="수박"
    b="수"
    result = n//2
    if n%2==0:
        return a*result
    else:
        return a*result+b