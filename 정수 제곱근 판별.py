from math import sqrt
def solution(n):
    n=sqrt(n)+1
    if n%1==0: # 수를 1로 나누었을 때 나머지가 0 = 정수
        return n*n
    else:
        return -1