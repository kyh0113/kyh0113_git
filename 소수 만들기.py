def sosu(a, b, c):
    total = a+b+c
    for i in range(2,total):
        if total%i==0:
            return False
    return True

def solution(nums): # 3개의 수를 보내는 함수를 만들기
    cnt=0
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if sosu(nums[i], nums[j], nums[k])==True:
                    cnt+=1
    return cnt