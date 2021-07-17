import sys
M = int(sys.stdin.readline())
S=set()

for i in range(M):
    st=sys.stdin.readline().strip().split()

    if len(st)==1:
        if st[0]=='all':
            S=set([i for i in range(1, 21)])
        else:
            S=set()
    else:
        if st[0]== "add":
            S.add(int(st[1]))
        elif st[0]=="remove":
            S.discard(int(st[1]))
        elif st[0]=="check":
            if int(st[1]) in S:
                print(1)
            else:
                print(0)
        elif st[0]=="toggle":
            if int(st[1]) in S:
                S.discard(int(st[1]))
            else:
                S.add(int(st[1]))
