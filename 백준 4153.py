import sys
while(1):
    tri = sorted(list(map(int, sys.stdin.readline().split()))) # 정렬을 통해 기준 잡기
    if 0 in tri: # 종료조건 (0입력 되면 끝내기)
        break
    elif tri[2]**2 == (tri[0]**2) + (tri[1]**2):
        print('right')
    else:
        print('wrong') 