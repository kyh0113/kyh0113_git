def solution(s):
    if len(s)==4 or len(s)==6:
        for i in range(len(s)):
            if s[i] not in "0123456789":
                return False
            elif s[i] in "0123456789":
                return True
    else : # s길이가 4와 6이 아닌 경우
        return False