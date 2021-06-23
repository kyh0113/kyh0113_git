def solution(n, lost, reserve):
    std=[1]*n # 0~4인덱스 값 1
    
    for i in reserve:
        std[i-1] = 2 # 0,2,4 인덱스값 2
    
    for i in lost:
        std[i-1] = std[i-1]-1 # 1,3인덱스값 0
    
    for i, v in enumerate(std):
        # 오른쪽 학생이 빌려줄 경우
        if i<n-1 and v==0 and std[i+1]==2:
            std[i]=1
            std[i+1]=1
            
        # 왼쪽 학생이 빌려줄 경우
        elif i>0 and v==0 and std[i-1]==2:
            std[i]=1
            std[i-1]=1
        
    return n-std.count(0) # 옷이 없을 학생 수 제외