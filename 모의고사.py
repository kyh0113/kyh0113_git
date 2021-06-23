from itertools import cycle

def solution(answers):
    p1=[1, 2, 3, 4, 5]
    p2=[2, 1, 2, 3, 2, 4, 2, 5]
    p3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores=[0,0,0]
    winner=[]
    
    for i,j,k,ans in zip(cycle(p1), cycle(p2), cycle(p3), answers):
        if i==ans: 
            scores[0]+=1
        if j==ans: 
            scores[1]+=1
        if k==ans:
            scores[2]+=1
        
    for index, score in enumerate(scores):
        if score==max(scores):
            winner.append(index+1) # 인덱스를 맞추기
    winner.sort()
    
    return winner