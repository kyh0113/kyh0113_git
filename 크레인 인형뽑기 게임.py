def solution(board, moves):
    moves = list(map(lambda m : m-1, moves))
    stack=[0]
    cnt = 0
    for i in moves:
        for j in board:
            if j[i] != 0:
                stack.append(j[i])
                j[i]=0
                if stack[-1]==stack[-2]:
                    stack.pop()
                    stack.pop()
                    cnt += 2 
                break
    return cnt