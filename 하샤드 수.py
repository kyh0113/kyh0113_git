def solution(x):
    sum = 0
    for i in range(len(str(x))):
        sum +=int(str(x)[i])
    if x%sum ==0:
        return True
    else:
        return False