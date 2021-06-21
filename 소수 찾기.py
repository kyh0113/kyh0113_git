from math import sqrt

def sosu(a):
    for i in range(2, int(sqrt(a))+1):
        if a%i==0:
            return False
    return True

def solution(n):
    answer=0
    for i in range(2,n+1):
        if sosu(i)==True:
            answer +=1
    return answer