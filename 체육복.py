# 배열을 이용한 문제 풀이

def solution(n, lost, reserve):
    std=[1]*n # 0~4인덱스 값 1 -> std[1,1,1,1,1]
    
    for i in reserve: # 체육복 2개 이상 있는 애들
        std[i-1] = 2 # 0,2,4 인덱스값 2 (-1을 하는 이유는 인덱스를 0~4로 맞추기 위함)
    
    for i in lost: # 체육복을 빌려야 하는 애들
        std[i-1] = std[i-1]-1 # 1,3인덱스값 0 

    for i, v in enumerate(std): # std[2,0,2,0,2] for문의 코드가 해당 안되면 걍 다음 loop 도는거임
        # 오른쪽 학생이 빌려줄 경우
        if i<n-1 and v==0 and std[i+1]==2: # 나는 체육복이 없는데 오른쪽애가 체육복 2개 이상, 3번째 인덱스에 있는 애까지만 체육복을 오른쪽 애한테서 빌릴 수 있음
            std[i]=1
            std[i+1]=1
            
        # 왼쪽 학생이 빌려줄 경우
        elif i>0 and v==0 and std[i-1]==2: # 나는 체육복이 없는데 왼쪽 애가 체육복 2개 이상, 0번째 인덱스에 있는 애는 왼쪽에 친구가 없음
            std[i]=1
            std[i-1]=1
        
    return n-std.count(0) # 옷이 없을 학생 수 제외

############################################################

# set을 이용한 문제 풀이

def solution(n, lost, reserve):
    # 여벌옷을 가져온 학생이 체육복을 하나만 도난당할 수도 있다고 문제에서 가정했음
    # 뭔말이냐면 reserve에도 lost에도 이름을 올린 애가 있을 수 있다는 말
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)
    
    # 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려주기
    for reserve in reserve_only:
        front = reserve - 1
        back = reserve + 1
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)
        
    return n -len(set(lost_only))