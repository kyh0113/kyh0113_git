while(1):
    st=input() # str로 받고
    l=list(map(int,str(st))) # 숫자로 나눔
    if st=="0":
        break

    while len(l) !=0:
        if len(l) % 2 ==1:
            mid=((0+len(l))//2) # 홀수면 가운데꺼 버리기
            l.pop(mid)
        else:
            if l[0] == l[-1]:
                l.pop(0)
                l.pop(-1)
            else:
                print('no')
                break
    #     break    
    # print('yes')
    if len(l)==0:
        print('yes')
# l=[1, 2, 4, 2, 1]
# if len(l) % 2== 1:
#     mid=((0+len(l))//2)
#     l.pop(mid)
# print(l)