import sys
a,b = map(int, sys.stdin.readline().split()) # a:21 b:5
cnt = 0

while 1:
    # a가 나눠질 수 있는 수가 될 수 있을때 까지 뺀 수를 cnt에 더하기
    target = (a//b)*b 
    cnt += a-target 
    a = target 
    
    # a가 나눠야 할 수(b)보다 작으면 멈추기 
    if a<b:
        break
    
    a = a//b 
    cnt += 1 # 계산 한번 됬으니깐 카운트 +1
    
# 나눠질 수 있는 수보다 작아지면 그 수가 1이 되기까지 1을 몇번 빼줘야 하는지 나타내야함
# ex) 5가 1이 되려면 1을 몇번 빼줘야 하는가? 5-1번 즉 4번
cnt += a-1
print(cnt)


