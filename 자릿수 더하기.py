def solution(n):
    total=0
    for i in range(len(str(n))):
        total += int(str(n)[i])
    return total