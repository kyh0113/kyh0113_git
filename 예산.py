def solution(d, budget):
    d.sort()
    total=0
    cnt=0
    for i in range(len(d)):
        total += d[i]
        if total > budget:
            break
        else:
            cnt+=1
    return cnt
        