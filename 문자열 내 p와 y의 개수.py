def solution(s):
    s=s.lower()
    s_p=s.count('p')
    s_y=s.count('y')
    if s_p==s_y:
        return True
    else:
        return False